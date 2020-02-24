from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ES
import time

driver = webdriver.Chrome(executable_path= "F:\Office\Practice\Selenium\chromedriver_win32\chromedriver.exe")
driver.maximize_window()

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

#Working with the Radio button
mRadioButtonStatus = driver.find_element(By.ID, "RESULT_RadioButton-7_0").is_selected()
print("Male radio button status: ", mRadioButtonStatus)

fRadioButtonStatus = driver.find_element(By.ID, "RESULT_RadioButton-7_1").is_selected()
print("Female radio button status: ", fRadioButtonStatus)

time.sleep(5)

sundayCheckBoxStatus = driver.find_element_by_id("RESULT_CheckBox-8_0").is_selected()
print("Monday checked ? ", sundayCheckBoxStatus)

mondayCheckBoxStatus = driver.find_element_by_id("RESULT_CheckBox-8_1").is_selected()
print("Monday checked ? ", mondayCheckBoxStatus)

time.sleep(5)
mRadioButtonStatus = driver.find_element_by_id("RESULT_RadioButton-7_0").click()
print("Male radio button status: ", mRadioButtonStatus)

