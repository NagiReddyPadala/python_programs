from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="F:\Office\Practice\Selenium\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.facebook.com/")

user_name_input = driver.find_element_by_id("email")
password_input = driver.find_element_by_id("pass")
login_button = driver.find_element_by_xpath("//input[@value='Log In']")

user_name_input.send_keys("nagi369")
password_input.send_keys("999591755777")
login_button.click()

time.sleep(10)

#friend_request_button = driver.find_element_by_xpath('//*[@id="js_48"]/div')
#friend_request_button.click()

# friend_request_layout = driver.find_element_by_id("fbRequestsFlyout")
# friend_request_layout.
# ui_list = driver.find_element_by_xpath('//*[@id="u_15_1"]/div/div/div[4]/ul')
#
# ui_list.
#

options_button = driver.find_element_by_id("userNavigationLabel")
options_button.click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="js_y"]/div/div/ul/li[9]/a/span/span').click()