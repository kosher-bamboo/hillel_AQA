from selenium.webdriver.common.by import By


class ForstudySignUpElements:
    SIGN_UP_BUTTON = (By.XPATH, '//button[@class="hero-descriptor_btn btn btn-primary"]')
    NAME_INPUT_FIELD = (By.ID, 'signupName')
    LAST_NAME_INPUT_FIELD = (By.ID, 'signupLastName')
    EMAIL_INPUT_FIELD = (By.ID, 'signupEmail')
    PASSWORD_INPUT_FIELD = (By.ID, 'signupPassword')
    RE_ENTER_PASSWORD_INPUT_FIELD = (By.ID, 'signupRepeatPassword')
    REGISTER_BUTTON = (By.XPATH, '//button[@class="btn btn-primary"]')


class ForstudySignInElements:
    SIGN_IN_BUTTON = (By.XPATH, '//button[@class="btn btn-outline-white header_signin"]')
    SIGN_IN_EMAIL = (By.ID, 'signinEmail')
    SIGN_IN_PASSWORD = (By.ID, 'signinPassword')
    LOGIN_BUTTON = (By.XPATH, '//button[@class="btn btn-primary"]')

