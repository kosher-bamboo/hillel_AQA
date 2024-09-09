from lesson_28.UI.base_page import BasePage
from lesson_28.UI.forstudy.elements.forstudy_profile_page_elements import ForstudyProfilePageElements


class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver)
        self.elements = ForstudyProfilePageElements()

    def get_user_name(self):
        asd = self.get_text(locator=self.elements.USER_FULL_NAME, timeout=2)
        asdf = asd.split()
        return asdf[0]

    def get_user_last_name(self):
        asd = self.get_text(locator=self.elements.USER_FULL_NAME, timeout=2)
        asdf = asd.split()
        return asdf[1]
