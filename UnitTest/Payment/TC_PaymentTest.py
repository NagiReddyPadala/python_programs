import unittest

class PaymentTest(unittest.TestCase):
    def test_paymentFromNetBanking(self):
        print("Payment from net banking")

    def test_paymentFromCard(self):
        print("Payment from card")


if __name__ == "__main__":
    unittest.main()