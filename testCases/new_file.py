# serv_obj=Service("C:/Users/konda/Drivers/chromedriver.exe")
# driver=webdriver.Chrome(service=serv_obj)
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def test_me():
    driver = webdriver.Chrome()
    driver.get("https://www.aptransport.org/")
    driver.implicitly_wait(10)
    print(driver.title)
    mh = driver.find_element(By.LINK_TEXT, "LICENCE")
    ac = ActionChains(driver)
    ac.move_to_element(mh).click().perform()hjsdfiuiJSF
huihsfjnWE
IHUYESE
JIHSFGE
