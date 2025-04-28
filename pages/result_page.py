import logging
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from utils.base_page import BasePage

class ResultPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        # No need to assign self.driver again (already in BasePage)

    def wait_for_results_page(self):
        logging.info("Waiting for the results page to load.")
        self.wait_until_url_contains("/flightSearch/results")
        logging.info("Results page URL detected.")

        # Handle loader if visible
        logging.info("Checking for any loading indicators before showing results.")
        start_time = time.time()
        max_wait = 300  # 5 minutes max wait for loader to disappear

        while True:
            try:
                loader = self.driver.find_element(
                    By.XPATH,
                    "//div[contains(@class, 'loading') and (contains(@class, 'before-results') or contains(@class, 'partial-results'))]"
                )
                if not loader.is_displayed():
                    logging.info("Loading completed. No loaders visible.")
                    break
            except:
                logging.info("No loading div found, continuing...")
                break

            if (time.time() - start_time) > max_wait:
                logging.error("Loader timeout after 5 minutes.")
                raise Exception("Loader timeout after 5 minutes.")

            time.sleep(2)

        # Escape any popups
        logging.info("Sending ESCAPE key to close any Chrome popups.")
        time.sleep(2)
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()

    def click_book_button(self):
        logging.info("Waiting for flight search results to appear.")
        self.wait_until_present((By.CSS_SELECTOR, "tr[id^='recommendation']"))
        
        logging.info("Waiting for the first 'Book' button to become clickable.")
        first_book_button = self.wait_until_clickable((By.CLASS_NAME, "btn-book"))
        
        logging.info("Clicking the 'Book' button for the first available flight.")
        first_book_button.click()
