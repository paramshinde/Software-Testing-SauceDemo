from selenium import webdriver

def test_page_title():
    driver=webdriver.Edge()
    driver.get("https://www.saucedemo.com/")
    if "Swag Labs" in driver.title:
        print("passed")
    else:
        print("error")
    driver.quit()
test_page_title()