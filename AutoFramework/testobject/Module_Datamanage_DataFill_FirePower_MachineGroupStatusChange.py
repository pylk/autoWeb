#encode:utf-8
from datetime import datetime,timedelta
import time
from selenium.webdriver.common.by import By
from AutoFramework.core.pom import BasePage


class Module_DataManage_DataFill_FirePower_Fill_GroupStatusChange(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_DataManage_DataFill_FirePower_Fill_GroupStatusChange,self).__init__(*args,**kwargs)
        self.firePowerTree = (By.XPATH, "//span[text()='火电']/../../span[1]")
        self.nayong = (By.XPATH, "//span[text()='火电']/../following-sibling::*//span[text()='纳雍电厂']/../../span")
        self.nayongOneFactory = (By.XPATH,
                                 "//span[text()='火电']/../following-sibling::*//span[text()='纳雍电厂']/..//following-sibling::*//span[text()='纳雍一厂']/../../span")
        self.groupOne = (By.XPATH,
                         "//span[text()='火电']/../following-sibling::*//span[text()='纳雍电厂']/..//following-sibling::*//span[text()='纳雍一厂']/..//following-sibling::*//span[text()='#1机组']")


        self.reporter=(By.XPATH,"//label[text()='报告人:']/following-sibling::*/input")
        self.reportTime=(By.NAME,"reportDate")
        self.oldstatusInput=(By.XPATH,"//select[@id='lastState']/following-sibling::*/descendant::*/input")
        self.oldstatus = (By.XPATH, "//select[@id='lastState']")
        self.statusAfterChangeInput = (By.XPATH, "//select[@name='changeState']/following-sibling::*/descendant::*/input")
        self.statusAfterChange = (By.XPATH, "//select[@name='changeState']")
        self.brifReasonInput = (By.XPATH, "//select[@name='briefReasonID']/following-sibling::*/descendant::*/input")
        self.brifReason = (By.XPATH, "//select[@name='briefReasonID']")
        self.changeTypeInput = (By.XPATH, "//select[@name='changeTypeID']/following-sibling::*/descendant::*/input")
        self.changeType = (By.XPATH, "//select[@name='changeTypeID']")
        self.oldStartTime= (By.NAME, "lastStateTime")
        self.changeTime = (By.NAME, "changeTime")
        self.eatEndTime=(By.NAME, "expectedEndTime")

        self.recordInNonStop=(By.XPATH,"//span[text()='记入非停']/following-sibling::*[1]")
        self.recordInCorp = (By.XPATH, "//span[text()='报集团']/following-sibling::*[1]")

        self.reason=(By.XPATH,"//label[text()='原因:']/following-sibling::*/textarea")
        self.brifDesc = (By.XPATH, "//label[text()='简要描述:']/following-sibling::*/textarea")
        self.reportGridReason = (By.XPATH, "//label[text()='汇报电网原因:']/following-sibling::*/textarea")

        self.saveButton=(By.XPATH,"//button[text()='保存']")
        self.submitButton=(By.XPATH,"//button[text()='提交']")

    def getTimeNow(self):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


    def click_firePowerTree(self):
        self.click(self.firePowerTree)
    def click_nayong(self):
        self.click(self.nayong)
    def click_nayongOneFactory(self):
        self.click(self.nayongOneFactory)
    def click_groupOne(self):
        self.click(self.groupOne)

    def input_reporter(self, value):
        self.type(value, self.reporter)
    def input_reportTime(self):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.js_execute("$('input[name="+self.reportTime[1]+"').removeAttr('onfocus')")
        self.js_execute("$('input[name="+self.reportTime[1]+"').removeAttr('readonly')")
        self.typeWithOutClear(now,self.reportTime)
        self.wait(2)


    def select_oldstatus(self, value):
        self.click(self.oldstatusInput)
        xpahtValue="//select[@id='lastState']/following-sibling::*/descendant::*/dd[text()='"+value+"']"
        self.click((By.XPATH,xpahtValue))
    def select_statusAfterChange(self, value):
        self.click(self.statusAfterChangeInput)
        xpahtValue = "//select[@name='changeState']/following-sibling::*/descendant::*/dd[text()='" + value + "']"
        self.click((By.XPATH, xpahtValue))
    def select_brifReason(self, value):
        self.click(self.brifReasonInput)
        xpahtValue = "//select[@name='briefReasonID']/following-sibling::*/descendant::*/dd[text()='" + value + "']"
        self.click((By.XPATH, xpahtValue))
    def select_changeType(self, value):
        self.click(self.changeTypeInput)
        xpahtValue = "//select[@name='changeTypeID']/following-sibling::*/descendant::*/dd[text()='" + value + "']"
        self.click((By.XPATH, xpahtValue))



    def input_oldStartTime(self):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.js_execute("$('input[name="+self.oldStartTime[1]+"').removeAttr('onfocus')")
        self.js_execute("$('input[name="+self.oldStartTime[1]+"').removeAttr('readonly')")
        self.typeWithOutClear(now,self.oldStartTime)

    def input_changeTime(self):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.js_execute("$('input[name="+self.changeTime[1]+"').removeAttr('onfocus')")
        self.js_execute("$('input[name="+self.changeTime[1]+"').removeAttr('readonly')")
        self.typeWithOutClear(now,self.changeTime)

    def input_eatEndTime(self):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.js_execute("$('input[name="+self.eatEndTime[1]+"').removeAttr('onfocus')")
        self.js_execute("$('input[name="+self.eatEndTime[1]+"').removeAttr('readonly')")
        self.typeWithOutClear(now,self.eatEndTime)

    def input_reason(self, value):
        self.type(value, self.reason)
    def input_brifDesc(self, value):
        self.type(value, self.brifDesc)
    def input_reportGridReason(self, value):
        self.type(value, self.reportGridReason)

    def click_recordInNonStop(self):
        self.click(self.recordInNonStop)
    def click_recordInCorp(self):
        self.click(self.recordInCorp)

    def click_saveButton(self):
        self.click(self.saveButton)
    def click_submitButton(self):
        self.click(self.submitButton)




class Module_DataManage_DataFill_FirePower_Confirm_GroupStatusChange(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_DataManage_DataFill_FirePower_Confirm_GroupStatusChange,self).__init__(*args,**kwargs)
        self.table=(By.XPATH,"//table[@id='UnitTable']")

    def click_confirmButtonInTable(self):
        row=self.table_getRowNum(self.table)
        for i in range(1,row+1):
            selector=(By.XPATH,"//button[text()='确认']")
            if self.isDisplayed(selector):
                self.table_clickInTableByRow(self.table,(By.XPATH,"//button[text()='确认']"),i)
                # time.sleep(3)
                # self.switchAlertAccept()
                break
        else:
            self.shot('没有需要确认的机组变更')




class Module_DataManage_DataFill_FirePower_Modify_GroupStatusChange(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_DataManage_DataFill_FirePower_Modify_GroupStatusChange,self).__init__(*args,**kwargs)
        self.table=(By.XPATH,"//table[@id='UnitTable']")
        self.startTime=(By.NAME,"startTime")
        self.endTime=(By.NAME,"endTime")
        self.searchButton=(By.XPATH,"//button[text()='查询']")
        self.oldstatusInput = (By.XPATH, "//select[@id='lastState']/following-sibling::*/descendant::*/input")
        self.oldstatus = (By.XPATH, "//select[@id='lastState']")
        self.statusAfterChangeInput = (
        By.XPATH, "//select[@name='changeState']/following-sibling::*/descendant::*/input")
        self.statusAfterChange = (By.XPATH, "//select[@name='changeState']")
        self.saveButton=(By.XPATH,"//button[text()='保存']")
        self.submitButton=(By.XPATH,"//button[text()='提交']")


    def input_startTime(self):
        now=datetime.now()
        lastDay=(now-timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')
        # self.jquery_removeProperty("input","id",self.startTime[1],['onfocus','readonly'])
        self.js_execute("$('input[name="+self.startTime[1]+"').removeAttr('onfocus')")
        self.js_execute("$('input[name="+self.startTime[1]+"').removeAttr('readonly')")
        self.typeWithOutClear(lastDay,self.startTime)
        self.justWait(2)

    def input_endTime(self):
        now=datetime.now()
        tommorrowDay=(now+timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')
        # self.jquery_removeProperty("input","id",self.endTime[1],['onfocus','readonly'])
        self.js_execute("$('input[name="+self.endTime[1]+"').removeAttr('onfocus')")
        self.js_execute("$('input[name="+self.endTime[1]+"').removeAttr('readonly')")
        self.typeWithOutClear(tommorrowDay,self.endTime)
        self.justWait(2)

    def select_oldstatus(self, value):
        self.click(self.oldstatusInput)
        xpahtValue="//select[@id='lastState']/following-sibling::*/descendant::*/dd[text()='"+value+"']"
        self.click((By.XPATH,xpahtValue))
    def select_statusAfterChange(self, value):
        self.click(self.statusAfterChangeInput)
        xpahtValue = "//select[@name='changeState']/following-sibling::*/descendant::*/dd[text()='" + value + "']"
        self.click((By.XPATH, xpahtValue))

    def click_searchButton(self):
        self.click(self.searchButton)

    def click_modifyButtonInTable(self):
        row=self.table_getRowNum(self.table)
        for i in range(1,row+1):
            selector=(By.XPATH,"//button[text()='修改']")
            if self.isDisplayed(selector):
                self.table_clickInTableByRow(self.table,(By.XPATH,"//button[text()='修改']"),i)
                # time.sleep(3)
                # self.switchAlertAccept()
                break
        else:
            self.shot('没有需要确认的机组变更')

    def click_saveButton(self):
        self.click(self.saveButton)
    def click_submitButton(self):
        self.click(self.submitButton)


class Module_DataManage_DataFill_FirePower_Delete_GroupStatusChange(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_DataManage_DataFill_FirePower_Delete_GroupStatusChange,self).__init__(*args,**kwargs)
        self.table=(By.XPATH,"//table[@id='UnitTable']")
        self.startTime=(By.NAME,"startTime")
        self.endTime=(By.NAME,"endTime")
        self.searchButton=(By.XPATH,"//button[text()='查询']")



    def input_startTime(self):
        now=datetime.now()
        lastDay=(now-timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')
        # self.jquery_removeProperty("input","id",self.startTime[1],['onfocus','readonly'])
        self.js_execute("$('input[name="+self.startTime[1]+"').removeAttr('onfocus')")
        self.js_execute("$('input[name="+self.startTime[1]+"').removeAttr('readonly')")
        self.typeWithOutClear(lastDay,self.startTime)
        self.justWait(2)

    def input_endTime(self):
        now=datetime.now()
        tommorrowDay=(now+timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')
        # self.jquery_removeProperty("input","id",self.endTime[1],['onfocus','readonly'])
        self.js_execute("$('input[name="+self.endTime[1]+"').removeAttr('onfocus')")
        self.js_execute("$('input[name="+self.endTime[1]+"').removeAttr('readonly')")
        self.typeWithOutClear(tommorrowDay,self.endTime)
        self.justWait(2)

    def click_searchButton(self):
        self.click(self.searchButton)

    def click_deleteButtonInTable(self):
        row=self.table_getRowNum(self.table)
        for i in range(1,row+1):
            selector=(By.XPATH,"//button[text()='删除']")
            if self.isDisplayed(selector):
                self.table_clickInTableByRow(self.table,(By.XPATH,"//button[text()='删除']"),i)
                # time.sleep(3)
                # self.switchAlertAccept()
                break
        else:
            self.shot('没有需要确认的机组变更')


class Module_DataManage_DataFill_FirePower_Record_GroupStatusChange(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_DataManage_DataFill_FirePower_Record_GroupStatusChange,self).__init__(*args,**kwargs)
        self.table=(By.XPATH,"//table[@id='UnitTable']")
        self.startTime=(By.NAME,"startTime")
        self.endTime=(By.NAME,"endTime")
        self.searchButton=(By.XPATH,"//button[text()='查询']")



    def input_startTime(self):
        now=datetime.now()
        lastDay=(now-timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')
        # self.jquery_removeProperty("input","id",self.startTime[1],['onfocus','readonly'])
        self.js_execute("$('input[name="+self.startTime[1]+"').removeAttr('onfocus')")
        self.js_execute("$('input[name="+self.startTime[1]+"').removeAttr('readonly')")
        self.typeWithOutClear(lastDay,self.startTime)
        self.justWait(2)

    def input_endTime(self):
        now=datetime.now()
        tommorrowDay=(now+timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')
        # self.jquery_removeProperty("input","id",self.endTime[1],['onfocus','readonly'])
        self.js_execute("$('input[name="+self.endTime[1]+"').removeAttr('onfocus')")
        self.js_execute("$('input[name="+self.endTime[1]+"').removeAttr('readonly')")
        self.typeWithOutClear(tommorrowDay,self.endTime)
        self.justWait(2)



    def click_searchButton(self):
        self.click(self.searchButton)

    def click_recordButtonInTable(self):
        row=self.table_getRowNum(self.table)
        for i in range(1,row+1):
            selector=(By.XPATH,"//button[text()='详情']")
            if self.isDisplayed(selector):
                self.table_clickInTableByRow(self.table,(By.XPATH,"//button[text()='详情']"),i)
                # time.sleep(3)
                # self.switchAlertAccept()
                break
        else:
            self.shot('没有需要确认的机组变更')


class Module_DataManage_DataFill_FirePower_typeMaintain_GroupStatusChange(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_DataManage_DataFill_FirePower_typeMaintain_GroupStatusChange,self).__init__(*args,**kwargs)
        self.table=(By.XPATH,"//table[@id='UnitTable']")
        self.startTime=(By.NAME,"startTime")
        self.endTime=(By.NAME,"endTime")
        self.searchButton=(By.XPATH,"//button[text()='查询']")

        self.filterList=(By.XPATH,"//select[@name='parentCode']")
        self.addButton=(By.XPATH,"//button[text()='新增']")

        self.add_type=(By.XPATH,"//select[@id='parentCodeTarget']")
        self.add_name=(By.XPATH,"//textarea[@id='name']")
        self.add_confirm=(By.XPATH,"//a[text()='确定']")

    def click_addButton(self):
        self.click(self.addButton)
    def select_add_type(self,value):
        self.selectByText(self.add_type,value)
    def input_add_name(self,value):
        self.type(value,self.add_name)
    def click_add_confirm(self):
        self.click(self.add_confirm)



