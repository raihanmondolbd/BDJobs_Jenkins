import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class BasePage(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(cls):
        service = Service(executable_path=ChromeDriverManager().install())
        option = Options()
        option.add_argument('--headless')
        option.add_argument('window-size=1920, 1080')
        cls.driver = webdriver.Chrome(service=service, options=option)
        cls.driver.maximize_window()
        cls.driver.get("https://www.bdjobs.com/")
        print("Test Started")

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        cls.driver.quit()
        print("Test Complete")