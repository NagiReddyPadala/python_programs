from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="F:\Office\Practice\Selenium\chromedriver_win32\chromedriver.exe")
driver.get("https://www.google.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
search_text_box = driver.find_element_by_name("q")
search_text_box.send_keys("Nagireddy Padala")
search_text_box.send_keys(Keys.ENTER)

# lst_links = driver.find_elements_by_tag_name("h3")
# for link in lst_links:
#     print(link.text)

print(driver.page_source)
#print(driver.)
driver.close()
driver.quit()