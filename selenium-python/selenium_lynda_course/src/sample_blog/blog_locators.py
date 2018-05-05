from selenium.webdriver.common.by import By


class SignUpPageSelectors:
    USERNAME_FIELD = (By.ID, "user_username")
    EMAIL_FIELD = (By.ID, "user_email")
    PASSWORD_FIELD = (By.ID, "user_password")
    SUBMIT_BUTTON = (By.ID, "submit")


class UserPageSelectors:
    SUCCESS_BANNER = (By.ID, "flash_success")
