import pytest
import pytest_html
#@pytest.fixture()
@pytest.yield_fixture()
def setup():
    print("Once before every method")
    yield
    print("Once after every method")

def testMedthod1(setup):
    print("This is test method1")


def testMedthod2():
    print("This is test method2")

#Execution by folder : pytest -v -s F:\Office\Practice\PycharmProjects\PyTest
#Execution by module : pytest -v -s test_Login.py
#Exectution by test case: pytest -v -s test_Login.py::test_loginByMail
#Html report pytest -v -s --html=report.html F:\Office\Practice\PycharmProjects\PyTest
# Need to install pytest_html
#Html report pytest -v -s --html=report.html --self-contained-html F:\Office\Practice\PycharmProjects\PyTest