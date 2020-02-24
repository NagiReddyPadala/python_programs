from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path= "F:\Office\Practice\Selenium\chromedriver_win32\chromedriver.exe")
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

driver.switch_to.frame(0)
driver.find_element_by_id("RESULT_FileUpload-10").send_keys("C://Users//NAGIREDDY P//Desktop//sample.txt")

time.sleep(10)

driver.close()