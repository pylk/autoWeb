#coding=utf-8
import datetime
import time

from AutoFramework.core.pom import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random


class Module_DutyFill_FirePower_FirePowerFill_Fill(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_DutyFill_FirePower_FirePowerFill_Fill,self).__init__(*args,**kwargs)

        self.submitButton=(By.XPATH,"//button[text()='提交']")
        self.forceSubmitButton=(By.XPATH,"//button[text()='强制提交']")
        self.submitUpdateButton=(By.XPATH,"//button[text()='提交更新']")

        self.input=(By.XPATH,"(//table)[3]//tbody//td/input[@check='number']")
        self.date = (By.XPATH, "//input[@id='filltime']")
        self.time=(By.XPATH,"//select[@id='slot']")

        self.searchButton=(By.XPATH,"//input[@value='查询']")

    def is_element_exist(self, selector):
        try:
            self.find_elements(selector)
            return True
        except:
            return False

    def click_submitButton(self):
        self.click(self.submitButton)
    def click_forceSubmitButton(self):
        self.click(self.forceSubmitButton)
    def click_submitUpdateButton(self):
        self.click(self.submitUpdateButton)

    def click_searchFromTime(self,day=0,time=10):
        self.js_inputRemoveReadOnly(self.date[1],'readOnly')
        now=datetime.datetime.now()
        yesterday = now+datetime.timedelta(day)
        strYest=datetime.datetime.strftime(yesterday,'%Y%m%d')
        self.type(strYest,self.date)

        # self.selectByInnerValue(self.time,time)
        self.click((By.XPATH,"//select[@id='slot']"))
        self.click((By.XPATH,"//option[@value='"+str(time)+"']"))
        self.click(self.searchButton)

    def input_inTable(self):
        inputs=self.find_elements(self.input)
        for one in inputs:
            rNum=random.randint(0,100)
            if not one.get_attribute('type')=='hidden':
                one.clear()
                one.send_keys(rNum)


class Module_DutyFill_FirePower_DutyFill_Fill(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_DutyFill_FirePower_DutyFill_Fill,self).__init__(*args,**kwargs)

        self.saveButton=(By.XPATH,"//button[text()='保存']")
        self.submitButton=(By.XPATH,"//button[text()='接班']")
        self.modifyButton=(By.XPATH,"//button[text()='修改']")

        self.input=(By.XPATH,"(//table)[3]//input[@check='number']")
        self.date = (By.XPATH, "//input[@id='startDate']")
        self.time=(By.XPATH,"//select[@id='slot']")

        self.startDate = (By.XPATH, "//input[@id='startDate']")
        self.endDate = (By.XPATH, "//input[@id='endDate']")

        #self.searchButton=(By.XPATH,"//button[text()='查询']")
        #self.searchButton = (By.XPATH, '//*[@id="queryRecord"]/input[2]')
        self.searchButton = (By.XPATH, '//*[@id="MonitorDocuments"]/div[3]/button')

        self.recordTable=(By.XPATH,"//table[@id='recordTable']")

        self.confirmDate=(By.XPATH,"//input[@id='dpOkInput']")

    def is_element_exist(self, selector):
        try:
            self.find_elements(selector)
            return True
        except:
            return False

    def click_submitButton(self):
        self.click(self.submitButton)

    def click_saveButton(self):
        self.click(self.saveButton)

    def click_searchButton(self):
        self.click(self.searchButton)

    def click_modifyButton(self):
        self.click(self.modifyButton)

    def input_date(self,day=0):
        self.js_inputRemoveReadOnly(self.date[1], 'readOnly')
        now = datetime.datetime.now()
        yesterday = now + datetime.timedelta(day)
        strYest = datetime.datetime.strftime(yesterday, '%Y-%m-%d')
        self.type(strYest, self.date)


    def input_startDate(self,day=0):
        self.js_inputRemoveReadOnly(self.startDate[1], 'readOnly')
        now = datetime.datetime.now()
        yesterday = now - datetime.timedelta(day)
        strYest = datetime.datetime.strftime(yesterday, '%Y%m%d')
        self.click(self.startDate)
        self.type(strYest, self.startDate)
        self.switchFrame(self.find_element((By.XPATH,"//iframe[@src='about:blank']")))
        self.click(self.confirmDate)
        self.switchBackFromIframe()



    def input_endDate(self,day=0):
        self.js_inputRemoveReadOnly(self.endDate[1], 'readOnly')
        now = datetime.datetime.now()
        yesterday = now + datetime.timedelta(day)
        strYest = datetime.datetime.strftime(yesterday, '%Y%m%d')
        self.click(self.endDate)
        self.type(strYest, self.endDate)
        self.switchFrame(self.find_element((By.XPATH,"//iframe[@src='about:blank']")))
        self.click(self.confirmDate)
        self.switchBackFromIframe()


    def click_searchFromTime(self,day=0,time=10):
        self.js_inputRemoveReadOnly(self.date[1],'readOnly')
        now=datetime.datetime.now()
        yesterday = now+datetime.timedelta(day)
        strYest=datetime.datetime.strftime(yesterday,'%Y%m%d')
        self.type(strYest,self.date)

        # self.selectByInnerValue(self.time,time)
        self.click((By.XPATH,"//select[@id='slot']"))
        self.click((By.XPATH,"//option[@value='"+str(time)+"']"))
        self.click(self.searchButton)

    def input_inTable(self):
        inputs=self.find_elements(self.input)
        for one in inputs:
            rNum=random.randint(0,100)
            if not one.get_attribute('type')=='hidden':
                one.clear()
                one.send_keys(rNum)

    def resultExistOrNot(self):
        num=self.table_getRowNum(self.recordTable)
        return num




class Module_DutyFill_WaterPower_DutyFill_Fill(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_DutyFill_WaterPower_DutyFill_Fill,self).__init__(*args,**kwargs)

        self.saveButton=(By.XPATH,"//button[text()='保存']")
        self.submitButton=(By.XPATH,"//button[text()='接班']")
        self.modifyButton=(By.XPATH,"//button[text()='修改']")

        self.input=(By.XPATH,"(//table)[3]//input[@check='number']")
       # self.date = (By.XPATH, "//input[@id='date']")
        self.date = (By.XPATH, "//input[@id='dutyTime']")#修改datew
        #self.date=(By.XPATH, "//input[@id='dutyTime']")
        self.time=(By.XPATH,"//select[@id='slot']")

        self.startDate = (By.XPATH, "//input[@id='startDate']")
        self.endDate = (By.XPATH, "//input[@id='endDate']")

        self.searchButton=(By.XPATH,"//button[text()='查询']")

        self.recordTable=(By.XPATH,"//table[@id='recordTable']")

        self.confirmDate=(By.XPATH,"//input[@id='dpOkInput']")

        self.waterpower1=(By.XPATH, "//*[@id='cssmenu']//ul//li[8]//a[text()='水电']")#增加值班填报-说表移动到水电
    def click_waterpower1(self):    #增加值班填报-说表移动到水电
        self.click(self.waterpower1)

    def click_submitButton(self):
        self.click(self.submitButton)

    def click_saveButton(self):
        self.click(self.saveButton)

    def click_searchButton(self):
        self.click(self.searchButton)

    def click_modifyButton(self):
        self.click(self.modifyButton)

    def input_date(self,day=0):
        self.js_inputRemoveReadOnly(self.date[1], 'readonly')#更新readOnly
        now = datetime.datetime.now()
        yesterday = now + datetime.timedelta(day)
        strYest = datetime.datetime.strftime(yesterday, '%Y%m%d')
        self.type(strYest, self.date)


    def input_startDate(self,day=0):
        self.js_inputRemoveReadOnly(self.startDate[1], 'readOnly')
        now = datetime.datetime.now()
        yesterday = now + datetime.timedelta(day)
        strYest = datetime.datetime.strftime(yesterday, '%Y%m%d')
        self.click(self.startDate)
        self.type(strYest, self.startDate)
        self.switchFrame(self.find_element((By.XPATH,"//iframe[@src='about:blank']")))
        self.click(self.confirmDate)
        self.switchBackFromIframe()



    def input_endDate(self,day=0):
        self.js_inputRemoveReadOnly(self.endDate[1], 'readOnly')
        now = datetime.datetime.now()
        yesterday = now + datetime.timedelta(day)
        strYest = datetime.datetime.strftime(yesterday, '%Y%m%d')
        self.click(self.endDate)
        self.type(strYest, self.endDate)
        self.switchFrame(self.find_element((By.XPATH,"//iframe[@src='about:blank']")))
        self.click(self.confirmDate)
        self.switchBackFromIframe()


    def click_searchFromTime(self,day=0,time=10):
        self.js_inputRemoveReadOnly(self.date[1],'readOnly')
        now=datetime.datetime.now()
        yesterday = now+datetime.timedelta(day)
        strYest=datetime.datetime.strftime(yesterday,'%Y%m%d')
        self.type(strYest,self.date)

        # self.selectByInnerValue(self.time,time)
        self.click((By.XPATH,"//select[@id='slot']"))
        self.click((By.XPATH,"//option[@value='"+str(time)+"']"))
        self.click(self.searchButton)

    def input_inTable(self):
        inputs=self.find_elements(self.input)
        for one in inputs:
            rNum=random.randint(0,100)
            if not one.get_attribute('type')=='hidden':
                one.clear()
                one.send_keys(rNum)

    def resultExistOrNot(self):
        num=self.table_getRowNum(self.recordTable)
        return num




class Module_DutyFill_SunPower_DutyFill_Fill(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_DutyFill_SunPower_DutyFill_Fill,self).__init__(*args,**kwargs)

        self.saveButton=(By.XPATH,"//button[text()='保存']")
        self.submitButton=(By.XPATH,"//button[text()='接班']")
        self.modifyButton=(By.XPATH,"//button[text()='修改']")

        self.input=(By.XPATH,"(//table)[3]//input[@check='number']")
        self.date = (By.XPATH, "//input[@id='dutyTime']")
        self.time=(By.XPATH,"//select[@id='slot']")

        self.startDate = (By.XPATH, "//input[@id='startDate']")
        self.endDate = (By.XPATH, "//input[@id='endDate']")

        self.searchButton=(By.XPATH,"//button[text()='查询']")

        self.recordTable=(By.XPATH,"//table[@id='recordTable']")

        self.confirmDate=(By.XPATH,"//input[@id='dpOkInput']")

    def click_submitButton(self):
        self.click(self.submitButton)

    def click_saveButton(self):
        self.click(self.saveButton)

    def click_searchButton(self):
        self.click(self.searchButton)

    def click_modifyButton(self):
        self.click(self.modifyButton)

    def input_date(self,day=0):
        self.js_inputRemoveReadOnly(self.date[1], 'readOnly')
        now = datetime.datetime.now()
        yesterday = now + datetime.timedelta(day)
        strYest = datetime.datetime.strftime(yesterday, '%Y%m%d')
        self.type(strYest, self.date)

    def input_startDate(self,day=0):
        self.js_inputRemoveReadOnly(self.startDate[1], 'readOnly')
        now = datetime.datetime.now()
        yesterday = now + datetime.timedelta(day)
        strYest = datetime.datetime.strftime(yesterday, '%Y%m%d')
        self.click(self.startDate)
        self.type(strYest, self.startDate)
        self.switchFrame(self.find_element((By.XPATH,"//iframe[@src='about:blank']")))
        self.click(self.confirmDate)
        self.switchBackFromIframe()

    def input_endDate(self,day=0):
        self.js_inputRemoveReadOnly(self.endDate[1], 'readOnly')
        now = datetime.datetime.now()
        yesterday = now + datetime.timedelta(day)
        strYest = datetime.datetime.strftime(yesterday, '%Y%m%d')
        self.click(self.endDate)
        self.type(strYest, self.endDate)
        self.switchFrame(self.find_element((By.XPATH,"//iframe[@src='about:blank']")))
        self.click(self.confirmDate)
        self.switchBackFromIframe()

    def click_searchFromTime(self,day=0,time=10):
        self.js_inputRemoveReadOnly(self.date[1],'readOnly')
        now=datetime.datetime.now()
        yesterday = now+datetime.timedelta(day)
        strYest=datetime.datetime.strftime(yesterday,'%Y%m%d')
        self.type(strYest,self.date)

        # self.selectByInnerValue(self.time,time)
        self.click((By.XPATH,"//select[@id='slot']"))
        self.click((By.XPATH,"//option[@value='"+str(time)+"']"))
        self.click(self.searchButton)

    def input_inTable(self):
        inputs=self.find_elements(self.input)
        for one in inputs:
            rNum=random.randint(0,100)
            if not one.get_attribute('type')=='hidden':
                one.clear()
                one.send_keys(rNum)

    def resultExistOrNot(self):
        num=self.table_getRowNum(self.recordTable)
        return num

class Module_DutyFill_CoalPower_DutyFill_Fill(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_DutyFill_CoalPower_DutyFill_Fill,self).__init__(*args,**kwargs)

        self.saveButton=(By.XPATH,"//button[text()='保存']")
        self.submitButton=(By.XPATH,"//button[text()='接班']")
        self.modifyButton=(By.XPATH,"//button[text()='修改']")

        self.input=(By.XPATH,"(//table)[3]//input[@check='number']")
        self.date = (By.XPATH, "//input[@id='dutyTime']")
        self.time=(By.XPATH,"//select[@id='slot']")

        self.startDate = (By.XPATH, "//input[@id='startDate']")
        self.endDate = (By.XPATH, "//input[@id='endDate']")

        self.searchButton=(By.XPATH,"//button[text()='查询']")

        self.recordTable=(By.XPATH,"//table[@id='recordTable']")

        self.confirmDate=(By.XPATH,"//input[@id='dpOkInput']")

    def click_submitButton(self):
        self.click(self.submitButton)

    def click_saveButton(self):
        self.click(self.saveButton)

    def click_searchButton(self):
        self.click(self.searchButton)

    def click_modifyButton(self):
        self.click(self.modifyButton)

    def input_date(self,day=0):
        self.js_inputRemoveReadOnly(self.date[1], 'readOnly')
        now = datetime.datetime.now()
        yesterday = now + datetime.timedelta(day)
        strYest = datetime.datetime.strftime(yesterday, '%Y%m%d')
        self.type(strYest, self.date)

    def input_startDate(self,day=0):
        self.js_inputRemoveReadOnly(self.startDate[1], 'readOnly')
        now = datetime.datetime.now()
        yesterday = now + datetime.timedelta(day)
        strYest = datetime.datetime.strftime(yesterday, '%Y%m%d')
        self.click(self.startDate)
        self.type(strYest, self.startDate)
        self.switchFrame(self.find_element((By.XPATH,"//iframe[@src='about:blank']")))
        self.click(self.confirmDate)
        self.switchBackFromIframe()

    def input_endDate(self,day=0):
        self.js_inputRemoveReadOnly(self.endDate[1], 'readOnly')
        now = datetime.datetime.now()
        yesterday = now + datetime.timedelta(day)
        strYest = datetime.datetime.strftime(yesterday, '%Y%m%d')
        self.click(self.endDate)
        self.type(strYest, self.endDate)
        self.switchFrame(self.find_element((By.XPATH,"//iframe[@src='about:blank']")))
        self.click(self.confirmDate)
        self.switchBackFromIframe()

    def click_searchFromTime(self,day=0,time=10):
        self.js_inputRemoveReadOnly(self.date[1],'readOnly')
        now=datetime.datetime.now()
        yesterday = now+datetime.timedelta(day)
        strYest=datetime.datetime.strftime(yesterday,'%Y%m%d')
        self.type(strYest,self.date)

        # self.selectByInnerValue(self.time,time)
        self.click((By.XPATH,"//select[@id='slot']"))
        self.click((By.XPATH,"//option[@value='"+str(time)+"']"))
        self.click(self.searchButton)

    def input_inTable(self):
        inputs=self.find_elements(self.input)
        for one in inputs:
            rNum=random.randint(0,100)
            if not one.get_attribute('type')=='hidden':
                one.clear()
                one.send_keys(rNum)

    def resultExistOrNot(self):
        num=self.table_getRowNum(self.recordTable)
        return num
