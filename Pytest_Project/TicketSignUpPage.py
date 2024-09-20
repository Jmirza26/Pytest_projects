import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class RegistrationPage:
    textbox_firstname_xpath="//input[@id='travname']"
    textbox_lastname_xpath="//input[@id='travlastname']"
    box_dob_xpath="//input[@id='dob']"
    select_month_xpath="//select[@class='ui-datepicker-month']"
    select_year_xpath="//select[@class='ui-datepicker-year']"
    month = "Jun"
    year = 2021
    dates_xpath="//div[@id='ui-datepicker-div']//table/tbody/tr/td/a"

    radiobutton_male_xpath="//label[@for='sex_1']"
    textbox_fromcity_xpath="//input[@id='fromcity']"
    textbox_tocity_xpath = "//input[@id='tocity']"

    box_depart_xpath="//input[@id='departon']"
    select_depmonth_xpath="//select[@class='ui-datepicker-month']"
    select_depyear_xpath="//select[@class='ui-datepicker-year']"
    depart_dates="//div[@id='ui-datepicker-div']//table/tbody/tr/td/a"

    textbox_phonenum_xpath="//input[@id='billing_phone']"
    textbox_email_xpath="//input[@id='billing_email']"
    textbox_address_xpath="//input[@id='billing_address_1']"
    textbox_city_xpath="//input[@id='billing_city']"

    box_state_xpath="//span[@id='select2-billing_state-container']"
    textbox_postcode_xpath="//input[@id='billing_postcode']"
    button_paypal_xpath="//button[@id='place_order']"


    def __init__(self, driver):
        self.driver = driver

    def setFirstName(self, firstname):
        firstnametxt = self.driver.find_element(By.XPATH, self.textbox_firstname_xpath)
        firstnametxt.send_keys(firstname)

    def setLastName(self, lastname):
        lastnametxt = self.driver.find_element(By.XPATH, self.textbox_lastname_xpath)
        lastnametxt.send_keys(lastname)
        time.sleep(3)

    def clickDateofBirth(self):
        dateofbirthbox = self.driver.find_element(By.XPATH, self.box_dob_xpath)
        dateofbirthbox.click()

    def setMonthYear(self):
        mon = self.driver.find_element(By.XPATH, self.select_month_xpath)
        drpdown_month = Select(mon)
        drpdown_month.select_by_visible_text("Jul")

        yr = self.driver.find_element(By.XPATH, self.select_year_xpath)
        drpdown_year = Select(yr)
        drpdown_year.select_by_value("2021")


    def setDate(self):
        dates = self.driver.find_elements(By.XPATH, self.dates_xpath)
        for ele in dates:
            if ele.text == "3":
                ele.click()
                break

    def clickGender(self):
        rdio_bttn = self.driver.find_element(By.XPATH, self.radiobutton_male_xpath)
        rdio_bttn.click()

    def setFromCity(self, frmcity):
        citytxt = self.driver.find_element(By.XPATH, self.textbox_fromcity_xpath)
        citytxt.send_keys(frmcity)

    def setToCity(self, tocity):
        tocitytxt = self.driver.find_element(By.XPATH, self.textbox_tocity_xpath)
        tocitytxt.send_keys(tocity)

    def clickDepartDate(self):
        departuretxt = self.driver.find_element(By.XPATH, self.box_depart_xpath)
        departuretxt.click()

    def setDepartMon(self):
        depMonth = self.driver.find_element(By.XPATH, self.select_depmonth_xpath)
        drpdown_month = Select(depMonth)
        drpdown_month.select_by_visible_text("Dec")


    def setDepartYear(self):
        depYear = self.driver.find_element(By.XPATH, self.select_depyear_xpath)
        drpdown_year = Select(depYear)
        drpdown_year.select_by_visible_text("2024")

    def setDepartDate(self):
        dates = self.driver.find_elements(By.XPATH, self.depart_dates)
        for ele in dates:
            if ele.text == "25":
                ele.click()
                break


    def setPhoneNum(self, phonenumber):
        phonetxt = self.driver.find_element(By.XPATH, self.textbox_phonenum_xpath)
        phonetxt.send_keys(phonenumber)

    def setEmailAdd(self, emailaddress):
        emailtxt = self.driver.find_element(By.XPATH, self.textbox_email_xpath)
        emailtxt.send_keys(emailaddress)

    def setAddress(self, address):
        addresstxt = self.driver.find_element(By.XPATH, self.textbox_address_xpath)
        addresstxt.send_keys(address)

    def setCity(self, city):
        citytxt = self.driver.find_element(By.XPATH, self.textbox_city_xpath)
        citytxt.send_keys(city)

    def clickState(self):
        state_button = self.driver.find_element(By.XPATH, self.box_state_xpath)
        state_button.click()

    def setState(self):
        states_xpaths = self.driver.find_elements(By.XPATH, "//li[@class='select2-results__option']")
        for ele in states_xpaths:
            if ele.text == "Illinois":
                ele.click()
                break

    def setPostal(self, postcode):
        postcodetxt=self.driver.find_element(By.XPATH, self.textbox_postcode_xpath)
        postcodetxt.send_keys(postcode)

    def clickPaypal(self):
        paypal_button = self.driver.find_element(By.XPATH, self.button_paypal_xpath)
        paypal_button.click()


    def title(self):
        return self.driver.title