from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path= "F:\Office\Practice\Selenium\chromedriver_win32\chromedriver.exe")

driver.get("http://newtours.demoaut.com/")
#driver.navigate("http://newtours.demoaut.com/")

print(driver.title)  # Title of the page
#print(driver.current_url)  # Returns current URL


driver.get("http://pavantestingtools.blogspot.in/")
print(driver.title)  # Title of the page
#print(driver.current_url)  # Returns current URL

driver.back()
print(driver.title)  # Title of the page
driver.forward()

print(driver.title)  # Title of the page
driver.refresh()

driver.close()  # Closes the currently focused browser
driver.quit() # Closes all the browsers