from lesson_28.UI.base_page import BasePage
from lesson_28.UI.forstudy.elements.forstudy_panel_elements import ForstudyPanelElements


class GaragePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver)
        self.elements = ForstudyPanelElements()

    def click_fuel_expenses(self):
        self.click_on_element(locator=self.elements.LINK_TO_FUEL_EXPENSES, timeout=2)
        return self

    def click_instructions(self):
        self.click_on_element(locator=self.elements.LINK_TO_INSTRUCTIONS, timeout=2)
        return self

    def click_profile(self):
        self.click_on_element(locator=self.elements.LINK_TO_PROFILE, timeout=2)
        return self

    def click_settings(self):
        self.click_on_element(locator=self.elements.LINK_TO_SETTINGS, timeout=2)
        return self

    def click_log_out(self):
        self.click_on_element(locator=self.elements.LOG_OUT, timeout=2)

    def get_url(self, url):
        self.current_page_url(url=url, timeout=3)
        return self
