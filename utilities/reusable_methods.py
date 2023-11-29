from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select


class Reusabilities:
    serv_obj = Service("C:/Users/konda/Drivers/chromedriver.exe")
    driver = webdriver.Chrome(service=serv_obj)

    def __init__(self, driver):
        self.driver = driver

    def switch_window(self):
        self.windows_list = self.driver.window_handles
        for window in self.windows_list:
            self.driver.switch_to.window(window)

    def switch_to_frame(self, id):
        self.driver.switch_to.frame(id)

    def defualt_content(self):
        self.driver.switch_to.default_content()

    def switch_to_alert(self):
        self.driver.switch_to.alert.accept()

    def select_dropdowns(self, elements, text):
        self.select_cls = Select(elements)
        self.select_cls.select_by_visible_text(text)

    def action_chains(self, element):
        self.action=ActionChains(self.driver)
        self.action.move_to_element(element)

