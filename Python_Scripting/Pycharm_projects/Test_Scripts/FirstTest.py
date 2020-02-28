from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import HtmlTestRunner
#import time

class GoogleSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Test started")
        cls.driver = webdriver.Chrome("E:\Promethean\Python_Scripting\Pycharm_projects\Drivers\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    def testSearchPython(self):
        self.driver.get("https://www.google.com/")
        self.driver.find_element_by_name("q").send_keys("Python")
        self.driver.find_element_by_name("q").send_keys(Keys.ENTER)
        #time.sleep(4)

    def testSearchPythonUnitTest(self):
        self.driver.get("https://www.google.com/")
        self.driver.find_element_by_name("q").send_keys("Python unit test")
        self.driver.find_element_by_name("q").send_keys(Keys.ENTER)
        #time.sleep(4)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="E:\Promethean\Python_Scripting\Pycharm_projects\Reports"))