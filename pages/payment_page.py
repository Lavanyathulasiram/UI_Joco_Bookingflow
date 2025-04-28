import logging
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utils.base_page import BasePage

class PaymentPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        # No need for self.driver = driver again

    def confirm_booking(self):
        logging.info("Confirming booking by clicking 'OK' button after booking.")
        self.click((By.CSS_SELECTOR, ".btn.btn-primary.btn-yes"))

    def verify_traveller_name(self, first, last):
        logging.info(f"Verifying traveller name: Expected - {first} {last}")
        expected = f"{first} {last}".strip().upper()
        actual_raw = self.wait_until_present(
            (By.XPATH, "(//tr[@class='booking-data ng-scope']//div[@id='fullnameContainer']/div)[1]")
        ).text.strip().upper()
        actual = actual_raw.split('.', 1)[1].strip() if '.' in actual_raw else actual_raw

        if expected == actual:
            logging.info("Traveller name matches successfully.")
        else:
            logging.error(f"Traveller name mismatch! Expected: {expected}, Found: {actual}")
        return expected == actual

    def make_payment(self):
        logging.info("Initiating payment by clicking on 'Make Payment' option.")
        self.click((By.CLASS_NAME, "dropdown-toggle"))
        self.click((By.XPATH, "//button[@value='makePayment']"))
        logging.info("Clicked on 'Make Payment' button, waiting for payment options to load.")
        time.sleep(5)

    def confirm_payment(self):
        logging.info("Waiting for loading spinner to disappear before confirming payment.")
        self.wait_until_invisible((By.CLASS_NAME, "cg-busy-backdrop"))

        logging.info("Waiting for 'Confirm Payment' button to be clickable.")
        confirm_payment_button = self.wait_until_clickable(
            (By.XPATH, "//button[contains(@class, 'btn-pay') and contains(text(), 'CONFIRM PAYMENT')]")
        )
        self.driver.execute_script("arguments[0].scrollIntoView({behavior:'smooth', block:'center'});", confirm_payment_button)
        time.sleep(2)
        logging.info("Clicking 'Confirm Payment' button.")
        confirm_payment_button.click()

        logging.info("Waiting for payment confirmation popup to appear.")
        self.wait_until_present((By.CSS_SELECTOR, ".paymentModelPopup.ng-scope"))

        logging.info("Waiting for internal spinner to disappear after clicking Confirm Payment.")
        self.wait_until_invisible((By.CLASS_NAME, "cg-busy-default-spinner"))

        logging.info("Finding and clicking the final 'Confirm Payment' button.")
        final_confirm_button = self.wait_until_clickable((By.CSS_SELECTOR, ".btn.btn-primary.btn-add.ng-scope"))
        self.driver.execute_script("arguments[0].scrollIntoView({behavior:'smooth', block:'center'});", final_confirm_button)
        time.sleep(2)
        final_confirm_button.click()
        logging.info("Final payment confirmation completed successfully.")
