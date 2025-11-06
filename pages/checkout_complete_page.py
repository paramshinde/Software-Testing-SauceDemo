from selenium.webdriver.common.by import By
class CheckOutCompletePage:
    Complete_Header=(By.CLASS_NAME,'complete-header')
    def __init__(self,driver):
        self.driver=driver
    def get_complete_message(self):
        try:
            return self.driver.find_element(*self.Complete_Header).text
        except:
            return None