from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class Spicejet:
    mouse_hover_add_ons_class = "css-76zvg2 r-jwli3a r-ubezar r-16dba41 r-1pzd9i8"
    link_visa_services_class = "css-76zvg2 r-homxoj r-ubezar"
    link_countries_xpath = "//ul[@class='visa-list']/li/a"

    def __init__(self, driver):
        self.driver = driver

    def click_on_add_ons(self):
        self.ad_element=self.driver.find_element(By.CLASS_NAME, self.mouse_hover_add_ons_class)
        ac = ActionChains(self.driver)
        ac.move_to_element(self.ad_element).click().perform()
    def select_visa_services(self):
        self.driver.find_element(By.CLASS_NAME, self.link_visa_services_class).click()

    def click_on_countries(self):
        self.countires = self.driver.find_elements(By.XPATH, self.link_countries_xpath)
        for country in self.countires:
            country.click()

