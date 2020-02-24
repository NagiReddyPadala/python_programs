from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path= "F:\Office\Practice\Selenium\chromedriver_win32\chromedriver.exe")
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()
capital = driver.find_element_by_id("box6")
country = driver.find_element_by_id("box106")
actions = ActionChains(driver)
actions.drag_and_drop(capital, country).perform()
time.sleep(5)
driver.close()


driver = webdriver.Chrome(executable_path= "F:\Office\Practice\Selenium\chromedriver_win32\chromedriver.exe")
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()
element = driver.find_element_by_xpath('/html/body/div/section/div/div/div/p/span')
actions = ActionChains(driver)
actions.context_click(element).perform()
time.sleep(5)
driver.close()



driver = webdriver.Chrome(executable_path= "F:\Office\Practice\Selenium\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")

driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()

time.sleep(5)
admin = driver.find_element_by_id("menu_admin_viewAdminModule")
userMngmt = driver.find_element_by_id("menu_admin_UserManagement")
users = driver.find_element_by_id("menu_admin_viewSystemUsers")

#Mousehover actions
actions = ActionChains(driver)
actions.move_to_element(admin).move_to_element(userMngmt).move_to_element(users).click().perform()
time.sleep(5)

driver.close()




driver = webdriver.Chrome(executable_path= "F:\Office\Practice\Selenium\chromedriver_win32\chromedriver.exe")
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
element = driver.find_element_by_xpath('//*[@id="HTML10"]/div[1]/button')
actions = ActionChains(driver)
actions.double_click(element).perform()
time.sleep(5)
driver.close()
