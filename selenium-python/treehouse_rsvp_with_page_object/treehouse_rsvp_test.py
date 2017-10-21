import unittest
from selenium import webdriver

from pages import HomePage, Invitee

class TreehouseRSVPTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost/rsvp/index.html")
        self.home_page = HomePage(self.driver)


    def test_home_add_invitee(self):
        name = "Anne"
        self.home_page.add_invitee(name)
        invitee = self.home_page.find_invitee_by_name(name)
        self.assertIn(f"<span>{name}</span>", invitee.element.get_attribute('innerHTML'))

    def test_home_hide_non_responders_after_add(self):
        name = "Teddy"
        self.home_page.add_invitee(name)
        invitee = self.home_page.find_invitee_by_name(name)
        invitee.toggle_confirmation()
        self.home_page.toggle_non_responders_visibility()
        self.assertTrue(invitee.element.is_displayed())

    def test_home_hide_non_responders_before_add(self):
        name_1 = "Ozzy"
        self.home_page.add_invitee(name_1)
        invitee_1 = self.home_page.find_invitee_by_name(name_1)
        self.home_page.toggle_non_responders_visibility()
        #add another invitee after toggled non-responders visibility checkbox
        name_2 = "Bubbles"
        self.home_page.add_invitee(name_2)
        invitee_2 = self.home_page.find_invitee_by_name(name_2)
        self.assertFalse(invitee_2.element.is_displayed()) #Here come's the bug. Yay! Joy of testers.

    def test_invitee_confirm(self):
        name = "Huckleberry Finn"
        self.home_page.add_invitee(name)
        invitee =self.home_page.find_invitee_by_name(name)
        invitee.toggle_confirmation()
        self.assertEqual("responded", invitee.element.get_attribute('class'))
        
    def test_invitee_rename(self):
        wrong_name = "Tmiber"
        correct_name = "Timber"
        self.home_page.add_invitee(wrong_name)
        invitee =self.home_page.find_invitee_by_name(wrong_name)
        invitee.rename(correct_name)
        self.assertIn(f"<span>{correct_name}</span>", invitee.element.get_attribute('innerHTML'))

    def test_invitee_remove(self):
        names = ["Mr. Wonka", "Milka", "Dolly", "Kenny"]
        for name in names:
            self.home_page.add_invitee(name)
        kenny = self.home_page.find_invitee_by_name(names[3])
        kenny.remove()
        invitee_count = self.home_page.get_invitee_count()
        self.assertEqual(invitee_count, len(names)-1)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()