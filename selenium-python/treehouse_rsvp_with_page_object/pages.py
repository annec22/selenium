from selenium import webdriver
from selenium.webdriver.common.by import By

from locators import HomePageLocators, InviteeLocators
# from selenium.webdriver.common.action_chains import ActionChains


class Page():
    def __init__(self, driver, base_url="http://localhost/rsvp/index.html"):
        self.base_url = base_url
        self.driver = driver
        # self.timeout = 30

    def open(self, url=""):
        self.driver.get(self.base_url + url)


class HomePage(Page):
    def add_invitee(self, name):
        self.driver.find_element(*HomePageLocators.INVITE_FORM_NAME_FIELD).send_keys(name)
        self.driver.find_element(*HomePageLocators.INVITE_FORM).submit()

    def toggle_non_responders_visibility(self):
        self.driver.find_element(*HomePageLocators.TOGGLE_RESPONDERS_CHECKBOX).click()

    def find_invitee_by_name(self, name):
        element = self.driver.find_element(*HomePageLocators.INVITEE_BY_NAME(name))
        return Invitee(element)

    def get_invitee_count(self):
        elements = self.driver.find_elements(*HomePageLocators.INVITEES_COUNT)
        return len(elements)




class Invitee():
    def __init__(self, element):
        self.element = element
        self.edit_save_button = self.element.find_element(*InviteeLocators.EDIT_AND_SAVE_BUTTON)

    def remove(self):
        self.element.find_element(*InviteeLocators.REMOVE_BUTTON).click()

    def toggle_confirmation(self):
        self.element.find_element(*InviteeLocators.CONFIRM_CHECKBOX).click()

    def rename(self, new_name):
        self.edit_save_button.click()
        NAME_FIELD = self.element.find_element(*InviteeLocators.NAME_FIELD)
        NAME_FIELD.clear()
        NAME_FIELD.send_keys(new_name)
        self.edit_save_button.click()