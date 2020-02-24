from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ES
import time

driver = webdriver.Chrome(executable_path= "F:\Office\Practice\Selenium\chromedriver_win32\chromedriver.exe")
driver.maximize_window()

driver.get("http://newtours.demoaut.com/")

links = driver.find_elements(By.TAG_NAME,"a")
print("No.of links present in page: ", len(links))

print("Links are: ")
for link in links:
    print(link.text)

#Click on link
driver.find_element(By.LINK_TEXT, "REGISTER").click()
#driver.find_element(By.PARTIAL_LINK_TEXT, "REG").click()

time.sleep(5)
driver.close()