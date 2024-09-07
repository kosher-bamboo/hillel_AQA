import time
import pytest
from selenium import webdriver

from lesson_28.UI.forstudy.pages.forstudy_sign_up_page import SignUpPage
from lesson_28.UI.forstudy.pages.forstudy_log_in_page import LogInPage
from lesson_28.UI.forstudy.pages.forstudy_garage_page import GaragePage


@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def open_main_page(driver):
    def _open_main_page():
        driver.get('https://guest:welcome2qauto@qauto2.forstudy.space')

    return _open_main_page


@pytest.fixture(scope='session')
def register_user(driver):
    def _register_user(name, last_name, email, password):
        sign_up_page = SignUpPage(driver)
        sign_up_page.click_sign_up_button().input_name(name).input_last_name(last_name).input_email(email).input_password(password).input_re_enter_password(password).click_register_button()

    return _register_user


@pytest.fixture(scope='session')
def log_in_user(driver):
    def _log_in_user(email, password):
        log_in_page = LogInPage(driver)
        log_in_page.click_sign_in_button().input_email(email).input_password(password).click_login_button()

    return _log_in_user


@pytest.fixture(scope='session')
def log_out_user(driver):
    def _log_out_user():
        garage_page = GaragePage(driver)
        garage_page.click_my_profile_dropdown().click_log_out()

    return _log_out_user

