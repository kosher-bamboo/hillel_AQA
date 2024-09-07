from selenium.webdriver.common.by import By


class ForstudyGaragePageElements:
    # part URL: /panel/garage
    MY_PROFILE_DROPDOWN = (By.ID, 'userNavDropdown')
    # /panel/profile
    LINK_TO_PROFILE = (By.XPATH, '//div[@class="user-nav_menu-group"]//a[@href="/panel/profile"]')
    LOG_OUT = (By.XPATH, '//button[@class="dropdown-item btn btn-link user-nav_link"]')
