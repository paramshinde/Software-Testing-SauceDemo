from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import pytest
def test_successful_login(driver):
    login_page=LoginPage(driver)
    login_page.login("standard_user","secret_sauce")
    inventory_page=InventoryPage(driver)
    assert inventory_page.is_at()==True
def test_locked_out_login(driver):
    loginpage=LoginPage(driver)
    loginpage.login("locked_out_user",'secret_sauce')
    expected_error="Sorry this user has been locked"
    assert loginpage.get_error_message() in expected_error