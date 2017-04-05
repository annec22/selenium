from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

import unittest
from selenium.webdriver.support.expected_conditions import _find_element

class LoginTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.facebook.com/")
        
    def test_Login(self):
        driver = self.driver
        facebookUsername = "USERNAME"
        facbookPassword = "PASSWORD"
        emailFieldID        = "email"
        passwordFieldID     = "pass"
        loginButtonXpath    = "//input[@value='Log In']"
        fbLogoXpath         = "//a[contains(@href, '?ref=logo')]"
    
        emailFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(emailFieldID))
        passFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(passwordFieldID))
        loginButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(loginButtonXpath))
        
        emailFieldElement.clear()
        emailFieldElement.send_keys(facebookUsername)
        passFieldElement.clear()
        passFieldElement.send_keys(facbookPassword)
        loginButtonElement.click()
        
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(fbLogoXpath))
        
    def tearDown(self):
        self.driver.quit()
        
        
if __name__ == '__main__':
    unittest.main()

        