from selenium.webdriver.common.by import By
class InventoryPage:
    HeaderTitle=(By.CLASS_NAME,'title')
    Add_To_Cart_Sauce_Labs_Backpack=(By.ID,"add-to-cart-sauce-labs-backpack")
    Shopping_Cart_Link=(By.CLASS_NAME,'shopping_cart_link')
    def __init__(self,driver):
        self.driver=driver
    def is_at(self):
        return self.driver.find_element(*self.HeaderTitle).text=='Products'
    def add_backpack_to_cart(self):
        self.driver.find_element(*self.Add_To_Cart_Sauce_Labs_Backpack).click()
    def go_to_cart(self):
        self.driver.find_element(*self.Shopping_Cart_Link).click()    