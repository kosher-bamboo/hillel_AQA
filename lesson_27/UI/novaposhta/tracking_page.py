import allure

from lesson_27.UI.novaposhta.elements.tracking_page_elements import TrackingPageElements
from lesson_27.UI.base_page import BasePage
import allure


@allure.epic("Tracking Page")
class TrackingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver, url='https://tracking.novaposhta.ua/#/uk')
        self.elements = TrackingPageElements()

    @allure.step("Fill track number")
    def fill_input_field(self, data):
        self.input_data(locator=self.elements.INPUT_FIELD, data=data)
        return self

    @allure.step("Click 'Search' button")
    def click_search_button(self):
        self.click_on_element(locator=self.elements.SEARCH_BUTTON)
        return self

    @allure.step("Click 'Agree' button")
    def click_agree_button(self):
        self.click_on_element(locator=self.elements.AGREE_BUTTON)
        return self

    @allure.step("Get package status")
    def get_status(self):
        return self.get_text(locator=self.elements.STATUS)
