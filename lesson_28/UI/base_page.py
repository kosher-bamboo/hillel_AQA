from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def current_page_url(self, timeout, url):
        return WebDriverWait(self.driver, timeout).until(EC.url_contains(url))

    def element_is_present(self, locator, timeout):
        return WebDriverWait(self.driver, timeout=timeout).until(EC.presence_of_element_located(locator))

    def element_is_clickable(self, locator, timeout):
        return WebDriverWait(self.driver, timeout=timeout).until(EC.element_to_be_clickable(locator))

    def click_on_element(self, locator, timeout=2):
        element = self.element_is_clickable(locator=locator, timeout=timeout)
        element.click()

    def input_data(self, locator, data, timeout=3):
        element = self.element_is_present(locator=locator, timeout=timeout)
        element.send_keys(data)

    def get_text(self, locator, timeout=2):
        return self.element_is_present(locator=locator, timeout=2).text
