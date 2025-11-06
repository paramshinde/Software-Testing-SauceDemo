from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckOutPage
from pages.checkout_complete_page import CheckOutCompletePage
import pytest
def test_successful_checkout(driver):
    #Login
    login_page=LoginPage(driver)
    login_page.login("standard_user","secret_sauce")
    #add item to cart
    inventorypage=InventoryPage(driver)
    inventorypage.add_backpack_to_cart()
    inventorypage.go_to_cart()
    #go to checkout
    cartpage=CartPage(driver)
    cartpage.click_checkout()
    #fill checkout form and finish
    checkout_page=CheckOutPage(driver)
    checkout_page.fill_checkout_form("Testing","User123","54321")
    checkout_page.click_finish()
    #verify successfull checkout
    checkout_complete_page=CheckOutCompletePage(driver)
    message=checkout_complete_page.get_complete_message()
    assert message =="Thank you for your order!"