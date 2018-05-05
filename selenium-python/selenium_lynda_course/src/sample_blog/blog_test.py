from selenium import webdriver
import unittest

from src.sample_blog.blog_pages import SignUpPage, UserPage


class SignUpFormTesting(unittest.TestCase):

    def setUp(self):
        self.username = 'hhtest_user_username13'
        self.email = 'hhtest_user_email13@hhtest.com'
        self.password = 'user_password'
        self.driver = webdriver.Firefox() #local browser
        # self.driver = webdriver.Remote(
        #     command_executor='http://localhost:5555/wd/hub',
        #     desired_capabilities={'browserName': 'firefox', 'javascriptEnabled': True}) #remote_browser
        self.signup_page = SignUpPage(self.driver)
        self.signup_page.open('signup')

    def test_signup(self):
        welcome_message = 'Welcome to the alpha blog ' + self.username
        self.signup_page.enter_username(self.username)
        self.signup_page.enter_email(self.email)
        self.signup_page.enter_password(self.password)
        self.signup_page.submit_signup_form()
        self.user_page = UserPage(self.driver)
        self.assertEqual(self.user_page.get_signup_success_banner_text(), welcome_message)

    def tearDown(self):
        self.driver.close()

#class Login
#class CreateBlogPost


if __name__ == '__main__':
    unittest.main()
