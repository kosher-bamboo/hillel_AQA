from selenium.webdriver.common.by import By


class TrackingPageElements:
    INPUT_FIELD = (By.ID, 'en')
    SEARCH_BUTTON = (By.ID, 'np-number-input-desktop-btn-search-en')
    AGREE_BUTTON = (By.XPATH, '//span[contains(text(), " Добре ")]')
    STATUS = (By.XPATH, '//div[@class="header__status-text"]')
