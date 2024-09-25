from lesson_28.UI.base_page import BasePage
from lesson_28.UI.forstudy.elements.forstudy_main_page_elements import ForstudySignUpElements
import allure


class SignUpPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver)
        self.elements = ForstudySignUpElements()

    @allure.step("Click Sign up button")
    def click_sign_up_button(self):
        self.click_on_element(locator=self.elements.SIGN_UP_BUTTON, timeout=2)
        return self

    @allure.step("Input name")
    def input_name(self, data):
        self.input_data(locator=self.elements.NAME_INPUT_FIELD, data=data, timeout=2)
        return self

    @allure.step("Input last name")
    def input_last_name(self, data):
        self.input_data(locator=self.elements.LAST_NAME_INPUT_FIELD, data=data, timeout=2)
        return self

    @allure.step("Input email")
    def input_email(self, data):
        self.input_data(locator=self.elements.EMAIL_INPUT_FIELD, data=data, timeout=2)
        return self

    @allure.step("Input password")
    def input_password(self, data):
        self.input_data(locator=self.elements.PASSWORD_INPUT_FIELD, data=data, timeout=2)
        return self

    @allure.step("Re-enter password")
    def input_re_enter_password(self, data):
        self.input_data(locator=self.elements.RE_ENTER_PASSWORD_INPUT_FIELD, data=data, timeout=2)
        return self

    @allure.step("Click register button")
    def click_register_button(self):
        self.click_on_element(locator=self.elements.REGISTER_BUTTON, timeout=2)
        return self
