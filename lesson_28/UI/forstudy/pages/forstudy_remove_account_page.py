from lesson_28.UI.base_page import BasePage
from lesson_28.UI.forstudy.elements.forstudy_remove_account_elements import ForstudyRemoveAccountElements


class RemoveAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver)
        self.elements = ForstudyRemoveAccountElements()

    def click_delete_my_account(self):
        self.click_on_element(locator=self.elements.REMOVE_MY_ACCOUNT_BUTTON, timeout=2)
        return self

    def click_cancel(self):
        self.click_on_element(locator=self.elements.CANCEL_BUTTON)
        return self

    def click_remove(self):
        self.click_on_element(locator=self.elements.REMOVE_BUTTON)
        return self
