#coding=utf-8
import time

from AutoFramework.core.pom import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random

#配置管理 指标配置
class Module_ConfigManage_MatrixConfig(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_ConfigManage_MatrixConfig,self).__init__(*args,**kwargs)
        #三方公司
        self.thirdPartCompany=(By.NAME,"otherCompany1")
        #角色
        self.role=(By.NAME,"roleId")
        #组织级别
        self.orgType=(By.NAME,"levelType1")
        #新增按钮
        self.addButton=(By.XPATH,"//button[text()='新增']")

        #新增组织级别
        self.addlevelType=(By.XPATH,"//div[@class='trendInquire']//descendant::*//select[@name='levelType']")
        #新增板块
        self.addmodule=(By.XPATH,"//div[@class='trendInquire']//descendant::*//select[@name='plate']")
        #新增电厂
        self.addpowerPlant=(By.XPATH,"//div[@class='trendInquire']//descendant::*//select[@name='powerPlant']")
        #新增分厂
        self.addfactory=(By.XPATH,"//div[@class='trendInquire']//descendant::*//select[@name='factory']")
        #新增机组
        self.addunit=(By.XPATH,"//div[@class='trendInquire']//descendant::*//select[@name='unit']")

        #新增表格
        self.addTable=(By.ID,"table2")

        #新增按钮
        self.saveButton=(By.XPATH,"//button[text()='保存']")

    def select_thirdPartCompany(self,value):
        self.selectByText(self.thirdPartCompany,value)
    def select_role(self,value):
        self.selectByText(self.role,value)
    def select_orgType(self,value):
        self.selectByText(self.orgType,value)

    def click_addButton(self):
        self.click(self.addButton)

    def select_addlevelType(self,value):
        self.selectByText(self.addlevelType,value)
    def select_addModule(self,value):
        self.selectByText(self.addmodule,value)
    def select_addpowerPlant(self,value):
        self.selectByText(self.addpowerPlant,value)
    def select_addfactory(self,value):
        self.selectByText(self.addfactory,value)
    def select_addunit(self,value):
        self.selectByText(self.addunit,value)
    def choose_oneItemInTable(self):
        self.table_SelectByIndex(self.addTable,2)

    def click_saveButton(self):
        try:
            self.click(self.saveButton)
        except Exception as e:
            print(e)
        finally:
            self.switchAlertAccept()



#配置管理 指标维护
class Module_ConfigManage_MatrixMaintance(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_ConfigManage_MatrixMaintance,self).__init__(*args,**kwargs)
