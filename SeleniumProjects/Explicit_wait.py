from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path= "F:\Office\Practice\Selenium\chromedriver_win32\chromedriver.exe")

driver.maximize_window()
driver.get("https://www.expedia.com/")

driver.find_element_by_id("tab-flight-tab-hp").click()


driver.find_element_by_id("flight-origin-hp-flight").send_keys("SFO") #Origin
time.sleep(2)
driver.find_element_by_id("flight-destination-hp-flight").send_keys("NYC") #Destination

driver.find_element_by_id("flight-departing-hp-flight").clear()
driver.find_element_by_id("flight-departing-hp-flight").send_keys("01/31/2020") #Depart date

driver.find_element_by_id("flight-returning-hp-flight").clear()
driver.find_element_by_id("flight-returning-hp-flight").send_keys("02/22/2020") #Return date

driver.find_element_by_xpath("//*[@id='gcw-flights-form-hp-flight']/div[7]/label/button").click()

wait = WebDriverWait(driver, 10)

element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='stopFilter_stops-0']")))
element.click()
time.sleep(3)

driver.close()
driver.quit()





