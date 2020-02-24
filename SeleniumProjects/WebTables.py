from selenium import webdriver

driver = webdriver.Chrome(executable_path= "F:\Office\Practice\Selenium\chromedriver_win32\chromedriver.exe")
driver.get("file:///F:/Office/Practice/PycharmProjects/SeleniumProjects/SampleTable.html")

rows = len(driver.find_elements_by_xpath("/html/body/table/tbody/tr"))
cols = len(driver.find_elements_by_xpath("/html/body/table/tbody/tr[1]/th"))

print("Rows, Columns: ", rows, cols)

for r in range(2, rows+1):
    for c in range(1, cols+1):
        val = driver.find_element_by_xpath("/html/body/table/tbody/tr[" + str(r) + "]/td[" + str(c) + "]").text
        print(val, end= "    ")
    print()


driver.close()

