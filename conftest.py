
import pytest


import settings
from selenium import webdriver

@pytest.fixture(scope='function')
def driver():
    firefox_driver = webdriver.Firefox()
    firefox_driver.get(settings.MAIN_PAGE_URL)

    return firefox_driver

