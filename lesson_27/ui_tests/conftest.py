import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='session')
def driver():
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Run Chrome in headless mode
    chrome_options.add_argument('--no-sandbox')  # Important for running in Jenkins
    chrome_options.add_argument('--disable-dev-shm-usage')  # For better memory usage

    driver = webdriver.Chrome(options=chrome_options)

    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def track_number():
    return '20450952733334'
