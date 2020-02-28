from selenium import webdriver
import unittest
import HtmlTestRunner
# import sys
# import os
# sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
from POM_Project_Demo.Pages.loginPage import LoginPage
from POM_Project_Demo.Pages.homePage import HomePage
#from selenium.webdriver.common.keys import Keys
import time

class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="E:\Promethean\Python_Scripting\Pycharm_projects\Drivers\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    def test_01_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_loggin()

        homepage = HomePage(driver)
        homepage.click_welcome()
        time.sleep(4)
        homepage.click_logout()

        """
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        self.driver.find_element_by_id("welcome").click()
        time.sleep(2)
        self.driver.find_element_by_link_text("Logout").click()
        """

    def test_02_login_invalid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin1")
        login.enter_password("admin123")
        login.click_loggin()
        message = login.check_invalid_username_message()
        self.assertEqual(message, "Invalid credentials")


    @classmethod
    def tearDownClass(cls):
        time.sleep(4)
        cls.driver.close()
        cls.driver.quit()
        print("Test complete")

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="E:\Promethean\Python_Scripting\Pycharm_projects\Reports"))