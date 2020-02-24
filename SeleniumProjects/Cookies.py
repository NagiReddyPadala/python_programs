from selenium import webdriver

driver = webdriver.Chrome(executable_path= "F:\Office\Practice\Selenium\chromedriver_win32\chromedriver.exe")

driver.get("https://www.amazon.in/")

#Capture all the cookies created by browser
cookies = driver.get_cookies()
print(len(cookies))

for cookie in cookies:
    print(cookie)

cookie = {'name': "MyCookie", 'value': '123456789'}
driver.add_cookie(cookie)

cookies = driver.get_cookies()
print(len(cookies))

for cookie in cookies:
    print(cookie)

driver.delete_cookie('MyCookie')
#driver.delete_all_cookies()

cookies = driver.get_cookies()
print(len(cookies))

for cookie in cookies:
    print(cookie)


driver.close()