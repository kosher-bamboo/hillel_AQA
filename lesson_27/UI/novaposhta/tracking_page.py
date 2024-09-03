from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from lesson_27.UI.base_page import BasePage


class TrackingPage(BasePage):
    INPUT_FIELD = (By.ID, 'en')
    SEARCH_BUTTON = (By.ID, 'np-number-input-desktop-btn-search-en')
    AGREE_BUTTON = (By.XPATH, '//span[contains(text(), " Добре ")]')
    STATUS = (By.XPATH, '//div[@class="header__status-text"]')

    def __init__(self, driver, url):
        super().__init__(driver=driver, url=url)

    def fill_input_field(self, data):
        self.input_data(locator=self.INPUT_FIELD, data=data)
        return self

    def click_search_button(self):
        self.click_on_element(locator=self.SEARCH_BUTTON)
        return self

    def click_agree_button(self):
        self.click_on_element(locator=self.AGREE_BUTTON)
        return self

    def get_status(self):
        return self.driver.find_element(*self.STATUS).text
