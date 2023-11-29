from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pageObjects.spicejet_page import Spicejet

class TestSpicejet:
    baseURL = "https://www.spicejet.com/"

    def test_spicejet_countries(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(10)
        # self.driver.switch_to.alert.dismiss()
        # self.driver.find_element(By.LINK_TEXT, "Hotels").click()
        # time.sleep(10)
        # self.ad_element = self.driver.find_element(By.LINK_TEXT, "Add-ons")
        # self.ac = ActionChains(self.driver)
        # self.ac.move_to_element(self.ad_element).click().perform()
        # self.sp = Spicejet(self.driver)
        # self.sp.click_on_add_ons()
        self.driver.switch_to.frame("class=css-76zvg2 r-jwli3a r-ubezar r-16dba41 r-1pzd9i8")
        self.driver.find_element(By.LINK_TEXT, "Add-ons").click()
        self.windows=self.driver.window_handles
        self.driver.switch_to.window(1)
        self.sp.select_visa_services()
        self.sp.click_on_countries()


