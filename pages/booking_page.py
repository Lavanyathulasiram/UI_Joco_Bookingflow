import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from utils.base_page import BasePage

class BookingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        # No need to assign self.driver again (already assigned in BasePage)

    def confirm_review_details(self):
        logging.info("Confirming review details by clicking 'Add Traveller Info' button.")
        self.click((By.ID, "addTravellerInfo"))

    def fill_traveler_info(self, first, last):
        logging.info(f"Filling traveler information: {first} {last}")
        Select(self.wait_until_present((By.ID, "additionalVesselName"))).select_by_visible_text("INS Vikrant")
        logging.info("Selected vessel name: INS Vikrant")
        
        Select(self.wait_until_present((By.ID, "purposeOfTravel"))).select_by_visible_text("Office-Briefing")
        logging.info("Selected purpose of travel: Office-Briefing")
        
        Select(self.wait_until_present((By.ID, "salutation"))).select_by_visible_text("Mr")
        logging.info("Selected salutation: Mr")
        
        self.send_keys((By.ID, "firstName"), first)
        logging.info(f"Entered first name: {first}")
        
        self.send_keys((By.ID, "lastName"), last)
        logging.info(f"Entered last name: {last}")
        
        Select(self.wait_until_present((By.ID, "rank"))).select_by_visible_text("Master")
        logging.info("Selected rank: Master")

    def book_and_pay(self):
        logging.info("Scrolling to 'Book and Pay' button.")
        self.scroll_into_view((By.CSS_SELECTOR, ".btn.btn-warning.bookAndPay"))
        logging.info("Clicking 'Book and Pay' button.")
        self.click((By.CSS_SELECTOR, ".btn.btn-warning.bookAndPay"))

    def handle_price_popup(self):
        try:
            logging.info("Checking if price change popup is visible.")
            self.wait_until_present((By.XPATH, "//div[@ng-show='priceChanged' and not(contains(@class, 'ng-hide'))]"))
            self.click((By.ID, "changePriceAgree"))
            logging.info("Price change popup detected. Agreed to updated price.")
        except Exception:
            logging.info("No price change popup appeared.")
