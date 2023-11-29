import time

from pageObjects.orange_hrm_page import OrangeHRMPage
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig


class TestOrangeMainOptions:

    url = ReadConfig.getApplicationURL()
    user = ReadConfig.getusername()
    passw = ReadConfig.getpassword()


    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
        self.lp = LoginPage(self.driver)
        self.lp.setusername(self.user)
        self.lp.setpassword(self.passw)
        self.lp.login()
        self.op = OrangeHRMPage(self.driver)
        self.op.oranage_hrm_main_options()
        time.sleep(20)


