from selenium.webdriver.common.by import By


class ForstudyPanelElements:
    LINK_TO_GARAGE = (By.XPATH, '//a[@routerlink="garage"]')
    LINK_TO_FUEL_EXPENSES = (By.XPATH, '//a[@routerlink="expenses"]')
    LINK_TO_INSTRUCTIONS = (By.XPATH, '//a[@routerlink="instructions"]')
    LINK_TO_PROFILE = (By.XPATH, '//a[@routerlink="profile"]')
    LINK_TO_SETTINGS = (By.XPATH, '//a[@routerlink="settings"]')
    LOG_OUT = (By.XPATH, '//a[@class="btn btn-link text-danger btn-sidebar sidebar_btn"]')
