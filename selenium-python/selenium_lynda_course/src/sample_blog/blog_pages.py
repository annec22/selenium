from src.sample_blog.blog_locators import SignUpPageSelectors, UserPageSelectors


class Page:
    def __init__(self, driver, base_url="https://selenium-blog.herokuapp.com/"):
        self.base_url = base_url
        self.driver = driver

    def open(self, url=""):
        self.driver.get(self.base_url + url)


class SignUpPage(Page):

    def enter_username(self, username):
        self.driver.find_element(*SignUpPageSelectors.USERNAME_FIELD).send_keys(username)

    def enter_email(self, email):
        self.driver.find_element(*SignUpPageSelectors.EMAIL_FIELD).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*SignUpPageSelectors.PASSWORD_FIELD).send_keys(password)

    def submit_signup_form(self):
        self.driver.find_element(*SignUpPageSelectors.SUBMIT_BUTTON).click()


class UserPage(Page):

    def get_signup_success_banner_text(self):
        return self.driver.find_element(*UserPageSelectors.SUCCESS_BANNER).text
