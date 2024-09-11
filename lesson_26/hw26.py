import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


@pytest.fixture()
def driver():
    driver = Chrome()
    yield driver
    driver.quit()


url = "http://localhost:8000/dz.html"


@pytest.mark.parametrize("frame, input, secret, expected", [
    ("frame1", "input1", "Frame1_Secret", "Верифікація пройшла успішно!"),
    ("frame2", "input2", "Frame2_Secret", "Верифікація пройшла успішно!")
], ids=["frame1", "frame2"])
def test_check_alert(driver, frame, input, secret, expected):
    driver.get(url)
    driver.find_element(By.ID, frame)
    driver.switch_to.frame(driver.find_element(By.ID, frame))
    input_field = driver.find_element(By.ID, input)
    input_field.send_keys(secret)
    button = driver.find_element(By.TAG_NAME, 'button')
    button.click()
    alert = driver.switch_to.alert

    assert alert.text == expected, "Incorrect text input"

    alert.accept()
