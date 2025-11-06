from selenium.webdriver.common.by import By
class CheckOutPage:
    First_Name=(By.ID,'first-name')
    Last_Name=(By.ID,'last-name')
    Postal_Code=(By.ID,'postal-code')
    Countinue_Button=(By.ID,'continue')
    Finish_Button=(By.ID,'finish')
    
    def __init__(self,driver):
        self.driver=driver
        
    def fill_checkout_form(self,First_Name,Last_Name,Postal_Code):
        self.driver.find_element(*self.First_Name).send_keys(First_Name)
        self.driver.find_element(*self.Last_Name).send_keys(Last_Name)
        self.driver.find_element(*self.Postal_Code).send_keys(Postal_Code)
        self.driver.find_element(*self.Countinue_Button).click()
    
    def click_finish(self):
        self.driver.find_element(*self.Finish_Button).click()
            