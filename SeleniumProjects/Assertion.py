import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testTitle(self):
        driver = webdriver.Chrome(executable_path="F:\Office\Practice\Selenium\chromedriver_win32\chromedriver.exe")
        driver.get("http://newtours.demoaut.com/")

        self.assertIsNotNone(driver)
        #self.assertIsNone(driver)

        self.assertEqual(driver.title, "Welcome: Mercury Tours", "Title not same")
        #self.assertNotEqual(driver.title, "Welcome: Mercury Tour", "Title same")

        self.assertTrue(driver.title == "Welcome: Mercury Tours")
        #self.assertFalse(driver.title == "Welcome: Mercury Tours")

        lst = ["python", "selenium", "js"]
        self.assertIn("python", lst)
        #self.assertNotIn("pearl", lst)

        self.assertGreater(101, 100) #first number should be greater than 2nd
        self.assertGreaterEqual(100, 100)

        self.assertLess(10, 11)
        self.assertLessEqual(11, 11)


if __name__ == "__main__":
    unittest.main()