from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class OrangeHRMPage:
    side_options_xpath = "//ul[@class='oxd-main-menu']/li"

    def __init__(self, driver):
        self.driver = driver

    def oranage_hrm_main_options(self):
        self.elements = self.driver.find_elements(By.XPATH, self.side_options_xpath)
        for element in self.elements:
            print(element.text)

