from lesson_27.UI.novaposhta.elements.tracking_page_elements import TrackingPageElements
from lesson_27.UI.novaposhta.novaposhta_base_page import NovaposhtaBasePage


class TrackingPage(NovaposhtaBasePage):
    def __init__(self, driver):
        super().__init__(driver=driver)
        self.elements = TrackingPageElements()

    def fill_input_field(self, data):
        self.input_data(locator=self.elements.INPUT_FIELD, data=data)
        return self

    def click_search_button(self):
        self.click_on_element(locator=self.elements.SEARCH_BUTTON)
        return self

    def click_agree_button(self):
        self.click_on_element(locator=self.elements.AGREE_BUTTON)
        return self

    def get_status(self):
        return self.driver.find_element(*self.elements.STATUS).text
