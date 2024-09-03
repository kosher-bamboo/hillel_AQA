import pytest
from selenium.webdriver import Chrome


@pytest.fixture(scope='session')
def driver():
    return Chrome()


@pytest.fixture(scope='session')
def url():
    return 'https://tracking.novaposhta.ua/#/uk'


@pytest.fixture(scope='session')
def track_number():
    return '20450952733334'
