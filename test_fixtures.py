import pytest

@pytest.fixture
def browser():
    pass

@pytest.fixture
def login_page(browser):
    pass

@pytest.fixture
def credentials():
    return "admin", "12345"
def test_login(login_page, credentials):
    assert credentials == ("admin", "12345")