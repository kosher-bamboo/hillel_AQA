from lesson_27.UI.base_page import BasePage


class NovaposhtaBasePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver, url='https://tracking.novaposhta.ua/#/uk')
