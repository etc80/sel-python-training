from selenium import webdriver

print("Hello from Python!")

driver = webdriver.Chrome("D:\Progs\Selenium\chromedriver.exe")
driver.implicitly_wait(30)
driver.maximize_window()
# navigate to the application home page
driver.get("http://demo.magentocommerce.com/")
driver.find_element_by_xpath('//*[@id="nav-main"]/div/div[2]/div[1]/a[2]/i').click()
# get the search textbox
search_field = driver.find_element_by_name("keys")
# search_field.clear()
# enter search keyword and submit
search_field.send_keys("phones")
search_field.submit()
# get all the anchor elements which have product names displayed
# currently on result page using find_elements_by_xpath method
products = driver.find_elements_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/ul/li/div[1]/a')
# get the number of anchor elements found
print("Found " + str(len(products)) + " products:")
# iterate through each anchor element and print the text that is
# name of the product
for product in products:
    print(product.text)
# close the browser window
driver.quit()
