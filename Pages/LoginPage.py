from Pages.HomePage import HomePage
from Locators.Locators import LogIn

class LoginPage(HomePage):
    def __init__(self, driver):
        self.locator =  LogIn
        self.driver = driver
        super(LoginPage, self).__init__(driver)

    def click_on_advertise_close(self):
        self.find_element(*self.locator.advertise_xpath).click()

    def click_on_login(self):
        self.find_element(*self.locator.signIn_xpath).click()

    def click_on_login2(self):
        self.find_element(*self.locator.signIn_xpath2).click()

    def enter_email(self, email):
        self.find_element(*self.locator.email_textbox_xpath).send_keys(email)

    def click_next(self):
        self.find_element(*self.locator.next_button_xpath).click()

    def enter_password(self, password):
        self.find_element(*self.locator.password_button_xpath).send_keys(password)

    def click_login3(self):
        self.find_element(*self.locator.signIn_xpath3).click()

    def click_facebook(self):
        self.find_element(*self.locator.facebook_button_xpath).click()

