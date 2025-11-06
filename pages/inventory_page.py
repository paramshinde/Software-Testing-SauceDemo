from selenium.webdriver.common.by import By
class InventoryPage:
    HeaderTitle=(By.CLASS_NAME,'title')
    def __init__(self,driver):
        self.driver=driver
    def is_at(self):
        return self.driver.find_element(*self.HeaderTitle).text=='Products'