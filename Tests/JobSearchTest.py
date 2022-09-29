import time

from Pages.BasePage import BasePage
from Pages.JobSearchPage import JobSearchPage


class JobSearchTest(BasePage):

    def test_jobSearch(self):
        js = JobSearchPage(self.driver)
        time.sleep(5)
        # js.click_on_advertise_close()
        # time.sleep(3)
        js.enter_job_type_text()
        time.sleep(3)
        js.click_organization_type()
        time.sleep(3)
        js.select_organization_type()
        js.click_search()
        time.sleep(10)
