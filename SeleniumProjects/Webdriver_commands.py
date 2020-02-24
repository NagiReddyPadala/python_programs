from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path= "F:\Office\Practice\Selenium\chromedriver_win32\chromedriver.exe")
#driver = webdriver.Firefox(executable_path= "F:\Office\Practice\Selenium\geckodriver-v0.26.0-win64\geckodriver.exe")

#driver = webdriver.Ie(executable_path= "F:\Office\Practice\Selenium\IEDriverServer_Win32_3.150.1\IEDriverServer.exe")


#driver.get("http://newtours.demoaut.com/")
driver.get("http://demo.automationtesting.in/Windows.html")

print(driver.title)  # Title of the page
print(driver.current_url)  # Returns current URL
#print(driver.page_source) # HTML code for the page
driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()
time.sleep(5)

driver.close()  # Closes the currently focused browser
driver.quit() # Closes all the browsers