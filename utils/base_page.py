from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self, locator, value):
        self.wait.until(EC.element_to_be_clickable(locator)).send_keys(value)

    def scroll_into_view(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({behavior:'smooth', block:'center'});", element)

    def wait_until_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_until_present(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_until_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_until_invisible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def wait_until_url_contains(self, text):
        return self.wait.until(EC.url_contains(text))
