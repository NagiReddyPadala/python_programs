import unittest


class SignUpTest(unittest.TestCase):
    def test_SignUpUsingGoogle(self):
        print("SignUp using Google")

    def test_SignUpUsingFacebook(self):
        print("SignUp using Facebook")
        self.assertEqual(11,10)

if __name__ == "__main__":
    unittest.main()