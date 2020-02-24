from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

chromeOptions1 = Options()
chromeOptions1.add_experimental_option("prefs", {"download.default_directory": "F:\\"})

driver = webdriver.Chrome(executable_path= "F:\Office\Practice\Selenium\chromedriver_win32\chromedriver.exe", options = chromeOptions1)
print(type(driver))
driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()

driver.find_element_by_id("textbox").send_keys("Download test")
driver.find_element_by_id("createTxt").click()
driver.find_element_by_id("link-to-download").click()

time.sleep(10)

driver.close()
