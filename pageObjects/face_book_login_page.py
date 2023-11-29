from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class FB_Creating_NewAccount:
    link_create_newAC_linktext = "Create new account"
    textbox_firstname_name = "firstname"
    textbox_surname_name = "lastname"
    textbox_email_name = "reg_email__"
    textbox_password_id = "password_step_input"
    dropdown_day_id = "day"
    dropdown_month_id = "month"
    dropdown_year_id = "year"
    radiobutton_gender_xpath = "//label[text()='Male']"


    def __init__(self, driver):
        self.driver = driver

    def click_on_new_account(self):
        self.driver.find_element(By.LINK_TEXT,self.link_create_newAC_linktext).click()

    def enter_firstname(self, fisrtname):
        self.driver.find_element(By.NAME, self.textbox_firstname_name).send_keys(fisrtname)

    def enter_lastname(self, lastname):
        self.driver.find_element(By.NAME, self.textbox_surname_name).send_keys(lastname)

    def enter_emalid(self,email):
        self.driver.find_element(By.NAME, self.textbox_email_name).send_keys(email)

    def enter_new_password(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def birthday_date(self, day):
        self.day_elemant = self.driver.find_element(By.ID, self.dropdown_day_id)
        self.drp_day = Select(self.day_elemant)
        self.drp_day.select_by_visible_text(day)

    def birthmonth_month(self, month):
        self.month_element = self.driver.find_element(By.ID, self.dropdown_month_id)
        self.drp_month = Select(self.month_element)
        self.drp_month.select_by_visible_text(month)
    def birthyear_year(self, year):
        self.year_element = self.driver.find_element(By.ID, self.dropdown_year_id)
        self.drp_year = Select(self.year_element)
        self.drp_year.select_by_visible_text(year)

    def select_gender(self):
        self.driver.find_element(By.XPATH, self.radiobutton_gender_xpath).click()

