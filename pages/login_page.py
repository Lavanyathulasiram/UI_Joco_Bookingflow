import logging
from selenium.webdriver.common.by import By
from utils.base_page import BasePage
from utils.config import Config


class LoginPage(BasePage):
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Login')]")

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, email, password):
        logging.info(f"Attempting login with email: {email}")
        self.send_keys(self.EMAIL_INPUT, email)
        self.send_keys(self.PASSWORD_INPUT, password)
        logging.info("Password entered.")
        self.click(self.LOGIN_BUTTON)
        logging.info("Login button clicked.")