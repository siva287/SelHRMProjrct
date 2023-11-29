import time

from pageObjects.LoginPage import LoginPage


class Test001Login:
    baseURL = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
    usename = "Admin"
    password = "admin123"

    def test_homepagetitle(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        print(act_title)

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(10)
        self.driver.save_screenshot(".\\ScreenShots\\" + "test_login.png")
        self.lp = LoginPage(self.driver)
        self.lp.setusername(self.usename)
        self.lp.setpassword(self.password)
        self.lp.login()
#         //p[@class='oxd-userdropdown-name']
