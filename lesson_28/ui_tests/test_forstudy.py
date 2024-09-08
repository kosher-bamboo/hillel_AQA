import pytest
import time
from faker import Faker
import logging

from lesson_28.ui_tests.conftest import log_out_user

fake = Faker()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# File handler
file_handler = logging.FileHandler('input_data.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


name = fake.first_name()
last_name = fake.last_name()
email = fake.email()
password = fake.password()


def test_forstudy_sign_up(driver, open_main_page, register_user, log_out_user, log_in_user):
    open_main_page()
    register_user(name=name, last_name=last_name, email=email, password=password)
    logger.info(f"Registered user: name:{name}, last name {last_name}, email: {email}, password: {password}")
    # time.sleep(1)
    # assert check_that_user_is_registered(), "User not registered"

    log_out_user()

    log_in_user(email=email, password=password)
    logger.info(f"Try to login with email: {email}, password: {password}")
    # time.sleep(60)