#-*- coding:utf-8 -*-
# author:isyuan
# datetime:22/03/2019 14:36
# software: PyCharm
from AutoFramework.core.pom import BasePage
from selenium.webdriver.common.by import By

class BaiduObj(BasePage):
    def __init__(self, *args, **kwargs):
        super(BaiduObj, self).__init__(*args, **kwargs)
        # self.loginLink=(By.PARTIAL_LINK_TEXT,"登录")
        self.loginLink=(By.XPATH,"//*[@id='u1']/a[7]")
        self.lglink = (By.ID, "TANGRAM__PSP_10__footerULoginBtn")
        self.userName = (By.NAME, "userName")
        self.passWord = (By.NAME, "password")
        self.loginButton = (By.ID, "TANGRAM__PSP_10__submit")


    def bdLogin(self, userName, passWord):
        self.click(self.loginLink)
        self.click(self.lglink)
        self.type(userName, self.userName)
        self.type(passWord, self.passWord)
        self.click(self.loginButton)