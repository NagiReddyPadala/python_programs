from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path= "F:\Office\Practice\Selenium\chromedriver_win32\chromedriver.exe")
#driver = webdriver.Firefox(executable_path= "F:\Office\Practice\Selenium\geckodriver-v0.26.0-win64\geckodriver.exe")

#driver = webdriver.Ie(executable_path= "F:\Office\Practice\Selenium\IEDriverServer_Win32_3.150.1\IEDriverServer.exe")


driver.get("http://newtours.demoaut.com/")
#driver.get("http://demo.automationtesting.in/Windows.html")

print(driver.title)  # Title of the page
print(driver.current_url)  # Returns current URL
#print(driver.page_source) # HTML code for the page
usr_ele = driver.find_element_by_name('userName')
print(usr_ele.is_displayed())
print(usr_ele.is_enabled())

pwd_ele = driver.find_element_by_name('password')
print(pwd_ele.is_displayed())
print(pwd_ele.is_enabled())

usr_ele.send_keys("mercury")
pwd_ele.send_keys("mercury")
driver.find_element_by_name('login').click()

time.sleep(5)

rndtrp_ele= driver.find_element_by_css_selector("input[value=roundtrip]")
onetrp_ele= driver.find_element_by_css_selector("input[value=oneway]")

print("Round trip element status: " , rndtrp_ele.is_selected())
print("One trip element status: " , onetrp_ele.is_selected())

driver.close()  # Closes the currently focused browser
driver.quit() # Closes all the browsers