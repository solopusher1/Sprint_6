import pytest
from selenium import webdriver
from urls import URL


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    driver.get(URL.MAIN_PAGE)
    yield driver
    driver.quit()