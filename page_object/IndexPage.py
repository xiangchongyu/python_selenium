'''

页面对象
'''
from selenium import webdriver
from selenium.webdriver.common.by import By

from base.Base_Page import BasePage


class IndexPage(BasePage):
    # 核心业务

    url = 'https://wwww.baidu.com'

    search_input = (By.NAME, 'wd')
    search_button = (By.ID,'su')

    # 核心业务流
    def search(self,txt):
        self.visit()
        self.input_(self.search_input,txt)
        self.click(self.search_button)




if __name__ == '__main__':
    pass

    # driver = webdriver.Chrome()
    # txt = 'shuji'
    # ip =IndexPage(driver)
    # ip.search(txt)
