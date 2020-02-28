import unittest

class test(unittest.TestCase):
    @unittest.skip
    def test_sample(self):
        print("Sample test")



if __name__ == "__main__":
    unittest.main()