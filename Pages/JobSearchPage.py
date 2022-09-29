from Pages.HomePage import HomePage
from Locators.Locators import JobSearch


class JobSearchPage(HomePage):

    def __init__(self, driver):
        self.locator = JobSearch
        self.driver = driver
        super(JobSearchPage, self).__init__(driver)

    def click_on_advertise_close(self):
        self.find_element(*self.locator.advertise_xpath).click()

    def enter_job_type_text(self):
        self.find_element(*self.locator.jobsearch_textbox_xpath).send_keys("QA Engineer")

    def click_organization_type(self):
        self.find_element(*self.locator.organization_type_xpath).click()

    def select_organization_type(self):
        self.find_element(*self.locator.private_firm_xpath).click()

    def click_search(self):
        self.find_element(*self.locator.job_search_button_xpath).click()
