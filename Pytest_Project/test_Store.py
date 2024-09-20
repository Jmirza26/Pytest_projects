from selenium import webdriver
from StorePages import SwagLabsPage

class TestBank:

    def test_bank_login(self):      #1 Login test case
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        self.bp = SwagLabsPage(self.driver)
        self.bp.setUsername("standard_user")
        self.bp.setPassword("secret_sauce")
        self.bp.clickLogin()


    def test_Add_to_cart(self): #2 Add item to cart test case
        self.test_bank_login()
        self.bp.verify_title()
        self.bp.verifyItems()
        self.bp.clickAddtoCart()


    def test_Checkout(self): #3 Checking out item test case
        self.test_bank_login()
        self.test_Add_to_cart()
        self.bp.clickShoppingCart()
        self.bp.verifyBackupDetails()
        self.bp.clickCheckout()
        self.bp.setFirstName("Derrick")
        self.bp.setLastName("Johnson")
        self.bp.setZipcode("22232")
        self.bp.clickContinue()
        self.bp.clickFinish()
        self.bp.verifyOrderMsg()
