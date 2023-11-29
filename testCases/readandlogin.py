import time

from pageObjects.LoginPage import LoginPage
from utilities import ExcelUtilities


class Test_0011_Login:
    baseURL = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
    path = "C:\\Users\\konda\\OneDrive\\Desktop\\HRMBook.xlsx"
    username = "Admin"
    password = "admin123"

    def test_homepageTitle(self,setup):
        self.driver= setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        print(act_title)

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.save_screenshot(".\\ScreenShots\\" + "test_login.png")
        self.lp = LoginPage(self.driver)
        self.driver.implicitly_wait(10)
        self.rows=ExcelUtilities.getrowcount(self.path, 'Sheet1')
        print(self.rows)
        for r in range(2, self.rows+1):
            self.username=ExcelUtilities.readdata(self.path, 'Sheet1',r,1)
            self.password=ExcelUtilities.readdata(self.path, 'Sheet1',r,2)
            print(self.username)
            print(self.password)
            self.lp.setusername(self.username)
            self.lp.setpassword(self.password)
            self.lp.login()
            print("logged in success")
            time.sleep(8)
            if self.lp.element_present():
                print("element displayed")
                self.lp.logout()
                print("logged out success")
                time.sleep(8)
            else:
                print(self.lp.get_allert_messeage)
                time.sleep(8)

