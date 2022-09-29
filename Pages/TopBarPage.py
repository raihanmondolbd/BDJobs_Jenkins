from Pages.HomePage import HomePage
from Locators.Locators import TopBar


class TopBarPage(HomePage):
    
    def __init__(self, driver):
        self.locator =  TopBar
        self.driver = driver
        super(TopBarPage, self).__init__(driver)

    def click_on_advertise_close(self):
        self.find_element(*self.locator.advertise_xpath).click()

    def click_mybdjobs(self):
        self.find_element(*self.locator.mybdjobs_xpath).click()

    def click_elearning(self):
        self.find_element(*self.locator.elearning_xpath).click()

    def click_tender(self):
        self.find_element(*self.locator.tender_xpath).click()

    def click_employers(self):
        self.find_element(*self.locator.employers_xpath).click()

