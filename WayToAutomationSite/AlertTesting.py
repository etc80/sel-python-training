from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import gmtime, strftime
import unittest


class RegisterNewUser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("D:\Progs\Selenium\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("http://www.way2automation.com/demo.html")

    def testAlerts(self):
        driver = self.driver
        driver.find_element_by_link_text("Alert").click()
        for handle in driver.window_handles:
            driver.switch_to.window(handle)
        driver.find_element_by_link_text("Signin").click()
        user_names = driver.find_elements_by_name("username")
        user_names[1].send_keys("test")
        passwords = driver.find_elements_by_name("password")
        passwords[1].send_keys("test")
        submit_buttons = driver.find_elements_by_class_name("button")
        submit_buttons[1].submit()
        print("*** logged successfully! ***")

        driver.refresh()
        driver.find_element_by_link_text("Alert").click()
        # check confirmation alert
        simple_alert = driver.find_element_by_xpath(".//*[@id='wrapper']/div/div[1]/div[1]/ul/li[1]/a")
        simple_alert.click()
        driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
        alert_button = driver.find_element_by_tag_name("button")
        alert_button.click()
        alert = driver.switch_to.alert
        alert_text = alert.text
        print('*** ' + alert_text + " ***")
        alert.accept()
        driver.switch_to.default_content()

        # check input alert
        driver.refresh()
        simple_alert = driver.find_element_by_xpath(".//*[@id='wrapper']/div/div[1]/div[1]/ul/li[2]/a")
        simple_alert.click()
        driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[1])
        print("*** " + driver.find_element_by_id("demo").text + " ***")
        driver.find_element_by_tag_name("button").click()
        alert = driver.switch_to.alert
        alert_text = alert.text
        print('*** ' + alert_text + " ***")
        alert.send_keys("Test User")
        alert.accept()
        print(driver.find_element_by_id("demo").text)
        driver.switch_to.default_content()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)