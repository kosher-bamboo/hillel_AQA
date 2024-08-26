import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

driver = Chrome()

driver.get("http://localhost:8000/dz.html")

# get all iframes from main page
iframes = driver.find_elements(By.XPATH, "//*[contains(@id, 'frame')]")
for iframe in iframes:
    # get id of the iframe
    iframe_id = iframe.get_attribute('id')
    driver.switch_to.frame(driver.find_element(By.ID, iframe_id))
    input_field = driver.find_element(By.ID, f"input{iframe_id[-1]}")
    input_field.send_keys(f"Frame{iframe_id[-1]}_Secret")
    button = driver.find_element(By.TAG_NAME, 'button')
    button.click()
    time.sleep(1)

    alert = Alert(driver)
    if alert.text == f"Верифікація пройшла успішно!":
        print(alert.text)
    else:
        print(alert.text)
    alert.accept()
    driver.switch_to.default_content()
