import time
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customlogger import LogGen

class Test_0011_Login:

    url = ReadConfig.getApplicationURL()
    user = ReadConfig.getusername()
    passw = ReadConfig.getpassword()

    logger=LogGen.loggen()
    def test_homepageTitle(self,setup):
        self.logger.info("******Test_001_Login*****")
        self.logger.info("******Verifing HomePage*****")
        self.driver= setup
        self.driver.get(self.url)
        act_title=self.driver.title
        self.logger.info("******Printing Title*****")
        print(act_title)


    def test_login(self, setup):
        self.logger.info("******verifing Login*****")
        self.driver = setup
        self.driver.get(self.url)
        time.sleep(10)
        #self.driver.save_screenshot(".\\ScreenShots\\" + "test_login.png")
        self.logger.info("******sending username*****")
        self.lp = LoginPage(self.driver)
        self.logger.info("******giving correct password*****")
        self.lp.setusername(self.user)
        self.lp.setpassword(self.passw)
        self.lp.login()
        self.logger.info("******Login successed*****")
        time.sleep(10)
        print("logged success by config read")

