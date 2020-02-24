from SeleniumProjects import ExcelUtils
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ES

import time

driver = webdriver.Chrome(executable_path= "F:\Office\Practice\Selenium\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
driver.get("http://newtours.demoaut.com/")

path = "F:\Office\Practice\PycharmProjects\SeleniumProjects\login.xlsx"
rows = ExcelUtils.getRowCount(path, 'Sheet1')
for r in range(2, rows+1):
    username = ExcelUtils.readData(path, 'Sheet1', r, 1)
    password = ExcelUtils.readData(path, 'Sheet1', r, 2)

    driver.find_element_by_name("userName").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("login").click()

    if driver.title == "Find a Flight: Mercury Tours:":
        print("Login successful")
        ExcelUtils.writeData(path, 'Sheet1', r, 3, "Login successful")
    else:
        print("Login failed")
        ExcelUtils.writeData(path, 'Sheet1', r, 3, "Login failed")

    driver.find_element_by_link_text("Home").click()