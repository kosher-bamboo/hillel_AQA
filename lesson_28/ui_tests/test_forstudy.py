import pytest
from lesson_28.logger import logger
from lesson_28.ui_tests.conftest import check_last_name, check_name, remove_account, log_in_user
from faker import Faker

fake = Faker()

name = fake.first_name()
last_name = fake.last_name()
email = fake.email()
password = fake.password()


def test_forstudy_sign_up(driver, open_main_page, register_user, check_user_is_logged_in, log_out_user,
                          log_in_user, remove_account):
    open_main_page()
    register_user(name=name, last_name=last_name, email=email, password=password)
    logger.info(f"Registered user: name: {name}, last name: {last_name}, email: {email}, password: {password}")

    assert check_user_is_logged_in(), "User not registered"

    log_out_user()
    log_in_user(email=email, password=password)
    logger.info(f"Try to login with email: {email}, password: {password}")

    assert check_user_is_logged_in, "User isn't logged in"

    # remove_account()


@pytest.mark.parametrize("field, expected_value", [
    ("name", name),  # Check name
    ("last_name", last_name)  # Check last name
])
def test_forstudy_check_name(driver, open_main_page, register_user, log_in_user, check_name, check_last_name,
                             field, expected_value, remove_account):
    if field == "name":
        # open_main_page()
        # register_user(name=name, last_name=last_name, email=email, password=password)
        # logger.info(f"Registered user: name: {name}, last name: {last_name}, email: {email}, password: {password}")

        assert check_name() == expected_value, f"Expected {expected_value} but found {check_name()}"

    if field == "last_name":
        actual_last_name = check_last_name()
        remove_account()
        assert actual_last_name == expected_value, f"Expected {expected_value}, but found {actual_last_name}"
