from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path= "F:\Office\Practice\Selenium\chromedriver_win32\chromedriver.exe")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

# How to find how many input boxes present in Web page

inputBoxes = driver.find_elements(By.CLASS_NAME, 'text_field')
print("Number of input boxes are: ", len(inputBoxes))

# Display the status
displayStatus = driver.find_element(By.ID, "RESULT_TextField-1").is_displayed()
enableStatus = driver.find_element(By.ID, "RESULT_TextField-1").is_enabled()

print("Display status: ", displayStatus)
print("Enable status: ", enableStatus)

#How to provide values to Input field
driver.find_element(By.ID, "RESULT_TextField-1").send_keys("Nagireddy")
driver.find_element(By.ID, "RESULT_TextField-2").send_keys("Padala")
#driver.find_element_by_id("RESULT_TextField-2").send_keys("Padala")

