import pytest

@pytest.yield_fixture()
def setup():
    print("Open URL to login")
    yield
    print("Close browser")

def test_loginByMail(setup):
    print("This is login by mail test")

def test_loginByFacebook(setup):
    print("This is login by facebook test")

