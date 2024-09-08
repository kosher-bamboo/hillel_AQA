from selenium.webdriver.common.by import By

from lesson_28.UI.base_page import BasePage
from lesson_28.UI.forstudy.elements.forstudy_garage_page_elements import ForstudyGaragePageElements


class GaragePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver)
        self.elements = ForstudyGaragePageElements()


    def click_my_profile_dropdown(self):
        self.click_on_element(locator=self.elements.MY_PROFILE_DROPDOWN, timeout=2)
        return self


    def click_log_out(self):
        self.click_on_element(locator=self.elements.LOG_OUT, timeout=2)


    def click_profile_url(self):
        self.click_on_element(locator=self.elements.LINK_TO_PROFILE, timeout=2)
        return self


    # def check_notification(self):
        # return self.get_text(locator=self.elements.SUCCESSFUL_LOGIN_NOTIFICATION, timeout=1) == "Registration complete"


    def check_login_state(self, base_url):
        self.current_page_url() == base_url + "panel/garage"
        return self