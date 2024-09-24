from selenium.webdriver.common.by import By


class ForstudyProfilePageElements:
    EDIT_PROFILE_BUTTON = (By.XPATH, '//button[@class="btn btn-primary"]')
    CLOSE_BUTTON = (By.XPATH, '//button[@class="close"]')
    USER_FULL_NAME = (By.XPATH, '//p[@class="profile_name display-4"]')
    LOGOUT_BUTTON = (By.XPATH, '//button[@class="dropdown-item btn btn-link user-nav_link"]')
