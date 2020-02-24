import unittest

def setUpModule():
    print("Setup module")

def tearDownModule():
    print("Teardown module")

class TestingWithUnitTest(unittest.TestCase):
    def test_Hi(self):
        print("Hi")

    @unittest.SkipTest
    def test_Hello(self):
        print("Hello")

    @unittest.skip("This is not yet ready")
    def test_How(self):
        print("How")

    @unittest.skipIf(1 == 1, "Skip if testing")
    def test_Are(self):
        print("Are")

    @unittest.skipUnless(1 == 1, "Skip if testing")
    def test_You(self):
        print("You")

    def test1_one(self):
        print("1")

    def test2_two(self):
        print("2")

    def test3_three(self):
        print("3")

    @classmethod
    def setUp(self):
        print("Setup")

    @classmethod
    def tearDown(self):
        print("Teardown")

    @classmethod
    def setUpClass(cls):
        print("Setup class")
        print("Open application")

    @classmethod
    def tearDownClass(cls):
        print("Teardown class")
        print("Close application")

if __name__ == "__main__":
    unittest.main()
