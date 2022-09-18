'''

页面对象
'''
from selenium import webdriver
from selenium.webdriver.common.by import By

from base.Base_Page import BasePage


class LoginPage(BasePage):
    # 核心业务
    url = 'https://wwww.baidu.com'

    user = (By.NAME,'userName')
    PWD = (By.NAME,'password')
    login_Button =(By.ID,'s-top-loginbtn')
    login_web = (By.ID,'TANGRAM__PSP_11__footerULoginBtn')
    login_baidu  = (By.ID,'TANGRAM__PSP_11__submit')
    #  BasePage.click()
    # TANGRAM__PSP_11__footerULoginBtn
    # 核心业务流
    def Login(self,username,pwd):
        self.visit()
        self.click(self.login_Button)
        self.wait(1)
        self.click(self.login_web)

        self.input_(self.user,username)
        self.input_(self.PWD,pwd)
        self.click(self.login_baidu)

if __name__ =='__main__':
    pass
    # driver =webdriver.Chrome()
    # username = '15171364206'
    # pwd = 'yxc,./123'
    # lp =LoginPage(driver)
    # lp.Login(username,pwd)
