from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException

from pages import HomePage

treehouse_rsvp_url = "http://localhost/rsvp/index.html"

driver = webdriver.Chrome()

# driver.get(treehouse_rsvp_url)

invitees = [
    "Harry Potter",
    "Hermione Granger",
    "Ron Weasley",
    "Lord Voldemort",
    "Draco Malfoy",
    "Severus Snape",
    "Albus Dumbledore",
    "Neville Longbottom",
    "Luna Lovegood",
    "Rubeus Hagrid",
    "Ginny Weasley",
    "Minerva McGonagall",
    "Peeves the Rude Ghost",
    "Dobby the House Elf",
    "Moaning Myrtle",
    "Fred Weasley",
    "George Weasley",
    "Nagini the Snake",
    "Nymphadora Lupin",
    "Dudley Dursley",
    "Seamus Finnigan",
    "Oliver Wood"
]


# def add_invitee(name):
#     invite_form = driver.find_element_by_id('registrar')
#     invitee_name_field = driver.find_element_by_css_selector("#registrar input[name='name']")
#     invitee_name_field.send_keys(name)
#     invite_form.submit()

home_page = HomePage(driver, treehouse_rsvp_url)

home_page.open()
# home_page.add_invitee("Teddy")
# home_page.add_invitee("Lala")
# home_page.add_invitee("Pooh")
# # home_page.toggle_non_responders_visibility()

# teddy = home_page.find_invitee_by_name("Teddy")
# print(home_page.get_invitee_count())
# teddy.toggle_confirmation()
# print(teddy.element.get_attribute('class'))
# print(teddy.element.get_attribute('innerHTML'))
# home_page.add_invitee("Twitwi")
# elements = driver.find_elements_by_css_selector("#invitedList li")
# print("Number of elements: {}".format(len(elements)))

names = ["Mr. Wonka", "Milka", "Dolly", "Kenny"]

for name in names:
    home_page.add_invitee(name)

kenny = home_page.find_invitee_by_name(names[3])
kenny.remove()

invitee_count = home_page.get_invitee_count()
print("invitee_count: {}, names_length: {}".format(invitee_count, len(names)))


# driver.find_element_by_css_selector('#invitedList > li:nth-child(3) > label > input[type="checkbox"]').click()



# home_page.add_invitee("Tinky Winky")

# home_page.toggle_non_responders_visibility()
# teddy = home_page.find_invitee_by_name("Teddy")
# teddy.toggle_confirmation()
# home_page.toggle_non_responders_visibility()
# print(teddy.element.get_attribute('innerHTML'))
# hello = teddy.element.is_displayed()
# print(hello)
# teddy.rename("Teddy Biddie")

# lala = home_page.find_invitee_by_name("Lala")
# lala.toggle_confirmation()
# home_page.toggle_non_responders_visibility()
# lala.remove()



# add_invitee("AC")
# add_invitee("Teddy")
# add_invitee("Mama")
# add_invitee("Papa")
# driver.close()