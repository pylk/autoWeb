#coding=utf-8
import time

from AutoFramework.core.pom import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random

#数据管理
class Module_DataManage_OverallReport_FirePower_Daily(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_DataManage_OverallReport_FirePower_Daily,self).__init__(*args,**kwargs)
        self.reportHeader=(By.XPATH,"//h1")

    def check_ReportName(self,value):
        self.checkPoint_contain(self.reportHeader,value)

    def check_dataTable(self,value):
        xpath="//h1[text()='"+value+"']/..//following-sibling::*//table[1]"
        if self.waitUntil((By.XPATH,xpath))==False:
            self.fail("数据表 "+value+" 不存在")



class Module_DataManage_OverallReport_FirePower_OverallReport(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_DataManage_OverallReport_FirePower_OverallReport,self).__init__(*args,**kwargs)
        self.reportHeader=(By.XPATH,"//h1")

    def check_ReportName(self,value):
        self.checkPoint_contain(self.reportHeader,value)

    def check_dataTable(self,value):
        xpath="//h1[text()='"+value+"']/..//following-sibling::*//table[1]"
        if self.waitUntil((By.XPATH,xpath))==False:
            self.fail("数据表 "+value+" 不存在")



class Module_DataManage_OverallReport_WaterPower(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_DataManage_OverallReport_WaterPower,self).__init__(*args,**kwargs)
        self.reportHeader=(By.XPATH,"//h1")

    def check_ReportName(self,value):
        self.checkPoint_contain(self.reportHeader,value)

    def check_dataTable(self,value):
        xpath="//h1[text()='"+value+"']/..//following-sibling::*//table[1]"
        if self.waitUntil((By.XPATH,xpath))==False:
            self.fail("数据表 "+value+" 不存在")

class Module_DataManage_OverallReport_SunPower(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_DataManage_OverallReport_SunPower,self).__init__(*args,**kwargs)
        self.reportHeader=(By.XPATH,"//h1")

    def check_ReportName(self,value):
        self.checkPoint_contain(self.reportHeader,value)

    def check_dataTable(self,value):
        xpath="//h1[text()='"+value+"']/..//following-sibling::*//table[1]"
        if self.waitUntil((By.XPATH,xpath))==False:
            self.fail("数据表 "+value+" 不存在")

class Module_DataManage_OverallReport_CoalPower(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_DataManage_OverallReport_CoalPower,self).__init__(*args,**kwargs)
        self.reportHeader=(By.XPATH,"//h1")

    def check_ReportName(self,value):
        self.checkPoint_contain(self.reportHeader,value)

    def check_dataTable(self,value):
        xpath="//h1[text()='"+value+"']/..//following-sibling::*//table[1]"
        if self.waitUntil((By.XPATH,xpath))==False:
            self.fail("数据表 "+value+" 不存在")

class Module_DataManage_OverallReport_OtherProduct(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_DataManage_OverallReport_OtherProduct,self).__init__(*args,**kwargs)
        self.reportHeader=(By.XPATH,"//h1")

    def check_ReportName(self,value):
        self.checkPoint_contain(self.reportHeader,value)

    def check_dataTable(self,value):
        xpath="//h1[text()='"+value+"']/..//following-sibling::*//table[1]"
        if self.waitUntil((By.XPATH,xpath))==False:
            self.fail("数据表 "+value+" 不存在")