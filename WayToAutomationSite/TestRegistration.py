from selenium import webdriver
import unittest


class RegisterNewUser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("D:\Progs\Selenium\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("http://www.way2automation.com/demo.html")

    def testLogin(self):
        driver = self.driver
        driver.find_element_by_link_text("Alert").click()
        for handle in driver.window_handles:
            driver.switch_to.window(handle)
        # driver.switch_to.window('Welcome to the Test Site')
        # driver.find_element_by_link_text("Signin").click()
        driver.find_element_by_name("name").send_keys("test")
        driver.find_element_by_name("phone").send_keys("380505551212")
        driver.find_element_by_name("email").send_keys("test@newtest.com")
        driver.find_element_by_name("city").send_keys("Testcity")
        user_names = driver.find_elements_by_name("username")
        print(user_names)
        print(len(user_names))
        user_names[1].send_keys("test")
        passwords = driver.find_elements_by_name("password")
        print(passwords)
        print(len(passwords))
        passwords[1].send_keys("test")
        submit_buttons = driver.find_elements_by_class_name("button")
        print(submit_buttons)
        print(len(submit_buttons))
        submit_buttons[1].click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)