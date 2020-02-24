import unittest
from selenium import webdriver

class SearchEngineTest(unittest.TestCase):
    def test_google(self):
        driver = webdriver.Chrome(executable_path="F:\Office\Practice\Selenium\chromedriver_win32\chromedriver.exe")
        driver.get("https://www.google.com/")
        print(driver.title)
        driver.close()


    def test_bing(self):
        driver = webdriver.Chrome(executable_path="F:\Office\Practice\Selenium\chromedriver_win32\chromedriver.exe")
        driver.get("https://bing.com/")
        print(driver.title)
        driver.close()


if __name__ == "__main__":
    unittest.main()
