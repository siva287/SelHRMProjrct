import time
from pageObjects.windows_page import WindowsPage

class TestSwitchingWindows:
    baseURL = "https://netbanking.hdfcbank.com/netbanking/"
    frame_id = "login_page"

    def test_switch_windows(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.wp = WindowsPage(self.driver)
        # self.wp.switching_to_frame(self.frame_id)
        self.driver.switch_to.frame(self.frame_id)
        self.wp.clicking_on_multiple_link()
        time.sleep(10)
