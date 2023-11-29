import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage

baseURL = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
usename = "Admin"
password = "admin123"

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(baseURL)
    return driver
