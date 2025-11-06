from selenium.webdriver.common.by import By
class LoginPage:
    UserNameInput=(By.ID,'user-name')
    PassInput=(By.ID,'password')
    LoginButton=(By.ID,'login-button')
    ErrorMess=(By.CSS_SELECTOR,"h3[data-test='error']")

    def __init__(self,driver):
        self.driver=driver
    def enter_username(self,username):
        self.driver.find_element(*self.UserNameInput).send_keys(username)
    def enter_password(self,password):
        self.driver.find_element(*self.PassInput).send_keys(password)
    def click_login(self):
        self.driver.find_element(*self.LoginButton).click()
    def get_error_message(self):
        return self.driver.find_element(*self.ErrorMess).text
    def login(self,username,password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
            