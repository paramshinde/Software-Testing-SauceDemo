from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
import pytest
def test_add_item_to_cart(driver):
    #Login
    login_page=LoginPage(driver)
    login_page.login("standard_user",'secret_sauce')
    #Add item from inventory page
    inventorypage=InventoryPage(driver)
    assert inventorypage.is_at()
    inventorypage.add_backpack_to_cart()
    inventorypage.go_to_cart()
    #Verify Item in cart
    cart_page=CartPage(driver)
    item_name=cart_page.get_item_name()
    assert item_name=="Sauce Labs Backpack"
    