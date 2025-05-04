import pytest
from selenium import webdriver

from data import URLS

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    driver.get(URLS.MAIN_PAGE)
    yield driver
    driver.quit()
