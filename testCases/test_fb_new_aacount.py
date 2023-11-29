import time


from pageObjects.face_book_login_page import FB_Creating_NewAccount
from utilities import ExcelUtilities


class Test001FBAccount:
    baseUrl = "https://www.facebook.com/"
    path = "C:\\Users\\konda\\OneDrive\\Desktop\\HRMBook.xlsx"
    sheetname = "Sheet1"
    my_list_data = []

    def test_creating_new_account(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.implicitly_wait(8)
        self.fb = FB_Creating_NewAccount(self.driver)
        self.fb.click_on_new_account()
        self.rows = ExcelUtilities.getrowcount(self.path, self.sheetname)
        for r in range(2, self.rows+1):
            self.firstname = ExcelUtilities.readdata(self.path, self.sheetname, r, 1)
            self.my_list_data.append(self.firstname)
        print(self.my_list_data)
        self.fb.enter_firstname(self.my_list_data[0])
        self.fb.enter_lastname(self.my_list_data[1])
        self.fb.enter_emalid(self.my_list_data[2])
        self.fb.enter_new_password(self.my_list_data[3])
        time.sleep(5)
        self.fb.birthday_date(str(self.my_list_data[4]))
        self.fb.birthmonth_month(self.my_list_data[5])
        self.fb.birthyear_year(str(self.my_list_data[6]))
        time.sleep(5)
        self.fb.select_gender()
        time.sleep(10)
