from lesson_28.UI.base_page import BasePage
from lesson_28.UI.forstudy.elements.forstudy_main_page_elements import ForstudySignInElements


class LogInPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver)
        self.elements = ForstudySignInElements()

    def click_sign_in_button(self):
        self.click_on_element(locator=self.elements.SIGN_IN_BUTTON, timeout=2)
        return self

    def input_email(self, data):
        self.input_data(locator=self.elements.SIGN_IN_EMAIL, data=data, timeout=2)
        return self

    def input_password(self, data):
        self.input_data(locator=self.elements.SIGN_IN_PASSWORD, data=data, timeout=2)
        return self

    def click_login_button(self):
        self.click_on_element(locator=self.elements.LOGIN_BUTTON, timeout=2)
        return self
