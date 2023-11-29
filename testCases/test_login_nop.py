import time

#import pytest
from selenium import webdriver
from pageObjects.login_page import Login
from  utilities.readProperties import ReadConfig

class Test_001_Login_nop:
    # basenopURL = "https://admin-demo.nopcommerce.com/admin/"
    # username = "admin@yourstore.com"
    # password = "admin"
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()

    def test_homepage_title(self, setup):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        ac_title = self.driver.title
        assert ac_title == "Your store. Login"

    def test_002_login_page(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        tilte=self.driver.title
        assert tilte == "Dashboard / nopCommerce administration"
        self.driver.save_screenshot("C:\\Users\\konda\\PycharmProjects\\pythonProject2\\nopcommerceApp\\ScreenShots" + "test_login_nop.png")
        time.sleep(10)
        print("title is ", tilte)



