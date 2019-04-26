#coding=utf-8
import datetime
import time

from AutoFramework.core.pom import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random

#数据填报-火电-电量日报
class Module_DataManage_DataFill_FirePower_daily(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_DataManage_DataFill_FirePower_daily,self).__init__(*args,**kwargs)
        #填报
        self.firePowerTree=(By.XPATH,"//span[text()='火电']/../../span[1]")
        self.nayong=(By.XPATH,"//span[text()='火电']/../following-sibling::*//span[text()='纳雍电厂']/../../span")
        self.nayongOneFactory=(By.XPATH,"//span[text()='火电']/../following-sibling::*//span[text()='纳雍电厂']/..//following-sibling::*//span[text()='纳雍一厂']")

        self.saveButton=(By.XPATH,"//input[@value='保存']")
        self.submitButton=(By.XPATH,"//input[@value='提交']")

        self.date=(By.XPATH,"//input[@id='startDate']")
        self.dateConfirm=(By.XPATH,"//input[@id='dpOkInput']")

        self.table=(By.XPATH,"//table[@class='new-table new-table-top'][1]")

        #审核
        self.dateSearchButton=(By.XPATH,"//input[@value='查询']")
        self.verifyButton=(By.XPATH,"//input[@value='审核']")
        #修改
        self.modifyButton = (By.XPATH, "//input[@value='修改']")


    def click_firePowerTree(self):
        self.click(self.firePowerTree)
    def click_nayong(self):
        self.click(self.nayong)
    def click_nayongOneFactory(self):
        self.click(self.nayongOneFactory)
    def click_saveButton(self):
        self.click(self.saveButton)
    def click_submitButton(self):
        self.click(self.submitButton)
    def click_date(self):
        self.click(self.date)
    def click_dateConfirm(self):
        self.click(self.dateConfirm)
    def input_date(self):
        self.js_inputRemoveReadOnly("//input[@id='startDate']","readonly")
        now=datetime.datetime.now()
        preDay=now-datetime.timedelta(days=1)
        self.type(datetime.datetime.strftime(preDay,"%Y-%m-%d"),self.date)

    def input_inTable(self,text):
        self.table_InputInTableByRow(self.table,(By.XPATH,"//td[2]/div/input[2]"),1,text)
    def input_inTable2(self,text):
        self.table_InputInTableByRow(self.table,(By.XPATH,"//td[6]/div/input[2]"),1,text)
    def click_dateSearchButton(self):
        self.click(self.dateSearchButton)
    def click_verifyButton(self):
        self.click(self.verifyButton)
    def click_modifyButton(self):
        self.click(self.modifyButton)


class Module_DataManage_DataFill_FirePower_general(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_DataManage_DataFill_FirePower_general,self).__init__(*args,**kwargs)
        #填报
        self.firePowerTree=(By.XPATH,"//span[text()='火电']/../../span[1]")
        self.nayong=(By.XPATH,"//span[text()='火电']/../following-sibling::*//span[text()='纳雍电厂']/../../span")
        self.nayongOneFactory=(By.XPATH,"//span[text()='火电']/../following-sibling::*//span[text()='纳雍电厂']/..//following-sibling::*//span[text()='纳雍一厂']")

        self.saveButton=(By.XPATH,"//input[@value='保存']")
        self.submitButton=(By.XPATH,"//input[@value='提交']")

        self.date=(By.XPATH,"//input[@id='startDate']")
        self.dateConfirm=(By.XPATH,"//input[@id='dpOkInput']")

        self.table=(By.XPATH,"//table[@class='new-table new-table-top'][1]")

        #审核
        self.dateSearchButton=(By.XPATH,"//input[@value='查询']")
        self.verifyButton=(By.XPATH,"//input[@value='审核']")
        #修改
        self.modifyButton = (By.XPATH, "//input[@value='修改']")


    def click_firePowerTree(self):
        self.click(self.firePowerTree)
    def click_nayong(self):
        self.click(self.nayong)
    def click_nayongOneFactory(self):
        self.click(self.nayongOneFactory)
    def click_saveButton(self):
        self.click(self.saveButton)
    def click_submitButton(self):
        self.click(self.submitButton)
    def click_date(self):
        self.click(self.date)
    def click_dateConfirm(self):
        self.click(self.dateConfirm)
    def input_date(self):
        self.js_inputRemoveReadOnly("//input[@id='startDate']","readonly")
        now=datetime.datetime.now()
        preDay=now-datetime.timedelta(days=1)
        self.type(datetime.datetime.strftime(preDay,"%Y-%m-%d"),self.date)

    def input_inTable(self,text):
        self.table_InputInTableByRow(self.table,(By.XPATH,"//td[3]/div/input[2]"),1,text)
    def input_inTable2(self,text):
        self.table_InputInTableByRow(self.table,(By.XPATH,"//td[4]/div/input[2]"),1,text)
    def click_dateSearchButton(self):
        self.click(self.dateSearchButton)
    def click_verifyButton(self):
        self.click(self.verifyButton)
    def click_modifyButton(self):
        self.click(self.modifyButton)




class Module_DataManage_DataFill_FirePower_coalDaily(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_DataManage_DataFill_FirePower_coalDaily,self).__init__(*args,**kwargs)
        #填报
        self.firePowerTree=(By.XPATH,"//span[text()='火电']/../../span[1]")
        self.nayong=(By.XPATH,"//span[text()='火电']/../following-sibling::*//span[text()='纳雍电厂']/../../span")
        self.nayongOneFactory=(By.XPATH,"//span[text()='火电']/../following-sibling::*//span[text()='纳雍电厂']/..//following-sibling::*//span[text()='纳雍一厂']")

        self.saveButton=(By.XPATH,"//input[@value='保存']")
        self.submitButton=(By.XPATH,"//input[@value='提交']")

        self.date=(By.XPATH,"//input[@id='startDate']")
        self.dateConfirm=(By.XPATH,"//input[@id='dpOkInput']")

        self.table=(By.XPATH,"//table[@class='new-table new-table-top'][1]")

        #审核
        self.dateSearchButton=(By.XPATH,"//input[@value='查询']")
        self.verifyButton=(By.XPATH,"//input[@value='审核']")
        #修改
        self.modifyButton = (By.XPATH, "//input[@value='修改']")


    def click_firePowerTree(self):
        self.click(self.firePowerTree)
    def click_nayong(self):
        self.click(self.nayong)
    def click_nayongOneFactory(self):
        self.click(self.nayongOneFactory)
    def click_saveButton(self):
        self.click(self.saveButton)
    def click_submitButton(self):
        self.click(self.submitButton)
    def click_date(self):
        self.click(self.date)
    def click_dateConfirm(self):
        self.click(self.dateConfirm)
    def input_date(self,day=1):
        self.js_inputRemoveReadOnly("//input[@id='startDate']","readonly")
        now=datetime.datetime.now()
        preDay=now-datetime.timedelta(days=day)
        self.type(datetime.datetime.strftime(preDay,"%Y-%m-%d"),self.date)

    def input_normalCoal3(self,*num):
        a,b,c=num
        self.type(a,(By.XPATH,"//div[text()='正常煤来煤量（吨）：']/../following-sibling::*//input"))
        self.type(b, (By.XPATH, "//div[text()='应急煤耗煤量（吨）：']/../following-sibling::*//input"))
        self.type(c, (By.XPATH, "//div[text()='应急煤存煤量（吨）：']/../following-sibling::*//input"))

    def input_totalCoal4(self,*num):
        a,b,c,d=num
        self.type(a,(By.XPATH,"//div[text()='总来煤量（吨）：']/../following-sibling::*//input"))
        self.type(b, (By.XPATH, "//div[text()='总耗煤量（吨）：']/../following-sibling::*//input"))
        self.type(c, (By.XPATH, "//div[text()='总存煤量（吨）：']/../following-sibling::*//input"))
        self.type(d, (By.XPATH, "//div[text()='预计可用天数：']/../following-sibling::*//input"))

    def click_dateSearchButton(self):
        self.click(self.dateSearchButton)
    def click_verifyButton(self):
        self.click(self.verifyButton)
    def click_modifyButton(self):
        self.click(self.modifyButton)


class Module_DataManage_DataFill_FirePower_coalFill(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_DataManage_DataFill_FirePower_coalFill,self).__init__(*args,**kwargs)
        #填报
        self.firePowerTree=(By.XPATH,"//span[text()='火电']/../../span[1]")
        self.nayong=(By.XPATH,"//span[text()='火电']/../following-sibling::*//span[text()='纳雍电厂']/../../span")
        self.nayongOneFactory=(By.XPATH,"//span[text()='火电']/../following-sibling::*//span[text()='纳雍电厂']/..//following-sibling::*//span[text()='纳雍一厂']")

        self.saveButton=(By.XPATH,"//input[@value='保存']")
        self.submitButton=(By.XPATH,"//input[@value='提交']")

        self.date=(By.XPATH,"//input[@id='startDate']")
        self.dateConfirm=(By.XPATH,"//input[@id='dpOkInput']")

        self.table=(By.XPATH,"//table[@class='new-table new-table-top'][1]")

        #审核
        self.dateSearchButton=(By.XPATH,"//input[@value='查询']")
        self.verifyButton=(By.XPATH,"//input[@value='审核']")
        #修改
        self.modifyButton = (By.XPATH, "//input[@value='修改']")


    def click_firePowerTree(self):
        self.click(self.firePowerTree)
    def click_nayong(self):
        self.click(self.nayong)
    def click_nayongOneFactory(self):
        self.click(self.nayongOneFactory)
    def click_saveButton(self):
        self.click(self.saveButton)
    def click_submitButton(self):
        self.click(self.submitButton)
    def click_date(self):
        self.click(self.date)
    def click_dateConfirm(self):
        self.click(self.dateConfirm)
    def input_date(self,day=1):
        self.js_inputRemoveReadOnly("//input[@id='startDate']","readonly")
        now=datetime.datetime.now()
        preDay=now-datetime.timedelta(days=day)
        self.type(datetime.datetime.strftime(preDay,"%Y-%m-%d"),self.date)

    def input_normalCoal3(self,*num):
        a,b,c=num
        self.type(a,(By.XPATH,"//div[text()='正常煤来煤量（吨）：']/../following-sibling::*//input"))
        self.type(b, (By.XPATH, "//div[text()='应急煤耗煤量（吨）：']/../following-sibling::*//input"))
        self.type(c, (By.XPATH, "//div[text()='应急煤存煤量（吨）：']/../following-sibling::*//input"))

    def input_totalCoal4(self,*num):
        a,b,c,d=num
        self.type(a,(By.XPATH,"//div[text()='总来煤量（吨）：']/../following-sibling::*//input"))
        self.type(b, (By.XPATH, "//div[text()='总耗煤量（吨）：']/../following-sibling::*//input"))
        self.type(c, (By.XPATH, "//div[text()='总存煤量（吨）：']/../following-sibling::*//input"))
        self.type(d, (By.XPATH, "//div[text()='预计可用天数：']/../following-sibling::*//input"))

    def click_dateSearchButton(self):
        self.click(self.dateSearchButton)
    def click_verifyButton(self):
        self.click(self.verifyButton)
    def click_modifyButton(self):
        self.click(self.modifyButton)


class Module_DataManage_DataFill_FirePower_GroupStatusFill(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_DataManage_DataFill_FirePower_GroupStatusFill,self).__init__(*args,**kwargs)
        #填报
        self.firePowerTree=(By.XPATH,"//span[text()='火电']/../../span[1]")
        self.nayong=(By.XPATH,"//span[text()='火电']/../following-sibling::*//span[text()='纳雍电厂']/../../span")
        self.nayongOneFactory=(By.XPATH,"//span[text()='火电']/../following-sibling::*//span[text()='纳雍电厂']/..//following-sibling::*//span[text()='纳雍一厂']/../../span")
        self.groupOne=(By.XPATH,"//span[text()='火电']/../following-sibling::*//span[text()='纳雍电厂']/..//following-sibling::*//span[text()='纳雍一厂']/..//following-sibling::*//span[text()='#1机组']")

        self.saveButton=(By.XPATH,"//button[text()='保存']")
        self.submitButton=(By.XPATH,"//button[text()='提交']")

        # self.table=(By.XPATH,"//table[@class='new-table new-table-top'][1]")

        self.reporter=(By.XPATH,"//label[text()='报告人:']/following-sibling::*//input")
        self.reportTime=(By.XPATH,"//label[text()='报告时间:']/following-sibling::*//input")
        self.oldStatus=(By.XPATH,"//label[text()='原状态:']/following-sibling::*//select")
        self.afterStatus=(By.XPATH,"//label[text()='变更后状态:']/following-sibling::*//select")
        self.brifReason=(By.XPATH,"//label[text()='简要原因:']/following-sibling::*//select")
        self.changeType=(By.XPATH,"//label[text()='变更类型:']/following-sibling::*//select")
        self.whetherNonStop=(By.XPATH,"//input[@name='whetherNonStop']/following-sibling::*/i")
        self.whetherReport=(By.XPATH,"//input[@name='whetherReport']/following-sibling::*/i")

        self.lastStateTime=(By.XPATH,"//label[text()='原状态开始时间:']/following-sibling::*//input")
        self.changeTime=(By.XPATH,"//label[text()='变更时间:']/following-sibling::*//input")
        self.expectedEndTime=(By.XPATH,"//label[text()='预计结束时间:']/following-sibling::*//input")

        self.reason=(By.XPATH,"//textarea[@name='reason']")
        self.depict=(By.XPATH,"//textarea[@name='depict']")
        self.render=(By.XPATH,"//textarea[@name='render']")

        self.title=(By.XPATH,"//h1[@id='titileNa']")
        self.timeConfirm=(By.XPATH,"//span[text()='确定']")



    def click_firePowerTree(self):
        self.click(self.firePowerTree)
    def click_nayong(self):
        self.click(self.nayong)
    def click_nayongOneFactory(self):
        self.click(self.nayongOneFactory)
    def click_groupOne(self):
        self.click(self.groupOne)
    def click_saveButton(self):
        self.click(self.saveButton)
    def click_submitButton(self):
        self.click(self.submitButton)



    def click_reporter(self):
        self.click(self.reporter)
    def click_reportTime(self):
        self.click(self.reportTime)
    def click_oldStatus(self):
        self.click((By.XPATH,"//label[text()='原状态:']/following-sibling::*//input"))
        self.click((By.XPATH,"//label[text()='原状态:']/following-sibling::*//dd[text()='并网']"))
    def click_afterStatus(self):
        self.click((By.XPATH,"//label[text()='变更后状态:']/following-sibling::*//input"))
        self.click((By.XPATH,"//label[text()='变更后状态:']/following-sibling::*//dd[text()='停运']"))
    def click_brifReason(self):
        self.click((By.XPATH,"//label[text()='简要原因:']/following-sibling::*//input"))
        self.click((By.XPATH,"//label[text()='简要原因:']/following-sibling::*//dd[text()='锅炉-熄火']"))
    def click_changeType(self):
        self.click((By.XPATH,"//label[text()='变更类型:']/following-sibling::*//input"))
        self.click((By.XPATH,"//label[text()='变更类型:']/following-sibling::*//dd[text()='二类故障']"))
    def click_whetherNonStop(self):
        self.click(self.whetherNonStop)
    def click_whetherReport(self):
        self.click(self.whetherReport)
    def click_lastStateTime(self):
        self.click(self.lastStateTime)
    def click_changeTime(self):
        self.click(self.changeTime)
    def click_expectedEndTime(self):
        self.click(self.expectedEndTime)
    def click_reason(self):
        self.click(self.reason)
    def click_depict(self):
        self.click(self.depict)
    def click_render(self):
        self.click(self.render)


    def input_reporter(self, value):
        self.typeWithOutClear(value, self.reporter)
    def input_reportTime(self,day=0):
        # self.js_inputRemoveReadOnly("//input[@id='startDate']","readonly")
        now=datetime.datetime.now()
        preDay=now-datetime.timedelta(days=day)
        self.typeWithOutClear(datetime.datetime.strftime(preDay,"%Y-%m-%d"),self.reportTime)
        self.click(self.title)
    def input_oldStatus(self, value):
        # self.js_inputRemoveReadOnly("//label[text()='原状态:']/following-sibling::*//input", "readonly")
        self.selectByText( self.oldStatus,value)
    def input_afterStatus(self, value):
        # self.js_inputRemoveReadOnly("//label[text()='变更后状态:']/following-sibling::*//input", "readonly")
        self.selectByText( self.afterStatus,value)
    def input_brifReason(self, value):
        # self.js_inputRemoveReadOnly("//label[text()='简要原因:']/following-sibling::*//input", "readonly")
        self.selectByText( self.brifReason,value)
    def input_changeType(self, value):
        # self.js_inputRemoveReadOnly("//label[text()='变更类型:']/following-sibling::*//input", "readonly")
        self.selectByText( self.changeType,value)
    def input_whetherNonStop(self, value):
        self.typeWithOutClear(value, self.whetherNonStop)
    def input_whetherReport(self, value):
        self.typeWithOutClear(value, self.whetherReport)
    def input_lastStateTime(self,day=1):
        # self.js_inputRemoveReadOnly("//input[@id='startDate']","readonly")
        now=datetime.datetime.now()
        preDay=now-datetime.timedelta(days=day)
        self.typeWithOutClear(datetime.datetime.strftime(preDay,"%Y-%m-%d"),self.lastStateTime)
        # self.click(self.title)
        self.click(self.timeConfirm)
        time.sleep(1)
    def input_changeTime(self,day=0):
        # self.js_inputRemoveReadOnly("//input[@id='startDate']","readonly")
        now=datetime.datetime.now()
        preDay=now-datetime.timedelta(days=day)
        self.typeWithOutClear(datetime.datetime.strftime(preDay,"%Y-%m-%d"),self.changeTime)
        # self.click(self.title)
        self.click(self.timeConfirm)
        time.sleep(1)
    def input_expectedEndTime(self,day=-1):
        # self.js_inputRemoveReadOnly("//input[@id='startDate']","readonly")
        now=datetime.datetime.now()
        preDay=now-datetime.timedelta(days=day)
        self.typeWithOutClear(datetime.datetime.strftime(preDay,"%Y-%m-%d"),self.expectedEndTime)
        # self.click(self.title)
        self.click(self.timeConfirm)
        time.sleep(1)
    def input_reason(self, value):
        self.typeWithOutClear(value, self.reason)
    def input_depict(self, value):
        self.typeWithOutClear(value, self.depict)
    def input_render(self, value):
        self.typeWithOutClear(value, self.render)



class Module_DataManage_DataFill_WaterPower_Fill_groupStatus_Fill(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_DataManage_DataFill_WaterPower_Fill_groupStatus_Fill,self).__init__(*args,**kwargs)
        #填报
        self.waterPowerTree=(By.XPATH,"//span[text()='水电']/../../span[1]")
        self.anshun=(By.XPATH,"//span[text()='水电']/../following-sibling::*//span[text()='安顺中心站']/../../span")
        self.luFanFactory=(By.XPATH,"//span[text()='水电']/../following-sibling::*//span[text()='安顺中心站']/..//following-sibling::*//span[text()='洛凡水电站']")

        self.submitButton=(By.XPATH,"//button[text()='提交']")

        self.date=(By.XPATH,"//input[@id='startDate']")
        self.dateConfirm=(By.XPATH,"//input[@id='dpOkInput']")

        self.table=(By.XPATH,"//table[@class='new-table new-table-top'][1]")
        self.groupStats1=(By.XPATH,"//select[@name='JYAS001030012']")
        self.groupStats2 = (By.XPATH, "//select[@name='JYAS001030022']")
        self.groupStats3 = (By.XPATH, "//select[@name='JYAS001030032']")
        self.groupDate1=(By.XPATH,"//input[@name='JYAS001030013']")
        self.groupDate2 = (By.XPATH, "//input[@name='JYAS001030023']")
        self.groupDate3 = (By.XPATH, "//input[@name='JYAS001030033']")

    def click_waterPowerTree(self):
        self.click(self.waterPowerTree)
    def click_anshun(self):
        self.click(self.anshun)
    def click_luFanFactory(self):
        self.click(self.luFanFactory)
    def click_submitButton(self):
        self.click(self.submitButton)
    def click_date(self):
        self.click(self.date)
    def click_dateConfirm(self):
        self.click(self.dateConfirm)
    def click_table(self):
        self.click(self.table)
    def click_groupStats1(self):
        self.click(self.groupStats1)
    def click_groupStats2(self):
        self.click(self.groupStats2)
    def click_groupStats3(self):
        self.click(self.groupStats3)
    def click_groupDate1(self):
        self.click(self.groupDate1)
    def click_groupDate2(self):
        self.click(self.groupDate2)
    def click_groupDate3(self):
        self.click(self.groupDate3)

    def input_groupDate1(self):
        # self.js_inputRemoveReadOnly(self.groupDate1[1],"readonly")
        # now=datetime.datetime.now()
        # preDay=now-datetime.timedelta(days=1)
        # self.type(now,self.groupDate1)

        self.click((By.XPATH,"//input[@value='确定']"))
    def input_groupDate2(self,value):
        # self.js_inputRemoveReadOnly(self.groupDate2[1],"readonly")
        now=datetime.datetime.now()
        preDay=now-datetime.timedelta(days=1)
        self.type(now,self.groupDate2)
    def input_groupDate3(self,value):
        # self.js_inputRemoveReadOnly(self.groupDate3[1],"readonly")
        now=datetime.datetime.now()
        preDay=now-datetime.timedelta(days=1)
        self.type(now,self.groupDate3)

    def select_groupStats1(self,value):
        self.selectByText(self.groupStats1,value)
    def select_groupStats2(self,value):
        self.selectByText(self.groupStats2,value)
    def select_groupStats3(self,value):
        self.selectByText(self.groupStats3,value)

class Module_DataManage_DataFill_WaterPower_Fill_readNum_Fill(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_DataManage_DataFill_WaterPower_Fill_readNum_Fill,self).__init__(*args,**kwargs)
        #填报
        self.waterPowerTree=(By.XPATH,"//span[text()='水电']/../../span[1]")
        self.anshun=(By.XPATH,"//span[text()='水电']/../following-sibling::*//span[text()='安顺中心站']/../../span")
        self.luFanFactory=(By.XPATH,"//span[text()='水电']/../following-sibling::*//span[text()='安顺中心站']/..//following-sibling::*//span[text()='洛凡水电站']")

        self.saveButton=(By.XPATH,"//input[@value='保存']")
        self.submitButton=(By.XPATH,"//input[@value='提交']")

        self.dailyGeneratePower=(By.XPATH,"//div[text()='所有机组电量之和']/../following-sibling::*//input[@name='rfdl']")

        self.verifyButton=(By.XPATH,"//input[@value='审核']")

        self.modifyButton=(By.XPATH,"//input[@value='修改']")

        self.time=(By.XPATH,"//input[@name='time']")

        self.searchButton=(By.XPATH,"//input[@value='查询']")

    def click_waterPowerTree(self):
        self.click(self.waterPowerTree)
    def click_anshun(self):
        self.click(self.anshun)
    def click_luFanFactory(self):
        self.click(self.luFanFactory)
    def click_submitButton(self):
        self.click(self.submitButton)
    def click_saveButton(self):
        self.click(self.saveButton)
    def input_dailyGeneratePower(self,value):
        self.type(value,self.dailyGeneratePower)
    def click_verifyButton(self):
        self.click(self.verifyButton)
    def click_modifyButton(self):
        self.click(self.modifyButton)

    def input_time(self,day=1):
        self.js_inputRemoveReadOnly(self.time[1],'readOnly')
        now=datetime.datetime.now()
        preDay=now-datetime.timedelta(days=day)
        self.type(preDay,self.time)

    def click_searchButton(self):
        self.click(self.searchButton)

class Module_DataManage_DataFill_WaterPower_Fill_anualPlan_Fill(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_DataManage_DataFill_WaterPower_Fill_anualPlan_Fill,self).__init__(*args,**kwargs)
        #填报
        self.waterPowerTree=(By.XPATH,"//span[text()='水电']/../../span[1]")
        self.anshun=(By.XPATH,"//span[text()='水电']/../following-sibling::*//span[text()='安顺中心站']/../../span")
        self.luFanFactory=(By.XPATH,"//span[text()='水电']/../following-sibling::*//span[text()='安顺中心站']/..//following-sibling::*//span[text()='洛凡水电站']")

        self.saveButton=(By.XPATH,"//button[text()='保存']")
        self.submitButton=(By.XPATH,"//button[text()='提交']")

        self.JanFill=(By.XPATH,"//div[text()='发电量']/../..//td[2]/div/input")


        self.dailyGeneratePower=(By.XPATH,"//div[text()='所有机组电量之和']/../following-sibling::*//input[@name='rfdl']")

        self.verifyButton=(By.XPATH,"//input[@value='审核']")

        self.modifyButton=(By.XPATH,"//button[text()='修改']")

        self.time=(By.XPATH,"//input[@name='time']")

        self.searchButton=(By.XPATH,"//input[@value='查询']")

    def click_waterPowerTree(self):
        self.click(self.waterPowerTree)
    def click_anshun(self):
        self.click(self.anshun)
    def click_luFanFactory(self):
        self.click(self.luFanFactory)
    def click_submitButton(self):
        self.click(self.submitButton)
    def click_saveButton(self):
        self.click(self.saveButton)
    def input_JanFill(self,value):
        self.type(value,self.JanFill)
    def click_verifyButton(self):
        self.click(self.verifyButton)
    def click_modifyButton(self):
        self.click(self.modifyButton)

    def input_time(self,day=1):
        self.js_inputRemoveReadOnly(self.time[1],'readOnly')
        now=datetime.datetime.now()
        preDay=now-datetime.timedelta(days=day)
        self.type(preDay,self.time)

    def click_searchButton(self):
        self.click(self.searchButton)


class Module_DataManage_DataFill_SumPower_Fill(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_DataManage_DataFill_SumPower_Fill,self).__init__(*args,**kwargs)
        #填报
        self.sumPowerTree=(By.XPATH,"//span[text()='光伏']/../../span[1]")
        self.weiNing=(By.XPATH,"//span[text()='光伏']/../following-sibling::*//span[text()='威宁新能源']/../../span")
        self.PingQing=(By.XPATH,"//span[text()='光伏']/../following-sibling::*//span[text()='威宁新能源']/..//following-sibling::*//span[text()='平菁光伏电站']")

        self.saveButton=(By.XPATH,"//button[text()='保存']")
        self.submitButton=(By.XPATH,"//button[text()='提交']")

        self.modifyValue=(By.XPATH,"//input[@id='powerGenertion']")

        self.table=(By.XPATH,"//table[@id='tableNew']")
        self.input=(By.XPATH,"//div/input")


        # self.dailyGeneratePower=(By.XPATH,"//div[text()='所有机组电量之和']/../following-sibling::*//input[@name='rfdl']")
        #
        # self.verifyButton=(By.XPATH,"//input[@value='审核']")
        #
        # self.modifyButton=(By.XPATH,"//button[text()='修改']")
        #
        self.time=(By.XPATH,"//input[@id='startDate']")
        #
        self.searchButton=(By.XPATH,"//input[@value='查询']")

        self.veirfyButton = (By.XPATH, "//button[text()='审核']")

    def click_sumPowerTree(self):
        self.click(self.sumPowerTree)
    def click_weiNing(self):
        self.click(self.weiNing)
    def click_PingQing(self):
        self.click(self.PingQing)
    def click_submitButton(self):
        self.click(self.submitButton)
    def click_saveButton(self):
        self.click(self.saveButton)
    def click_verifyButton(self):
        self.click(self.veirfyButton)

    def input_time(self,day=1):
        self.js_inputRemoveReadOnly(self.time[1],'readOnly')
        now=datetime.datetime.now()
        preDay=now-datetime.timedelta(days=day)
        # strDay=datetime.datetime.strftime(preDay)
        self.type(preDay.strftime('%Y-%m-%d'),self.time)

    def click_searchButton(self):
        self.click(self.searchButton)


    def input_inTable(self):
        targets=(By.XPATH,"//table[@id='tableNew']//div/input")
        targetsOjb=self.find_elements(targets)
        for one in targetsOjb:
            if "readonly"==one.get_attribute("readonly"):
                print("abc")
                continue
            else:
                one.send_keys(random.randint(1,100))

    def input_modifyData(self,value):
        self.type(Keys.BACKSPACE,self.modifyValue)
        self.type(value,self.modifyValue)

class Module_DataManage_DataFill_SumPower_anual_Fill(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_DataManage_DataFill_SumPower_anual_Fill,self).__init__(*args,**kwargs)
        #填报
        self.sumPowerTree=(By.XPATH,"//span[text()='光伏']/../../span[1]")
        self.weiNing=(By.XPATH,"//span[text()='光伏']/../following-sibling::*//span[text()='威宁新能源']/../../span")
        self.PingQing=(By.XPATH,"//span[text()='光伏']/../following-sibling::*//span[text()='威宁新能源']/..//following-sibling::*//span[text()='平菁光伏电站']")

        self.saveButton=(By.XPATH,"//button[text()='保存']")
        self.submitButton=(By.XPATH,"//button[text()='提交']")

        self.modifyValue=(By.XPATH,"//input[@id='powerGenertion']")

        self.table=(By.XPATH,"//table[@id='tableNew']")
        self.input=(By.XPATH,"//div/input")


        # self.dailyGeneratePower=(By.XPATH,"//div[text()='所有机组电量之和']/../following-sibling::*//input[@name='rfdl']")
        #
        # self.verifyButton=(By.XPATH,"//input[@value='审核']")
        #
        self.modifyButton=(By.XPATH,"//button[text()='修改']")
        #
        self.time=(By.XPATH,"//input[@id='startDate']")
        #
        self.searchButton=(By.XPATH,"//input[@value='查询']")

        self.veirfyButton = (By.XPATH, "//button[text()='审核']")

    def click_sumPowerTree(self):
        self.click(self.sumPowerTree)
    def click_weiNing(self):
        self.click(self.weiNing)
    def click_PingQing(self):
        self.click(self.PingQing)
    def click_submitButton(self):
        self.click(self.submitButton)
    def click_saveButton(self):
        self.click(self.saveButton)
    def click_verifyButton(self):
        self.click(self.veirfyButton)

    def input_time(self,day=1):
        self.js_inputRemoveReadOnly(self.time[1],'readOnly')
        now=datetime.datetime.now()
        preDay=now-datetime.timedelta(days=day)
        # strDay=datetime.datetime.strftime(preDay)
        self.type(preDay.strftime('%Y-%m-%d'),self.time)

    def click_searchButton(self):
        self.click(self.searchButton)


    def input_inTable(self,num1,num2):
        # targets=(By.XPATH,"//table[@class='new-table']//following-sibling::*//input")
        # targetsOjb=self.find_elements(targets)
        # for one in targetsOjb:
        #     if "readonly"!=one.get_attribute("readonly"):
        #         one.click()
        #         one.send_keys(random.randint(1,100))
        self.type(num1,(By.XPATH,"//input[@name='powerGeneration1']"))
        self.type(num2, (By.XPATH, "//input[@name='powerGeneration2']"))

    def input_modifyData(self,value):
        # self.type(Keys.BACKSPACE,self.modifyValue)
        self.type(value,self.modifyValue)

    def click_modifyButton(self):
        self.click(self.modifyButton)


class Module_DataManage_DataFill_Coal_Daily_Fill(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_DataManage_DataFill_Coal_Daily_Fill,self).__init__(*args,**kwargs)
        #填报
        self.coalPowerTree=(By.XPATH,"//span[text()='煤矿']/../../span[1]")
        self.linHua=(By.XPATH,"//span[text()='煤矿']/../following-sibling::*//span[text()='林华煤矿']")
        # self.PingQing=(By.XPATH,"//span[text()='光伏']/../following-sibling::*//span[text()='威宁新能源']/..//following-sibling::*//span[text()='平菁光伏电站']")

        self.saveButton=(By.XPATH,"//button[text()='保存']")
        self.submitButton=(By.XPATH,"//button[text()='提交']")

        self.modifyValue=(By.XPATH,"//input[@id='powerGenertion']")

        self.table=(By.XPATH,"//table[@id='tableNew']")
        self.input=(By.XPATH,"//div/input")



        # self.dailyGeneratePower=(By.XPATH,"//div[text()='所有机组电量之和']/../following-sibling::*//input[@name='rfdl']")
        #
        # self.verifyButton=(By.XPATH,"//input[@value='审核']")
        #
        self.modifyButton=(By.XPATH,"//button[text()='修改']")
        #
        self.time=(By.XPATH,"//input[@id='startDate']")
        #
        self.searchButton=(By.XPATH,"//input[@value='查询']")

        self.veirfyButton = (By.XPATH, "//button[text()='审核']")
        self.no_data_tip=("xpath",'//*[@id="tiptitle"]')

    def click_coalPowerTree(self):
        self.click(self.coalPowerTree)
    def click_linHua(self):
        self.click(self.linHua)

    def click_submitButton(self):
        self.click(self.submitButton)
    def click_saveButton(self):
        self.click(self.saveButton)
    def click_verifyButton(self):
        self.click(self.veirfyButton)

    def input_time(self,day=1):
        self.js_inputRemoveReadOnly(self.time[1],'readOnly')
        now=datetime.datetime.now()
        preDay=now-datetime.timedelta(days=day)
        # strDay=datetime.datetime.strftime(preDay)
        self.type(preDay.strftime('%Y-%m-%d'),self.time)

    def click_searchButton(self):
        self.click(self.searchButton)


    def input_inTable(self,num1,num2,num3,num4,num5):
        # targets=(By.XPATH,"//table[@class='new-table']//following-sibling::*//input")
        # targetsOjb=self.find_elements(targets)
        # for one in targetsOjb:
        #     if "readonly"!=one.get_attribute("readonly"):
        #         one.click()
        #         one.send_keys(random.randint(1,100))
        self.GenerateCoalQuality=(By.XPATH,"//td/*[text()='产煤量(吨):']/../following-sibling::*//input")
        self.sellCoalQuality=(By.XPATH,"//td/*[text()='总销量(吨):']/../following-sibling::*//input")
        self.storageQuantity=(By.XPATH,"//td/*[text()='库存量(吨):']/../following-sibling::*//input")
        self.produceMeter=(By.XPATH,"//td/*[text()='生产进尺(米):']/../following-sibling::*//input")
        self.buildMeter=(By.XPATH,"//td/*[text()='建设进尺(米):']/../following-sibling::*//input")

        self.type(num1,self.GenerateCoalQuality)
        self.type(num2, self.sellCoalQuality)
        self.type(num3,self.produceMeter)
        self.type(num4,self.buildMeter)
        self.type(num5,self.storageQuantity)

    def input_modifyData(self,value):
        # self.type(Keys.BACKSPACE,self.modifyValue)
        self.type(value,self.modifyValue)

    def click_modifyButton(self):
        self.click(self.modifyButton)

    def is_element_exist(self, selector):
        try:
            self.find_element(selector)
            return True
        except:
            return False

class Module_DataManage_DataFill_Coal_Anual_Fill(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_DataManage_DataFill_Coal_Anual_Fill,self).__init__(*args,**kwargs)
        #填报
        self.coalPowerTree=(By.XPATH,"//span[text()='煤矿']/../../span[1]")
        self.linHua=(By.XPATH,"//span[text()='煤矿']/../following-sibling::*//span[text()='林华煤矿']")
        # self.PingQing=(By.XPATH,"//span[text()='光伏']/../following-sibling::*//span[text()='威宁新能源']/..//following-sibling::*//span[text()='平菁光伏电站']")

        self.saveButton=(By.XPATH,"//button[text()='保存']")
        self.submitButton=(By.XPATH,"//button[text()='提交']")

        self.modifyValue=(By.XPATH,"//input[@id='powerGenertion']")

        self.table=(By.XPATH,"//table[@id='tableNew']")
        self.input=(By.XPATH,"//div/input")


        # self.dailyGeneratePower=(By.XPATH,"//div[text()='所有机组电量之和']/../following-sibling::*//input[@name='rfdl']")
        #
        # self.verifyButton=(By.XPATH,"//input[@value='审核']")
        #
        self.modifyButton=(By.XPATH,"//button[text()='修改']")
        #
        self.time=(By.XPATH,"//input[@id='startDate']")
        #
        self.searchButton=(By.XPATH,"//input[@value='查询']")

        self.veirfyButton = (By.XPATH, "//button[text()='审核']")

    def click_coalPowerTree(self):
        self.click(self.coalPowerTree)
    def click_linHua(self):
        self.click(self.linHua)

    def click_submitButton(self):
        self.click(self.submitButton)
    def click_saveButton(self):
        self.click(self.saveButton)
    def click_verifyButton(self):
        self.click(self.veirfyButton)

    def input_time(self,day=1):
        self.js_inputRemoveReadOnly(self.time[1],'readOnly')
        now=datetime.datetime.now()
        preDay=now-datetime.timedelta(days=day)
        # strDay=datetime.datetime.strftime(preDay)
        self.type(preDay.strftime('%Y-%m-%d'),self.time)

    def click_searchButton(self):
        self.click(self.searchButton)


    def input_inTable(self):
        targets=(By.XPATH,"//table[@class='new-table']/tbody//following-sibling::*//input")
        targetsOjb=self.find_elements(targets)
        for one in targetsOjb:
            if "readonly"!=one.get_attribute("readonly"):
                one.click()
                one.send_keys(random.randint(1,100))


    def input_modifyData(self,value):
        # self.type(Keys.BACKSPACE,self.modifyValue)
        self.type(value,self.modifyValue)

    def click_modifyButton(self):
        self.click(self.modifyButton)


class Module_DataManage_DataFill_Gas_Daily_Fill(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_DataManage_DataFill_Gas_Daily_Fill,self).__init__(*args,**kwargs)
        #填报
        self.coalPowerTree=(By.XPATH,"//span[text()='煤矿']/../../span[1]")
        self.linHua=(By.XPATH,"//span[text()='煤矿']/../following-sibling::*//span[text()='林华煤矿']")
        # self.PingQing=(By.XPATH,"//span[text()='光伏']/../following-sibling::*//span[text()='威宁新能源']/..//following-sibling::*//span[text()='平菁光伏电站']")

        self.saveButton=(By.XPATH,"//button[text()='保存']")
        self.submitButton=(By.XPATH,"//button[text()='提交']")

        self.modifyValue=(By.XPATH,"//input[@id='powerGenertion']")

        self.table=(By.XPATH,"//table[@id='tableNew']")
        self.input=(By.XPATH,"//div/input")


        # self.dailyGeneratePower=(By.XPATH,"//div[text()='所有机组电量之和']/../following-sibling::*//input[@name='rfdl']")
        #
        # self.verifyButton=(By.XPATH,"//input[@value='审核']")
        #
        self.modifyButton=(By.XPATH,"//button[text()='修改']")
        #
        self.time=(By.XPATH,"//input[@id='startDate']")
        #
        self.searchButton=(By.XPATH,"//input[@value='查询']")

        self.veirfyButton = (By.XPATH, "//button[text()='审核']")

    def click_coalPowerTree(self):
        self.click(self.coalPowerTree)
    def click_linHua(self):
        self.click(self.linHua)

    def click_submitButton(self):
        self.click(self.submitButton)
    def click_saveButton(self):
        self.click(self.saveButton)
    def click_verifyButton(self):
        self.click(self.veirfyButton)

    def input_time(self,day=1):
        self.js_inputRemoveReadOnly(self.time[1],'readOnly')
        now=datetime.datetime.now()
        preDay=now-datetime.timedelta(days=day)
        # strDay=datetime.datetime.strftime(preDay)
        self.type(preDay.strftime('%Y-%m-%d'),self.time)

    def click_searchButton(self):
        self.click(self.searchButton)


    def input_inTable(self,num1,num2):
        self.gasGenerate=(By.XPATH,"//td/*[text()='瓦斯发电量(万kW.h):']/../following-sibling::*//input")
        self.gasSell=(By.XPATH,"//td/*[text()='瓦斯售电量(万kW.h):']/../following-sibling::*//input")

        self.type(num1,self.gasGenerate)
        self.type(num2, self.gasSell)

    def input_modifyData(self,value):
        # self.type(Keys.BACKSPACE,self.modifyValue)
        self.type(value,self.modifyValue)

    def click_modifyButton(self):
        self.click(self.modifyButton)


class Module_DataManage_DataFill_General_Daily_Fill(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_DataManage_DataFill_General_Daily_Fill,self).__init__(*args,**kwargs)
        #填报
        self.GeneralTree=(By.XPATH,"//span[text()='综合产业']/../../span[1]")
        self.suiYang=(By.XPATH,"//span[text()='综合产业']/../following-sibling::*//span[text()='绥阳化工']")
        # self.PingQing=(By.XPATH,"//span[text()='光伏']/../following-sibling::*//span[text()='威宁新能源']/..//following-sibling::*//span[text()='平菁光伏电站']")

        self.saveButton=(By.XPATH,"//input[@value='保存']")
        self.submitButton=(By.XPATH,"//input[@value='提交']")

        self.modifyValue=(By.XPATH,"//input[@id='powerGenertion']")

        self.table=(By.XPATH,"//table[@id='tableNew']")
        self.input=(By.XPATH,"//div/input")
        self.tip=("id","tiptitle") #打开修改页面查询无数据时提示信息的元素


        # self.dailyGeneratePower=(By.XPATH,"//div[text()='所有机组电量之和']/../following-sibling::*//input[@name='rfdl']")
        #
        # self.verifyButton=(By.XPATH,"//input[@value='审核']")
        #
        self.modifyButton=(By.XPATH,"//input[@value='修改']")
        #
        self.time=(By.XPATH,"//input[@id='startDate']")
        #
        self.searchButton=(By.XPATH,"//input[@value='查询']")

        self.veirfyButton = (By.XPATH, "//input[@value='审核']")

    def is_element_exist(self,selector):
       try:
           self.find_element(selector)
           return True
       except:
           return False


    def click_GeneralTree(self):
        self.click(self.GeneralTree)
    def click_suiYang(self):
        self.click(self.suiYang)

    def click_submitButton(self):
        self.click(self.submitButton)
        #self.click((By.XPATH, "//span[text()='Ok']"))
    def click_saveButton(self):
        self.click(self.saveButton)
        #self.click((By.XPATH,"//span[text()='Ok']"))
    def click_verifyButton(self):
        self.click(self.veirfyButton)
        #self.click((By.XPATH, "//span[text()='Ok']"))

    def input_time(self,day=1):
        self.js_inputRemoveReadOnly(self.time[1],'readOnly')
        now=datetime.datetime.now()
        preDay=now-datetime.timedelta(days=day)
        # strDay=datetime.datetime.strftime(preDay)
        self.type(preDay.strftime('%Y-%m-%d'),self.time)

    def click_searchButton(self):
        self.click(self.searchButton)


    def input_inTable(self,num1=5,num2=5,num3=5,num4=5):
        self.gasGenerate=(By.XPATH,"//div[text()='销售价格(含税)(元/吨)：']/../following-sibling::*//input[@name='saleprice']")
        self.gasSell=(By.XPATH,"//div[text()='P·O52.5：']/../following-sibling::*//input[@name='sp0525']")
        self.gasPrice=(By.XPATH,"//div[text()='P·C32.5R(包)(元/吨)：']/../following-sibling::*//input")
        self.gasPrice2=(By.XPATH,"//div[text()='P·O42.5(包)(元/吨):']/../following-sibling::*//input")

        self.type(num1,self.gasGenerate)
        self.type(num2, self.gasSell)
        self.type(num3,self.gasPrice)
        self.type(num4,self.gasPrice2)

    def input_modifyData(self,value):
        # self.type(Keys.BACKSPACE,self.modifyValue)
        self.type(value,self.modifyValue)

    def click_modifyButton(self):
        self.click(self.modifyButton)
        #self.click((By.XPATH, "//span[text()='Ok']"))

class Module_DataManage_DataFill_General_Anual_Fill(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_DataManage_DataFill_General_Anual_Fill,self).__init__(*args,**kwargs)
        #填报
        self.GeneralTree=(By.XPATH,"//span[text()='综合产业']/../../span[1]")
        self.suiYang=(By.XPATH,"//span[text()='综合产业']/../following-sibling::*//span[text()='绥阳化工']")
        # self.PingQing=(By.XPATH,"//span[text()='光伏']/../following-sibling::*//span[text()='威宁新能源']/..//following-sibling::*//span[text()='平菁光伏电站']")

        self.saveButton=(By.XPATH,"//button[text()='保存']")
        self.submitButton=(By.XPATH,"//button[text()='提交']")

        self.modifyValue=(By.XPATH,"//button[text()='修改']")

        self.table=(By.XPATH,"//table[@id='tableNew']")
        self.input=(By.XPATH,"//div/input")


        # self.dailyGeneratePower=(By.XPATH,"//div[text()='所有机组电量之和']/../following-sibling::*//input[@name='rfdl']")
        #
        # self.verifyButton=(By.XPATH,"//input[@value='审核']")
        #
        self.modifyButton=(By.XPATH,"//button[text()='修改']")
        #
        self.time=(By.XPATH,"//input[@id='startDate']")
        #
        self.searchButton=(By.XPATH,"//input[@value='查询']")

        self.veirfyButton = (By.XPATH, "//input[@value='审核']")

    def click_GeneralTree(self):
        self.click(self.GeneralTree)
    def click_suiYang(self):
        self.click(self.suiYang)

    def click_submitButton(self):
        self.click(self.submitButton)
    def click_saveButton(self):
        self.click(self.saveButton)
    def click_verifyButton(self):
        self.click(self.veirfyButton)
        self.click((By.XPATH, "//span[text()='Ok']"))

    def input_year(self,y=0):
        self.js_inputRemoveReadOnly(self.time[1],'readOnly')
        now=datetime.datetime.now()
        curYear=str(now.strftime('%Y'))
        year=int(curYear)+y
        self.type(year,self.time)

    def click_searchButton(self):
        self.click(self.searchButton)


    def input_inTable(self):
        self.table=(By.XPATH,"(//table)[3]/child::*//td/div/input")
        inputs=self.find_elements(self.table)
        for one in inputs:
            rNum=random.randint(0,100)
            if not one.get_attribute('readonly')=='readonly':
                one.clear()
                one.send_keys(rNum)

    def input_modifyData(self,value):
        # self.type(Keys.BACKSPACE,self.modifyValue)
        self.type(value,self.modifyValue)

    def click_modifyButton(self):
        self.click(self.modifyButton)











