from selenium.webdriver.common.by import By

class WindowsPage:
    links_for_windows_linktext = "//table/tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def switching_to_frame(self):
        self.driver.switch_to.frame()

    def clicking_on_multiple_link(self):
        self.windows = self.driver.find_elements(By.XPATH, self.links_for_windows_linktext)
        for window in self.windows:
            window.click()
