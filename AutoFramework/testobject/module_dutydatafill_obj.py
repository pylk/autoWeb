#coding=utf-8
import datetime
import time

from AutoFramework.core.pom import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random

     #光伏抄表
class Module_Duty_sunshinePower_Fill(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_Duty_sunshinePower_Fill,self).__init__(*args,**kwargs)
        # 光伏抄表填报
        self.waterPowerTree = (By.XPATH, "//span[text()='光伏抄表']/../../span[1]")
        self.submitButton = (By.XPATH, "//button[text()='强制提交']")
        self.JanFill=(By.XPATH,"//td[text()='负荷']/../..//td[2]/div/input")
        self.time=(By.XPATH,"//input[@name='time']")
    def input_normalCoal3(self, *num):
            a= num
            self.type(a, (By.XPATH, "//td[text()='负荷']/following-sibling::*//input"))
            self.justWait(10)

    def input_JanFill(self,value):
        self.type(value,self.JanFill)
    def input_inTable(self):
        targets=(By.XPATH,"//td[text()='负荷']/following-sibling::*//input")
        targetsOjb=self.find_elements(targets)
        for one in targetsOjb:
            if "readonly"==one.get_attribute("readonly"):
                print("abc")
                continue
            else:
                one.send_keys(random.randint(1,100))

    def click_submitButton(self):
        self.click(self.submitButton)

    #水电抄表
class Module_Duty_WaterPower_Fill(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_Duty_WaterPower_Fill,self).__init__(*args,**kwargs)
        #水电抄表填报
        self.waterPowerTree=(By.XPATH,"//span[text()='水电']/../../span[1]")
        self.submitButton=(By.XPATH,"//button[@value='强制提交']")
        self.JanFill=((By.XPATH,"//div[text()='负荷']/../following-sibling::*//input[@name='fh']"))

    def click_waterPowerTree(self):
        self.click(self.waterPowerTree)
    def click_submitButton(self):
        self.click(self.submitButton)

    def input_normalCoal3(self,*num):
        a,b,c=num
        self.type(a, (By.XPATH, "//input[@value='毛家河水电厂']/../following-sibling::*//input"))
        self.type(b, (By.XPATH, "//input[@value='象鼻岭水电厂']/../following-sibling::*//input"))
        self.type(c, (By.XPATH, "//input[@value='蒙江水力发电总厂']/../following-sibling::*//input"))
        self.justWait(10)
        
    def input_time(self,day=1):
        self.js_inputRemoveReadOnly(self.time[1],'readOnly')
        now=datetime.datetime.now()
        preDay=now-datetime.timedelta(days=day)
        self.type(preDay,self.time)

    def click_searchButton(self):
        self.click(self.searchButton)

     #煤矿抄表填报
class Module_Duty_coalnuber_Fill(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_Duty_coalnuber_Fill,self).__init__(*args,**kwargs)
        # 煤矿抄表填报
        self.coalPowerTree = (By.XPATH, "//span[text()='煤矿抄表']/../../span[1]")
        self.submitButton = (By.XPATH, "//button[text()='强制提交']")
        self.time=(By.XPATH,"//input[@name='time']")

    def input_JanFill(self,value):
        self.type(value,self.JanFill)
    def input_inTable(self):
        targets=(By.XPATH,"//tbody[@id='tableBody']/*//input")
        targetsOjb=self.find_elements(targets)
        for one in targetsOjb:
            if "readonly"==one.get_attribute("readonly"):
                print("abc")
                continue
            else:
                one.send_keys(random.randint(1,100))
    def click_submitButton(self):
        self.click(self.submitButton)


#火电抄表填报
class Module_Duty_firepower_Fill(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_Duty_firepower_Fill,self).__init__(*args,**kwargs)
        # 火电抄表填报
        self.firePowerTree = (By.XPATH, "//span[text()='火电']/../../span[1]")
        self.dataFill_firePower = (By.XPATH, "//a[text()='火电']//following-sibling::*//a[text()='火电抄表填报']")
        self.submitButton = (By.XPATH, "//button[text()='强制提交']")
        self.time=(By.XPATH,"//input[@name='time']")
        self.input = (By.XPATH, "(//table)[3]//input[@check='number']")
    def input_inTable(self):
        inputs=self.find_elements(self.input)
        for one in inputs:
            rNum=random.randint(0,100)
            if not one.get_attribute('type')=='hidden':
                one.clear()
                one.send_keys(rNum)

    def click_submitButton(self):
        self.click(self.submitButton)

#火电抄表查询
class Module_Duty_firepower_Fill_search(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_Duty_firepower_Fill_search,self).__init__(*args,**kwargs)
        # 火电抄表填报 查询
        self.firePowerTree = (By.XPATH, "//span[text()='火电']/../../span[1]")
        self.searchButton = (By.XPATH, "//input[@value='查询']")
        self.time=(By.XPATH,"//input[@name='filltime']")
        self.retime = (By.XPATH, "//*[@id='slot']/option[5]")
        self.timea=(By.XPATH,"//input[@id='startDate']")
        self.date = (By.XPATH, "//input[@name='filltime']")

    def check_choose(self):
        self.click(self.retime)

    def click_searchButton(self):
        self.click(self.searchButton)

    def input_time(self, day=1):
        self.js_inputRemoveReadOnly(self.time[1], 'readOnly')
        now = datetime.datetime.now()
        preDay = now - datetime.timedelta(days=day)
        self.type(preDay, self.time)

    def input_timea(self, day=1):
        self.js_inputRemoveReadOnly(self.timea[1], 'readOnly')
        now = datetime.datetime.now()
        preDay = now - datetime.timedelta(days=day)
        self.type(preDay, self.time)

    def input_date(self, day=1):
        self.js_inputRemoveReadOnly(self.date[1], 'readOnly')
        now = datetime.datetime.now()
        yesterday = now + datetime.timedelta(day)
        strYest = datetime.datetime.strftime(yesterday, '%Y%m%d')
        self.type(strYest, self.date)

#火电值班查询
class Module_Duty_firepower_modify(BasePage):
    def __init__(self, *args, **kwargs):
        super(Module_Duty_firepower_modify, self).__init__(*args, **kwargs)
        # 火电值班查询
        self.firePowerTree = (By.XPATH, "//span[text()='火电']/../../span[1]")
        self.searchButton = (By.XPATH, "//input[@value='查询']")
        self.msgTable = (By.XPATH, "//table[@class='new-table new-tablehead-bj']")
        self.date = (By.XPATH, "//input[@name='filltime']")
        self.retime = (By.XPATH, "//*[@id='slot']/option[10]")

    def check_choose(self):
        self.click(self.retime)

    def input_date(self,day=0):
        self.js_inputRemoveReadOnly(self.date[1], 'readOnly')
        now = datetime.datetime.now()
        yesterday = now + datetime.timedelta(day)
        strYest = datetime.datetime.strftime(yesterday, '%Y%m%d')
        self.type(strYest, self.date)

    def click_searchButton(self):
        self.click(self.searchButton)

    def count_result(self):
        return self.table_getRowNum(self.msgTable)

 #光伏值班填报
class Module_Duty_sunshine_Fill(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_Duty_sunshine_Fill,self).__init__(*args,**kwargs)
        # 火电抄表填报 查询
        self.firePowerTree = (By.XPATH, "//span[text()='光伏值班填报']/../../span[1]")
        self.searchButton = (By.XPATH, "//input[@value='查询']")
        self.time=(By.XPATH,"//input[@id='date']")
        self.retime = (By.XPATH, "//*[@id='slot']/option[5]")

    def check_choose(self):
        self.click(self.retime)

    def click_searchButton(self):
        self.click(self.searchButton)

    def input_time(self, day=1):
        self.js_inputRemoveReadOnly(self.time[1], 'readOnly')
        now = datetime.datetime.now()
        preDay = now - datetime.timedelta(days=day)
        self.type(preDay, self.time)

    def input_inTable7(self):
        targets7 = (By.XPATH, "//tr[@class='data_tr']/*//input")
        targetsOjb = self.find_elements(targets7)
        for one in targetsOjb:
            if "readonly" == one.get_attribute("readonly"):
                print("abc")
                continue
            else:
                one.send_keys(random.randint(1, 100))

    def input_date(self,day=1):
        self.js_inputRemoveReadOnly("//input[@id='startDate']","readonly")
        now=datetime.datetime.now()
        preDay=now-datetime.timedelta(days=day)
        self.type(datetime.datetime.strftime(preDay,"%Y-%m-%d"),self.date)