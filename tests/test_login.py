import csv
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from ..pages.login_page import Login
from ..pages.utilities import Utilities

class Test_CalculatorTest(TestCase):

    @classmethod
    def setUp(cls):
        options = Options()
        options.headless = True  
        cls.driver = webdriver.Firefox(options=options)
        cls.driver.get("https://www.saucedemo.com/")
        cls.login_page = Login(cls.driver)
       
    @classmethod
    def tearDown(cls):
        if cls.driver.current_url == "https://www.saucedemo.com/inventory.html":
            Utilities.logout(cls.driver)
        cls.driver.quit()

    def test_login(self):
        expected_result = False
        for username in self.login_page.usernames:
            self.login_page.login(self,username,self.login_page.password)

            if username == "locked_out_user":
                expected_result = True

            self.assertEqual(self.login_page.error_message(self), expected_result)  



