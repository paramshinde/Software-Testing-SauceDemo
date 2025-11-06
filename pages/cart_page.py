from selenium.webdriver.common.by import By
class CartPage:
    Cart_Item_Name=(By.CLASS_NAME,'inventory_item_name')
    Checkout_Button=(By.ID,'checkout')
    def __init__(self,driver):
        self.driver=driver
    def get_item_name(self):
        try:
            return self.driver.find_element(*self.Cart_Item_Name).text
        except:
            return None
    