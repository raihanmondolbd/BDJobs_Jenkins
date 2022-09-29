import time

from Pages.BasePage import BasePage
from Pages.TopBarPage import TopBarPage


class test_TopBar(BasePage):
    def test_topbar_navigation(self):
        tb = TopBarPage(self.driver)

        # tb.click_on_advertise_close()
        tb.click_mybdjobs()
        time.sleep(3)
        tb.click_elearning()
        time.sleep(3)
        tb.click_tender()
        time.sleep(3)
        tb.click_employers()
