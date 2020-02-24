import pytest


@pytest.yield_fixture()
def setup():
    print("Open URL to login")
    yield
    print("Close browser")


def test_SignupByMail(setup):
    print("This is signup by mail test")


def test_SignupByFacebook(setup):
    print("This is signup by facebook test")

