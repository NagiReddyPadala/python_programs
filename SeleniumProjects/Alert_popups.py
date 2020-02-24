from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="F:\Office\Practice\Selenium\chromedriver_win32\chromedriver.exe")

res = driver.get("https://testautomationpractice.blogspot.com/")

print(res)

driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()

time.sleep(5)

#driver.switch_to_alert.accept()
driver.switch_to.alert.accept()
#driver.switch_to.alert.dismiss()

driver.close()
