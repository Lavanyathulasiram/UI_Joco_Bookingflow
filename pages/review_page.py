import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.base_page import BasePage

class ReviewPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 20)
        # No need to do self.driver = driver again (BasePage already assigns driver)

    def confirm_review_details(self):
        logging.info("Waiting for 'Add Traveller Info' button to become clickable.")
        confirm_btn = self.wait.until(
            EC.element_to_be_clickable((By.ID, "addTravellerInfo"))
        )
        logging.info("Clicking on 'Add Traveller Info' button to confirm review details.")
        confirm_btn.click()
