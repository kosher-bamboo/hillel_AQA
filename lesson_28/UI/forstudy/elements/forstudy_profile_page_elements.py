from selenium.webdriver.common.by import By


class ForstudyProfilePageElements:
    EDIT_PROFILE_BUTTON = (By.XPATH, '//button[@class="btn btn-primary"]')
    CLOSE_BUTTON = (By.XPATH, '//button[@class="close"]')
    PROFILE_NAME = (By.XPATH, '//input[@id="editProfileName"]')
    PROFILE_LAST_NAME = (By.XPATH, '//input[@id="editProfileLastName"]')
    LOGOUT_BUTTON = (By.XPATH, '//button[@class="dropdown-item btn btn-link user-nav_link"]')
