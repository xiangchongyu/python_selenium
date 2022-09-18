'''

Basepage是POM中的基类 ，主要提供常用的函数，为页面对象服务

selenium 常用函数：
    元素定位
    输入
    点击
    访问url
    等待
    关闭
    ...
'''
from time import sleep

from selenium import webdriver


class BasePage:
    # 虚构一个driver对象
    # driver = webdriver.Chrome('F:\\python_selenium\\Package\\chromedriver.exe')

    def __init__(self,driver):
        self.driver = driver

    def visit(self):
        self.driver.get(self.url)

    # 元素定位
    def locator(self,*loc):
        return self.driver.find_element(*loc)

    # 输入
    def input_(self,loc,txt):
        self.locator(loc).send_keys(txt)
    # 点击
    def click(self,loc):
        self.locator(loc).click()
    # 访问url
    # 等待
    def wait(self,time_):
        sleep(time_)
    # 关闭
