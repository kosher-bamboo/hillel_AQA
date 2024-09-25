import allure

from lesson_28.UI.base_page import BasePage
from lesson_28.UI.forstudy.elements.forstudy_main_page_elements import ForstudySignInElements


class LogInPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver)
        self.elements = ForstudySignInElements()

    @allure.step("Click Sign in button")
    def click_sign_in_button(self):
        self.click_on_element(locator=self.elements.SIGN_IN_BUTTON, timeout=2)
        return self

    @allure.step("Input email")
    def input_email(self, data):
        self.input_data(locator=self.elements.SIGN_IN_EMAIL, data=data, timeout=2)
        return self

    @allure.step("Input password")
    def input_password(self, data):
        self.input_data(locator=self.elements.SIGN_IN_PASSWORD, data=data, timeout=2)
        return self

    @allure.step("Click Login button")
    def click_login_button(self):
        self.click_on_element(locator=self.elements.LOGIN_BUTTON, timeout=2)
        return self
