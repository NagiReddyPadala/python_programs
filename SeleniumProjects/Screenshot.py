from selenium import webdriver

driver = webdriver.Chrome(executable_path= "F:\Office\Practice\Selenium\chromedriver_win32\chromedriver.exe")
driver.maximize_window()

driver.get("http://newtours.demoaut.com/")

driver.save_screenshot("F:\Office\Practice\PycharmProjects\SeleniumProjects\ScnshtFrmSelenium.png")

driver.get_screenshot_as_file("F:\Office\Practice\PycharmProjects\SeleniumProjects\ScnshtFrmSelenium1.jpg")

driver.close()