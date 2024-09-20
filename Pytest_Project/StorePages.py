from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class SwagLabsPage:
    textbox_username_css = "input[id='user-name']"
    textbox_password_css = "input[id='password']"
    button_login_css = "input[id='login-button']"
    button_backpack_id = "add-to-cart-sauce-labs-backpack"
    button_cart_xpath = "//div[@class='shopping_cart_container' and @class='shopping_cart_container']"
    text_backpack_css = "div[class='inventory_item_desc']"
    button_checkout_css = "button[id=checkout]"
    textbox_firstname_css = "input[id='first-name']"
    textbox_lastname_css = "input[id='last-name']"
    textbox_zipcode_css = "input[id='postal-code']"
    button_continue_css = "input[id='continue']"
    button_finish_css = "button[id='finish']"
    expected_ordermsg_css = "h2[data-test=complete-header]"
    button_back_home_xpath = "//button[@name='back-to-products']"
    list_items_xpath = "//div[@class='inventory_item']"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        usernametxt = self.driver.find_element(By.CSS_SELECTOR, self.textbox_username_css)
        usernametxt.send_keys(username)

    def setPassword(self, password):
        passtxt = self.driver.find_element(By.CSS_SELECTOR, self.textbox_password_css)
        passtxt.send_keys(password)

    def clickLogin(self):
        loginbttn = self.driver.find_element(By.CSS_SELECTOR, self.button_login_css)
        loginbttn.click()

    def get_title(self):
        return self.driver.title

    def verify_title(self, expected_title="Swag Labs"):
        actual_title = self.get_title()
        assert actual_title == expected_title, f"Expected title '{expected_title}', but got '{actual_title}'"

    def verifyItems(self):
        items = self.driver.find_elements(By.XPATH, self.list_items_xpath)
        print(len(items))
        for ele in items:
            print(ele.text)

    def clickAddtoCart(self):
        self.driver.find_element(By.ID, self.button_backpack_id).click()

    def clickShoppingCart(self):
        self.driver.find_element(By.XPATH, self.button_cart_xpath).click()

    def verifyBackupDetails(self):
        backpack = self.driver.find_element(By.CSS_SELECTOR, self.text_backpack_css).text
        expected_backpack = "carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection."
        if backpack == expected_backpack:
            print(backpack)
        else:
            print("Error")

    def clickCheckout(self):
        self.driver.find_element(By.CSS_SELECTOR, self.button_checkout_css).click()

    def setFirstName(self, firstname):
        fntxt = self.driver.find_element(By.CSS_SELECTOR, self.textbox_firstname_css)
        fntxt.send_keys(firstname)

    def setLastName(self, lastname):
        lntxt = self.driver.find_element(By.CSS_SELECTOR, self.textbox_lastname_css)
        lntxt.send_keys(lastname)

    def setZipcode(self, zipcode):
        ziptxt = self.driver.find_element(By.CSS_SELECTOR, self.textbox_zipcode_css)
        ziptxt.send_keys(zipcode)

    def clickContinue(self):
        self.driver.find_element(By.CSS_SELECTOR, self.button_continue_css).click()

    def clickFinish(self):
        self.driver.find_element(By.CSS_SELECTOR, self.button_finish_css).click()

    def verifyOrderMsg(self):
        ordermsg = self.driver.find_element(By.CSS_SELECTOR, self.expected_ordermsg_css).text
        expected_msg = "Thank you for your order!"
        if ordermsg == expected_msg:
            print("Hello: ", ordermsg)
        else:
            print("Error")
        self.driver.close()