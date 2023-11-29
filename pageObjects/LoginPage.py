from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username_name = "username"
    textbox_password_name = "password"
    button_login_xpath = "//button[@type='submit']"
    to_logOut_xpath = "//p[@class='oxd-userdropdown-name']"
    way_to_logout_xpath = "//p[@class='oxd-userdropdown-name']"
    link_logout_linktext = "Logout"
    allert_mess_xpath = "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']"

    def __init__(self, driver):
        self.driver = driver

    def setusername(self, username):
        self.driver.find_element(By.NAME, self.textbox_username_name).clear()
        self.driver.find_element(By.NAME, self.textbox_username_name).send_keys(username)

    def setpassword(self, password):
        self.driver.find_element(By.NAME, self.textbox_password_name).clear()
        self.driver.find_element(By.NAME, self.textbox_password_name).send_keys(password)

    def login(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def logout(self):
        self.driver.find_element(By.XPATH, self.way_to_logout_xpath).click()
        self.driver.find_element(By.LINK_TEXT, self.link_logout_linktext).click()

    def element_present(self):
        self.driver.find_element(By.XPATH, self.way_to_logout_xpath).is_displayed()




