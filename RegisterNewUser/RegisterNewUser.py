from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import gmtime, strftime
import unittest


class RegisterNewUser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("D:\Progs\Selenium\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("http://www.demoqa.com")

    def test_register_new_user(self):
        driver = self.driver
        # get the Create Account button
        create_account_button = driver.find_element_by_id("menu-item-374")
        # check Create Account button is displayed and enabled
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        # click on Create Account button. This will display new account
        create_account_button.click()
        # check title
        self.assertEquals("Registration | Demoqa", driver.title)
        # get all the fields from Create an Account form
        first_name = driver.find_element_by_id("name_3_firstname")
        last_name = driver.find_element_by_id("name_3_lastname")
        email_address = driver.find_element_by_id("email_1")
        phone_number = driver.find_element_by_id("phone_9")
        username = driver.find_element_by_id("username")
        about_yourself = driver.find_element_by_id("description")
        marital_status = driver.find_elements_by_name("radio_4[]")
        hobby = driver.find_elements_by_name("checkbox_5[]")
        # news_letter_subscription = driver.find_element_by_id("is_subscribed")
        country = Select(driver.find_element_by_id("dropdown_7"))
        birth_month = Select(driver.find_element_by_id("mm_date_8"))
        birth_day = Select(driver.find_element_by_id("dd_date_8"))
        birth_year = Select(driver.find_element_by_id("yy_date_8"))

        password = driver.find_element_by_id("password_2")
        confirm_password = driver.find_element_by_id("confirm_password_password_2")
        submit_button = driver.find_element_by_name("pie_submit")

        # check rows and columns of description
        self.assertEqual("5", about_yourself.get_attribute("rows"))
        self.assertEqual("80", about_yourself.get_attribute("cols"))

        # check all fields are enabled
        self.assertTrue(first_name.is_enabled() and last_name.is_enabled() and email_address.is_enabled() and password.is_enabled() and confirm_password.is_enabled() and submit_button.is_enabled())

        # check Sign Up for Newsletter is unchecked
        # self.assertFalse(news_letter_subscription.is_selected())

        user_name = "user_" + strftime("%Y%m%d%H%M%S", gmtime())
        # fill out all the fields
        first_name.send_keys("Test")
        last_name.send_keys("Test")
        username.send_keys(user_name)
        email_address.send_keys(user_name + "@example.com")
        phone_number.send_keys("380505551234")
        about_yourself.send_keys("This is test user from selenium + python practice")
        marital_status[0].click()
        hobby[0].click()
        country.select_by_visible_text("Ukraine")
        birth_month.select_by_visible_text("10")
        birth_day.select_by_visible_text("28")
        birth_year.select_by_visible_text("1983")
        password.send_keys("TestTempP@$$w0rd1!")
        confirm_password.send_keys("TestTempP@$$w0rd1!")

        # click Submit button to submit the form
        submit_button.click()

        # check new user is registered
        self.assertEqual("Thank you for your registration", driver.find_element_by_class_name("piereg_message").text)
        # self.assertTrue(driver.find_element_by_link_text("Log Out").is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
