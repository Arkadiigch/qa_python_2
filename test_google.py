import pytest
from selene import browser, be, have
from selenium import webdriver

@pytest.fixture
def browser_size():
    browser.config.window_height = 600
    browser.config.window_width = 600

def test_serch(browser_size):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('йфывфывфывфывфывфывфыв').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))