from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ES

import time

driver = webdriver.Chrome(executable_path= "F:\Office\Practice\Selenium\chromedriver_win32\chromedriver.exe")
driver.maximize_window()

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")


element = driver.find_element_by_id("RESULT_RadioButton-9")
drp = Select(element)

#Select by visible text
drp.select_by_visible_text('Morning')
time.sleep(3)

#Selecy by index
drp.select_by_index(2)
time.sleep(3)

#Select by Value
drp.select_by_value("Radio-2")
time.sleep(3)

count = len(drp.options)
print("No.of options are: ", count)

options = drp.options
print("Options are: ")
for option in options:
    print(option.text)

driver.close()
driver.quit()