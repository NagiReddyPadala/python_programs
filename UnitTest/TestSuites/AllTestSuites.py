from UnitTest.Login.TC_LoginTest import LoginTest
from UnitTest.Login.TC_SignUpTest import SignUpTest

from UnitTest.Payment.TC_PaymentTest import PaymentTest
from UnitTest.Payment.TC_PaymentReturn import PaymentReturnTest
import unittest
import HtmlTestRunner

tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SignUpTest)

tc3 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnTest)

loginSignupTestSuite = unittest.TestSuite([tc1, tc2])
paymentTestSuite = unittest.TestSuite([tc3, tc4])
masterTestSuite = unittest.TestSuite([tc1, tc2, tc3, tc4])


if __name__ == "__main__":
    res = unittest.TextTestRunner().run(loginSignupTestSuite)
    #res = unittest.TextTestRunner().run(paymentTestSuite)
    #res = unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner()).runTests()
    #unittest.TextTestRunner(verbosity=2).run(masterTestSuite)

    print(res)