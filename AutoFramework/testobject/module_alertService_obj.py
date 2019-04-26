#coding=utf-8
import time

from AutoFramework.core.pom import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random

#配置管理 指标配置
class Module_AlertService_InitPoint(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_AlertService_InitPoint,self).__init__(*args,**kwargs)
        #查询板块
        self.plate=(By.XPATH,"//table[@class='new-table new-tablehead-bj-nei']//select[@id='plate']")
        #查询按钮
        self.searchButton=(By.XPATH,"//table[@class='new-table new-tablehead-bj-nei']//button[@id='querypoint']")
        #添加按钮
        self.addButton=(By.XPATH,"//table[@class='new-table new-tablehead-bj-nei']//button[@id='addpoint']")
        #删除按钮
        self.deleteButton = (By.XPATH, "//table[@class='new-table new-tablehead-bj-nei']//button[@id='deletepoint']")
        #结果表格
        self.resultTable=(By.XPATH,"//table[@id='recordTable']")



        #添加板块
        self.addPlate=(By.XPATH,"//table[@class='new-table new-tablehead-bj']//select[@id='addplate']")
        #添加单位名称
        self.addUnitName =(By.XPATH,"//div[text()='单位名称：']/../following-sibling::*//descendant::*//select")
        #添加机组名称
        self.addGroupName=(By.XPATH,"//div[text()='机组名称：']/../following-sibling::*//descendant::*//select")
        #系统测点
        self.systemPoint=(By.XPATH,"//table[@class='new-table new-tablehead-bj']/descendant::*/input[@id='adddatatype']")
        #测点类别
        self.pointType=(By.XPATH,"//table[@class='new-table new-tablehead-bj']/descendant::*/select[@id='addpointtype']")
        #测点名称
        self.pointName=(By.XPATH,"//table[@class='new-table new-tablehead-bj']/descendant::*/input[@id='addindexname']")
        #测点描述
        self.pointDesc=(By.XPATH,"//table[@class='new-table new-tablehead-bj']/descendant::*/input[@id='addindexdesc']")

        #测点添加
        self.pointAddButton=(By.XPATH,"//div[@class='new-release']/descendant::*//button[text()='添加']")

        #测点页面关闭
        self.pointPageCloseButton=(By.XPATH,"//div[@class='new-release']/descendant::*//button[text()='关闭']")
        #搜索描述
        self.pointSearchDesc=(By.XPATH,"//input[@id='indexdesc']")

    def input_pointSearchDesc(self,value):
        self.type(value,self.pointSearchDesc)
    def choose_oneIteminTable(self):
        self.table_SelectByIndex(self.resultTable,1)
    def click_deleteButton(self):
        self.click(self.deleteButton)
    def click_closePointAddPage(self):
        self.click(self.pointPageCloseButton)
    def count_resultTable(self):
        return int(self.table_getRowNum(self.resultTable))

    def select_plate(self,value):
        # self.justWait()
        self.selectByText(self.plate,value)
        # self.click(self.plate)
        # self.move_to_element((By.XPATH,"//option[text()='火电']"))
        # self.click((By.XPATH,"//option[text()='火电']"))
    def click_searchButton(self):
        self.click(self.searchButton)
    def click_addButton(self):
        self.click(self.addButton)


    def select_addPlate(self,value):
        # self.click(self.addPlate)
        self.selectByText(self.addPlate,value)
    def select_addUnitName(self,value):
        self.selectByText(self.addUnitName,value)
    def select_addGroupName(self,value):
        self.selectByText(self.addGroupName,value)
    def input_systemPoint(self,value):
        self.click(self.systemPoint)
        self.type(value,self.systemPoint)
    def select_pointType(self,value):
        self.selectByText(self.pointType,value)
    def input_pointName(self,value):
        self.click(self.pointName)
        self.type(value,self.pointName)
    def input_pointDesc(self,value):
        self.click(self.pointDesc)
        self.type(value,self.pointDesc)

    def click_pointAddButton(self):
        self.click(self.pointAddButton)


#模拟量报警记录查询
class Module_alertService_SimulateCapacityAlertRecord(BasePage):
    def __init__(self, *args, **kwargs):
        super(Module_alertService_SimulateCapacityAlertRecord, self).__init__(*args, **kwargs)
        #测点描述
        self.pointDesc=(By.XPATH,"//table[@class='new-table new-tablehead-bj-nei']/descendant::*/input[@name='indexDesc']")
        #查找按钮
        self.searchButton=(By.XPATH,"//table[@class='new-table new-tablehead-bj-nei']/descendant::*/button[text()='查询']")
        #表格
        self.resultTable=(By.XPATH,"//table[@id='recordTable']")

    def input_PointDesc(self,value):
        self.click(self.pointDesc)
        self.type(value,self.pointDesc)

    def click_searchButton(self):
        self.click(self.searchButton)
    def count_tableRow(self):
        return int(self.table_getRowNum(self.resultTable))

#开关量报警记录查询
class Module_alertService_SwitcherCapacityAlertRecord(BasePage):
    def __init__(self, *args, **kwargs):
        super(Module_alertService_SwitcherCapacityAlertRecord, self).__init__(*args, **kwargs)
        # 测点描述
        self.pointDesc=(By.XPATH,"//table[@class='new-table new-tablehead-bj-nei']/descendant::*/input[@name='indexDesc']")
        # 查找按钮
        self.searchButton=(By.XPATH,"//table[@class='new-table new-tablehead-bj-nei']/descendant::*/button[text()='查询']")
        # 表格
        self.resultTable=(By.XPATH,"//table[@id='recordTable']")

    def input_PointDesc(self,value):
        self.click(self.pointDesc)
        self.type(value,self.pointDesc)

    def click_searchButton(self):
        self.click(self.searchButton)
    def count_tableRow(self):
        return int(self.table_getRowNum(self.resultTable))


#不刷新报警
class Module_alertService_notFreshAlert(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_alertService_notFreshAlert,self).__init__(*args,**kwargs)
        #数据不刷新报警页面
        self.dataNotFreshAlertPage=(By.XPATH,"//table[@id='datarefreshbody']")
        #测点页面详情
        #self.pointPageDetail=(By.XPATH,"//table[@id='datarefreshhis']")
        self.pointPageDetail = (By.XPATH, "//table[@id='recordTable']")
        #原间隔时间
        self.oldInterval=(By.XPATH,"//input[@id='oldrefreshtime']")
        #新间隔时间
        self.newInterval=(By.XPATH,"//input[@id='newrefreshtime']")
        #确认按钮
        self.confirmModify=(By.XPATH,"//button[text()='确认修改']")

    def count_AlertPage(self):
        return int(self.table_getRowNum(self.dataNotFreshAlertPage))
    def count_pointPageDetail(self):
        return int(self.table_getRowNum(self.pointPageDetail))
    def get_oldInterval(self):
        return self.getValue(self.oldInterval)
    def input_newInterval(self,value):
        self.type(value,self.newInterval)
    def click_confimButton(self):
        self.click(self.confirmModify)

#报警服务-开关量报警配置-新增
class Module_alertService_switcherCapacityAlertConfig(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_alertService_switcherCapacityAlertConfig,self).__init__(*args,**kwargs)
        #新增报警测点
        self.addAlertPointButton=(By.XPATH,"//button[text()='新增报警测点']")
        #选择声音
        self.alertSound=(By.XPATH,"//input[@id='table-voice']")
        #监控平台
        self.sendToMonitorPlatForm=(By.XPATH,"//input[@id='table-sjjk']")
        #添加连接
        #self.addLink=(By.XPATH,"//a[text()='添加测点']")
        self.addLink=('xpath','//*[@class="table-button bn-center"]') #添加测点按钮
        #测点表格
        #self.pointTable=(By.XPATH,"//table[@id='recordTable2']")
        self.pointTable =("xpath",'//*[@name="ck_box"]')
        #保存按钮
        self.saveButton=(By.XPATH,"//button[text()='保存']")

    def click_addAlertPointButton(self):
        self.click(self.addAlertPointButton)
    def click_alertSound(self):
        self.click(self.alertSound)
    def click_sendToMonitorPlatForm(self):
        self.click(self.sendToMonitorPlatForm)
    def click_addLink(self):
        self.click(self.addLink)
    def choose_talbeOneData(self):
        self.table_SelectByIndex(self.pointTable,1)
    def choose_talbeOneData1(self):
        eles=self.find_elements(self.pointTable)
        for ele in eles:
            ele.click()
    def click_saveButton(self):
        self.click(self.saveButton)

#报警服务--模拟量阈值配置
class Module_alertService_simulateCapacityThreasholdConfig(BasePage):
    def __init__(self, *args, **kwargs):
        super(Module_alertService_simulateCapacityThreasholdConfig, self).__init__(*args, **kwargs)
        #结果表格
        self.resultTable=(By.XPATH,"//table[@id='recordTable']")
        #结果表格输入框,选择第三
        self.inputBox=(By.XPATH,"//td[11]/input")

        #测点搜索描述
        self.desc=(By.ID,"indexdesc")
        #查询按钮
        self.searchButton=(By.ID,"buttonid")

        #提交按钮
        self.submitButton=(By.XPATH,"//button[@id='commit']")

    def input_searchDesc(self,value):
        self.type(value, self.desc)
    def click_searchButton(self):
        self.click(self.searchButton)
    def input_in_table(self,value):
        self.table_InputInTableByRow(self.resultTable,self.inputBox,1,value)
    def click_submitButton(self):
        self.click(self.submitButton)

#报警服务--模拟量阈值配置-修改
class Module_alertService_simulateCapacityThreasholdConfig_modify(BasePage):
    def __init__(self, *args, **kwargs):
        super(Module_alertService_simulateCapacityThreasholdConfig_modify, self).__init__(*args, **kwargs)
        #结果表格
        self.resultTable=(By.XPATH,"//table[@id='recordTable']")
        #结果表格输入框,选择第三
        self.inputBox=(By.XPATH,"//td[11]/input")

        #测点搜索描述
        self.desc=(By.ID,"indexdesc")
        #查询按钮
        self.searchButton=(By.ID,"buttonid")
        #x修改按钮
        self.modifyButton=(By.ID,"commit")

        #查询结果为无数据时
        self.no_data_tip=("xpath",'//*[@id="recordTable"]/tbody/tr/td')

    def is_element_exist(self, selector):
        try:
            self.find_element(selector)
            return True
        except:
            return False

    def input_searchDesc(self,value):
        self.type(value, self.desc)
    def click_searchButton(self):
        self.click(self.searchButton)
    def input_in_table(self,value):
        self.table_InputInTableByRow(self.resultTable,self.inputBox,1,value)
    def choose_oneData(self):
        self.table_SelectByIndex(self.resultTable,1)
    def click_modifyButton(self):
        self.click(self.modifyButton)
        self.switchAlertAccept()

#报警服务--模拟量报警配置
class  Module_alertService_simulateCapacityAlertConfig_add(BasePage):
    def __init__(self, *args, **kwargs):
        super(Module_alertService_simulateCapacityAlertConfig_add, self).__init__(*args, **kwargs)
        #新增按钮
        self.addNewButton=(By.XPATH,"//button[@id='commit']")
        # 选择声音
        self.alertSound = (By.XPATH, "//input[@id='table-voice']")
        # 监控平台
        self.sendToMonitorPlatForm = (By.XPATH, "//input[@id='table-sjjk']")
        # 添加连接
        self.addLink = (By.XPATH, "//a[text()='添加测点']")
        self.addLink = ('xpath', '//*[@class="table-button bn-center"]')  # 添加测点按钮
        # 测点表格
        #self.pointTable=(By.XPATH,"//table[@id='recordTable2']")
        self.pointTable = ("xpath", '//*[@id="recordTable2"]/thead/tr/th[1]/input')

        # 保存按钮
        self.saveButton = (By.XPATH, "//button[text()='保存']")

        #搜索框
        self.searchBox=(By.XPATH,"//input[@id='sindexdesc']")
        # 查询按钮
        self.searchButton = (By.XPATH, "//div[@class='new-head-input new-head-input-max add-bn']/button[text()='查询']")
        #报警级别
        self.alertLevel=(By.XPATH,"//select[@id='alarm-level']")

    def click_addNewButton(self):
        self.click(self.addNewButton)
    def click_alertSound(self):
        self.click(self.alertSound)
    def click_sendToMonitorPlatForm(self):
        self.click(self.sendToMonitorPlatForm)
    def click_addLink(self):
        self.click(self.addLink)
    def select_leve(self,value):
        self.selectByText(self.alertLevel,value)

    def input_searchBox(self,value):
        self.type(value,self.searchBox)
    def click_searchButton(self):
        self.justWait(4)
        self.click(self.searchButton)

    def choose_talbeOneData(self):
        self.table_SelectByIndex(self.pointTable,1)

    def choose_talbeOneData1(self):
        self.click(self.pointTable)
    def click_saveButton(self):
        self.click(self.saveButton)
