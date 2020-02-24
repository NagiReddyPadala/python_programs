import unittest

class LoginTest(unittest.TestCase):
    def test_LoginUsingGoogle(self):
        print("login using Google")

    def test_LoginUsingFacebook(self):
        print("login using Facebook")

if __name__ == "__main__":
    unittest.main()