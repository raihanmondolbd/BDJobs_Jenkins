from Pages.LoginPage import LoginPage
from Pages.BasePage import BasePage

class LoginTest(BasePage):
    def test_login_page(self):

        loginPage = LoginPage(self.driver)
        # loginPage.click_on_advertise_close()
        loginPage.click_on_login()
        loginPage.click_on_login2()
        loginPage.enter_email("raihanmondolbd@gmail.com")
        loginPage.click_next()
        loginPage.enter_password("123456")
        loginPage.click_login3()
