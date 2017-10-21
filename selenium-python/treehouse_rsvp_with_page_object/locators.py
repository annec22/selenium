from selenium.webdriver.common.by import By


class HomePageLocators():
    INVITE_FORM = (By.ID, "registrar")
    INVITE_FORM_NAME_FIELD = (By.CSS_SELECTOR, "#registrar input[name='name']")
    TOGGLE_RESPONDERS_CHECKBOX = (By.CSS_SELECTOR, ".main > div input[type='checkbox']")
    INVITEE_BY_NAME = lambda name: (By.XPATH, f"//span[text() = '{name}']/..")
    INVITEES_COUNT = (By.CSS_SELECTOR, "#invitedList li")


class InviteeLocators():
    EDIT_AND_SAVE_BUTTON = (By.CSS_SELECTOR, "button:first-of-type")
    REMOVE_BUTTON = (By.CSS_SELECTOR, "button:last-child")
    CONFIRM_CHECKBOX = (By.CSS_SELECTOR, "input[type='checkbox']")
    NAME_FIELD = (By.CSS_SELECTOR, "input[type='text']")

