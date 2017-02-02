import unittest
from selenium import webdriver


class SearchTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # create a new session
        cls.driver = webdriver.Chrome("D:\Progs\Selenium\chromedriver.exe")
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        # navigate to the application home page
        cls.driver.get("http://demo.magentocommerce.com/")

    def setUp(self):
        print("Test Starts")
        # create a new Chrome session
        # self.driver = webdriver.Chrome("D:\Progs\Selenium\chromedriver.exe")
        # self.driver.implicitly_wait(30)
        # self.driver.maximize_window()
        # navigate to the application home page
        # self.driver.get("http://demo.magentocommerce.com/")

    def test_search_by_category(self):
        self.driver.find_element_by_xpath('//*[@id="nav-main"]/div/div[2]/div[1]/a[2]/i').click()
        # get the search textbox
        search_field = self.driver.find_element_by_name("keys")
        # search_field.clear()
        # enter search keyword and submit
        search_field.send_keys("phones")
        search_field.submit()
        # get all the anchor elements which have product names displayed
        # currently on result page using find_elements_by_xpath method
        products = self.driver.find_elements_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/ul/li/div[1]/a')
        self.assertEqual(20, len(products))

    def test_search_by_name(self):
        self.driver.find_element_by_xpath('//*[@id="nav-main"]/div/div[2]/div[1]/a[2]/i').click()
        # get the search textbox
        search_field = self.driver.find_element_by_name("keys")
        # search_field.clear()
        # enter search keyword and submit
        search_field.send_keys("salt shaker")
        search_field.submit()
        # get all the anchor elements which have product names displayed
        # currently on result page using find_elements_by_xpath method
        products = self.driver.find_elements_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/ul/li/div[1]/a')
        self.assertEqual(0, len(products))

    def tearDown(self):
        # close the browser window
        print("Test Ends!")
        # self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()

