import pytest
from selene import browser, have

@pytest.fixture(scope='function', autouse=True)
def browser_setup():
    browser.config.driver_name = 'chrome'

    yield

    browser.quit()