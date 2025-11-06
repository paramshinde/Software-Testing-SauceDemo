import pytest
from selenium import webdriver
@pytest.fixture(scope="function")
def driver():
    driver=webdriver.Edge()
    driver.implicitly_wait(10)
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()