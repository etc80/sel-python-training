import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
# from __builtin__ import classmethod


class HomePageTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # create a new Firefox session """
        cls.driver = webdriver.Chrome("D:\Progs\Selenium\chromedriver.exe")
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        # navigate to the application home page """
        cls.driver.get("http://www.rozetka.com.ua/")

    def test_search_field(self):
        # check search field exists on Home page
        self.assertTrue(self.is_element_present(By.NAME, "text"))

    def test_language_option(self):
        # check language options dropdown on Home page
        self.assertTrue(self.is_element_present(By.XPATH, ".//*[@id='language-switcher']/span"))

    def test_shopping_cart_empty_message(self):
        # check content of My Shopping Cart block on Home page
        shopping_cart_icon = \
            self.driver.find_element_by_css_selector(".sprite-side.novisited.hub-i-link.hub-i-cart-link")
        shopping_cart_icon.click()
        shopping_cart_status = self.driver.find_element_by_xpath(".//*[@id='drop-block']/h2").text
        self.assertEqual("Корзина пуста", shopping_cart_status)
        close_button = self.driver.find_element_by_xpath(".//*[@id='cart-popup']/a/img")
        close_button.click()

    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.quit()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            print("*** ERROR *** ", e)
            return False
        return True
"""
Utility method to check presence of an element on page
:params how: By locator type
:params what: locator value
"""

if __name__ == '__main__':
    unittest.main()
