from selenium import webdriver
from selenium.webdriver.common.by import By
from TicketSignUpPage import RegistrationPage


class TestTicket:

    url="https://www.dummyticket.com/dummy-ticket-for-visa-application/"
    firstName="Zach"
    lastName="Philips"
    email="Bababooey1237@yahoo.com"




    def test_ticket(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        self.driver.maximize_window()

        self.tk = RegistrationPage(self.driver)
        self.tk.setFirstName(self.firstName)
        self.tk.setLastName(self.lastName)
        self.tk.clickDateofBirth()
        self.tk.setMonthYear()
        self.tk.setDate()
        self.tk.clickGender()
        self.tk.setFromCity("China")
        self.tk.setToCity("Los Angeles")
        self.tk.clickDepartDate()
        self.tk.setDepartMon()
        self.tk.setDepartYear()
        self.tk.setDepartDate()
        self.tk.setPhoneNum("822-555-8283")
        self.tk.setEmailAdd(self.email)
        self.tk.setAddress("421 Pinecone St")
        self.tk.setCity("Moscow")
        self.tk.clickState()
        self.tk.setState()
        self.tk.setPostal(50031)
        self.tk.clickPaypal()
        parent_handle = self.driver.window_handles
        parentWindowID = parent_handle[0]
        self.driver.switch_to.window(parentWindowID)
        assert "Log in to your PayPal account", self.driver.title
        print(self.driver.title, "Test Successfully passed ✅")
        self.driver.close()




