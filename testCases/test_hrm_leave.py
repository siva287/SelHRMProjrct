from selenium.webdriver.common.by import By


class TestOrangeHRMLeave:

    def test_orange_leave(self, setup):
        self.driver = setup
        self.driver.find_element(By.LINK_TEXT, "Leave").click()
        self.driver.find_element(By.XPATH, "//span[@class='oxd-topbar-body-nav-tab-item']").click()
        elelist = self.driver.find_elements(By.XPATH, "//a[@class='oxd-topbar-body-nav-tab-link']")
        for ele in elelist:
            print(ele.text)