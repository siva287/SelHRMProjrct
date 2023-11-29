import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# serv_obj=Service("C:/Users/konda/Drivers/chromedriver.exe")
# driver=webdriver.Chrome(service=serv_obj)
def test_me():
    driver = webdriver.Chrome()
    driver.get("https://www.aptransport.org/")
    driver.implicitly_wait(10)
    print(driver.title)
    mh = driver.find_element(By.LINK_TEXT, "LICENCE")
    ac = ActionChains(driver)
    ac.move_to_element(mh).click().perform()
    # //a[@target='_blank'][1]
    # //a[@class='top_link'][1]
    driver.find_element(By.LINK_TEXT, "Permanent Licence").click()
    wins = driver.window_handles
    driver.switch_to.window(wins[0])
    print(driver.title)