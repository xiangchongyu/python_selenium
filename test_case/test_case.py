import time
import unittest

from selenium import webdriver
from page_object import Login_Page
from page_object.Login_Page import LoginPage
from page_object.IndexPage import IndexPage

from ddt import ddt, file_data, data

@ddt
class TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.lp = LoginPage(cls.driver)
        cls.ip = IndexPage(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    @file_data('../data/user.yaml')
    def test_01_login(self,username,pwd):


        txt = 'shouji'
        # lp = LoginPage(driver)
        self.lp.Login(username,pwd)
        # ip= IndexPage(driver)
        time.sleep(3)

    @data('shouji','衣服','帽子')
    def test_02_search(self,txt):
        self.ip.search(txt)

if __name__=='__main__':
    unittest.main()