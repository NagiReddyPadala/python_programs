from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="F:\Office\Practice\Selenium\chromedriver_win32\chromedriver.exe")

driver.get("https://selenium.dev/selenium/docs/api/java/index.html?deprecated-list.html")
driver.switch_to.frame("packageListFrame")
driver.find_element_by_link_text("com.thoughtworks.selenium").click()
time.sleep(3)
driver.switch_to.default_content()

driver.switch_to.frame("packageFrame")
driver.find_element_by_link_text("Selenium").click()
time.sleep(3)

driver.switch_to.default_content()

driver.find_element_by_link_text("Deprecated").click()
time.sleep(3)

driver.close()