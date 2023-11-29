import time
from utilities import ExcelUtilities
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
path = "C:\\Users\\konda\\OneDrive\\Desktop\\HRMBook.xlsx"
sheetname = "Sheet2"
mylist1=[]
row = ExcelUtilities.getrowcount(path, sheetname)
col = ExcelUtilities.getcolumncount(path, sheetname)
for r in range(2, row+1):
    for c in range(1, col+1):
     mylist = ExcelUtilities.readdata(path, sheetname, r, c)
     print(mylist)
     mylist1.append(mylist)
serv_obj=Service("C:/Users/konda/Drivers/chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://opensource-demo.orangehrmlive.com/")
print(driver.title)
time.sleep(4)
driver.find_element(By.NAME,"username").send_keys(mylist1[0])
driver.find_element(By.NAME,"password").send_keys(mylist1[1])
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(6)
# driver.find_element(By.NAME,"username").text()








