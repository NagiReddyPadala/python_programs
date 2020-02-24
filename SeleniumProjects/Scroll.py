from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path= "F:\Office\Practice\Selenium\chromedriver_win32\chromedriver.exe")
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()

#Scrolldown by pixel
driver.execute_script("window.scrollBy(0, 1000)", "")
time.sleep(5)

#scrolldown till element
indFlag = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[2]/table[1]/tbody/tr[86]/td[1]/img')
driver.execute_script("arguments[0].scrollIntoView()", indFlag)
time.sleep(5)

#Scroll till end of the page
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
time.sleep(5)

driver.close()