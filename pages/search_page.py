import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
from utils.base_page import BasePage

class SearchFlightPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def search_flight(self, origin, destination):
        logging.info(f"Starting flight search: Origin = {origin}, Destination = {destination}")

        # Select Origin
        logging.info("Entering origin city.")
        origin_input = self.wait_until_clickable((By.ID, "origin"))
        self.scroll_into_view((By.ID, "origin"))
        origin_input.clear()
        origin_input.send_keys(origin)
        first_origin = self.wait_until_visible((By.XPATH, "//li[contains(@id,'option')][1]/a"))
        ActionChains(self.driver).move_to_element(first_origin).click().perform()
        logging.info(f"Selected first suggestion for origin: {origin}")

        # Select Destination
        logging.info("Entering destination city.")
        dest_input = self.wait_until_clickable((By.ID, "destination"))
        self.scroll_into_view((By.ID, "destination"))
        dest_input.clear()
        dest_input.send_keys(destination)
        first_dest = self.wait_until_visible((By.XPATH, "(//ul[contains(@class, 'dropdown-menu')])[2]//li[1]/a"))
        ActionChains(self.driver).move_to_element(first_dest).click().perform()
        logging.info(f"Selected first suggestion for destination: {destination}")

        # Select Travel Date
        future_date = datetime.now() + timedelta(days=2)
        desired_date = str(future_date.day)
        logging.info(f"Selecting travel date {future_date.strftime('%d-%b-%Y')} (day = {desired_date}).")
        date_field = self.wait_until_clickable((By.ID, "fromDate"))
        self.driver.execute_script("arguments[0].click();", date_field)
        date_xpath = f"//td[not(contains(@class,'disabled'))]//button[span[text()='{desired_date}']]"
        date_element = self.wait_until_clickable((By.XPATH, date_xpath))
        self.driver.execute_script("arguments[0].click();", date_element)
        logging.info(f"Selected date: {desired_date}")

        # Click Search
        self.click((By.ID, "search"))
        logging.info("Clicked on 'Search' button to find flights.")
