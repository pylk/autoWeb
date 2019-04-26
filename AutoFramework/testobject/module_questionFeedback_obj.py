#coding=utf-8
import time

from AutoFramework.core.pom import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random

#问题添加对象及其操作
class Module_QuestionFeedback_add(BasePage):
    '''问题添加'''
    def __init__(self,*args,**kwargs):
        super(Module_QuestionFeedback_add,self).__init__(*args,**kwargs)
        #添加问题
        self.questionAdd=(By.ID,"btn_addquestion")
        #检查点
        self.checkName=(By.XPATH,"//a[text()='欢迎您：管理员']")
        #类别
        typeList=[(By.XPATH,"//span[text()='新需求']"),(By.XPATH, "//span[text()='BUG']")]
        self.classis=typeList[random.randint(0,len(typeList)-1)]
        #产品板块
        self.productModule=(By.XPATH,"//input[@placeholder='请选择']")

        #标题名称
        self.name=(By.ID,"settitleName")
        #描述
        self.describe=(By.ID,"setTextarea")
        #选择文件
        self.choose_file=(By.ID,"question-file1")
        #添加按钮
        self.addButton=(By.XPATH,"//a[text()='创建']")

    def click_questionAdd(self):
        self.click(self.questionAdd)
    def choose_type(self):
        self.click(self.classis)
    def choose_module(self):
        moduleList=['风电','光伏','水电','火电','煤矿','综合产业','其它']
        moduleValue=moduleList[random.randint(0,len(moduleList)-1)]
        # self.move_to_element(self.productModule)
        self.click(self.productModule)
        tempValue="//input[@placeholder='请选择']/../following-sibling::*/dd[text()='"+moduleValue+"']"
        tempSelector=(By.XPATH,tempValue)
        self.move_to_element(tempSelector)
        self.click(tempSelector)
    def input_name(self,value):
        self.type(value,self.name)
    def input_desc(self,value):
        self.type(value,self.describe)
    def click_upload(self,filePath):
        self.upload_file(self.choose_file,filePath)
    def click_addButton(self):
        self.click(self.addButton)


#问题审计对象及其操作
class Module_QuestionFeedback_audit(BasePage):

    def __init__(self,*args,**kwargs):
        super(Module_QuestionFeedback_audit,self).__init__(*args,**kwargs)
        #搜索名称
        self.searchName=(By.XPATH,"// label[text() = '标题'] /../ descendant::input[ @ name = 'email']")
        #搜索类型
        self.searchType = (By.XPATH, "//label[text()='状态']/following-sibling::*/descendant::input")
        #搜索按钮
        self.searchButton=(By.XPATH,"//button[@id='quButton-inquire']")
        #搜索返回表格
        self.resultTable=(By.XPATH,"//table[@class='question-table']")
        #表格中的名称字段
        self.tableValueName=(By.XPATH,"//tbody[@id='t_body']/tr/td[2]")
        #备注
        self.comments=(By.ID,"questionTextareaVal")
        #备注保存按钮
        self.commentSave=(By.XPATH,"//a[text()='保存备注']")
        #下一步
        self.nextStep=(By.XPATH,"//a[text()='下一步']")

    def input_searchName(self,value):
        self.type(value,self.searchName)
    def choose_searchType(self,value):
        self.click(self.searchType)
        tempValue="//label[text()='状态']/following-sibling::*/descendant::dd[text()='"+value+"']"
        tempSelector=(By.XPATH,tempValue)
        self.move_to_element(tempSelector)
        self.click(tempSelector)
        # self.selectByText(self.searchType,value)
    def click_searchButton(self):
        self.click(self.searchButton)
    def click_firstRowData(self):
        self.table_clickInTableByRow(self.resultTable,self.tableValueName,1)
    def input_comments(self,value):
        self.type(value,self.comments)
    def click_saveComments(self):
        self.click(self.commentSave)
    def click_nextStep(self):
        self.click(self.nextStep)


#问题备注对象及其操作
class Module_QuestionFeedback_addComments(BasePage):

    def __init__(self,*args,**kwargs):
        super(Module_QuestionFeedback_addComments,self).__init__(*args,**kwargs)
        #搜索名称
        self.searchName=(By.XPATH,"// label[text() = '标题'] /../ descendant::input[ @ name = 'email']")
        #搜索类型
        self.searchType = (By.XPATH, "//label[text()='状态']/following-sibling::*/descendant::input")
        #搜索按钮
        self.searchButton=(By.XPATH,"//button[@id='quButton-inquire']")
        #搜索返回表格
        self.resultTable=(By.XPATH,"//table[@class='question-table']")
        #表格中的名称字段
        self.tableValueName=(By.XPATH,"//tbody[@id='t_body']/tr/td[2]")
        #备注
        self.comments=(By.ID,"questionTextareaVal")
        #备注保存按钮
        self.commentSave=(By.XPATH,"//a[text()='保存备注']")


    def input_searchName(self,value):
        self.type(value,self.searchName)
    def choose_searchType(self,value):
        self.click(self.searchType)
        tempValue="//label[text()='状态']/following-sibling::*/descendant::dd[text()='"+value+"']"
        tempSelector=(By.XPATH,tempValue)
        self.move_to_element(tempSelector)
        self.click(tempSelector)
        # self.selectByText(self.searchType,value)
    def click_searchButton(self):
        self.click(self.searchButton)
    def click_firstRowData(self):
        self.table_clickInTableByRow(self.resultTable,self.tableValueName,1)
    def input_comments(self,value):
        self.type(value,self.comments)
    def click_saveComments(self):
        self.click(self.commentSave)


#问题开发对象及其操作
class Module_QuestionFeedback_develop(BasePage):

    def __init__(self,*args,**kwargs):
        super(Module_QuestionFeedback_develop,self).__init__(*args,**kwargs)
        #搜索名称
        self.searchName=(By.XPATH,"// label[text() = '标题'] /../ descendant::input[ @ name = 'email']")
        #搜索类型
        self.searchType = (By.XPATH, "//label[text()='状态']/following-sibling::*/descendant::input")
        #搜索按钮
        self.searchButton=(By.XPATH,"//button[@id='quButton-inquire']")
        #搜索返回表格
        self.resultTable=(By.XPATH,"//table[@class='question-table']")
        #表格中的名称字段
        self.tableValueName=(By.XPATH,"//tbody[@id='t_body']/tr/td[2]")
        #备注
        self.comments=(By.ID,"questionTextareaVal")
        #备注保存按钮
        self.commentSave=(By.XPATH,"//a[text()='保存备注']")
        #下一步
        self.nextStep=(By.XPATH,"//a[text()='下一步']")

    def input_searchName(self,value):
        self.type(value,self.searchName)
    def choose_searchType(self,value):
        self.click(self.searchType)
        tempValue="//label[text()='状态']/following-sibling::*/descendant::dd[text()='"+value+"']"
        tempSelector=(By.XPATH,tempValue)
        self.move_to_element(tempSelector)
        self.click(tempSelector)
        # self.selectByText(self.searchType,value)
    def click_searchButton(self):
        self.click(self.searchButton)
    def click_firstRowData(self):
        self.table_clickInTableByRow(self.resultTable,self.tableValueName,1)
    def input_comments(self,value):
        self.type(value,self.comments)
    def click_saveComments(self):
        self.click(self.commentSave)
    def click_nextStep(self):
        self.click(self.nextStep)

#问题验证对象及其操作
class Module_QuestionFeedback_check(BasePage):

    def __init__(self,*args,**kwargs):
        super(Module_QuestionFeedback_check,self).__init__(*args,**kwargs)
        #搜索名称
        self.searchName=(By.XPATH,"// label[text() = '标题'] /../ descendant::input[ @ name = 'email']")
        #搜索类型
        self.searchType = (By.XPATH, "//label[text()='状态']/following-sibling::*/descendant::input")
        #搜索按钮
        self.searchButton=(By.XPATH,"//button[@id='quButton-inquire']")
        #搜索返回表格
        self.resultTable=(By.XPATH,"//table[@class='question-table']")
        #表格中的名称字段
        self.tableValueName=(By.XPATH,"//tbody[@id='t_body']/tr/td[2]")
        #备注
        self.comments=(By.ID,"questionTextareaVal")
        #备注保存按钮
        self.commentSave=(By.XPATH,"//a[text()='保存备注']")
        #下一步
        self.nextStep=(By.XPATH,"//a[text()='下一步']")

    def input_searchName(self,value):
        self.type(value,self.searchName)
    def choose_searchType(self,value):
        self.click(self.searchType)
        tempValue="//label[text()='状态']/following-sibling::*/descendant::dd[text()='"+value+"']"
        tempSelector=(By.XPATH,tempValue)
        self.move_to_element(tempSelector)
        self.click(tempSelector)
        # self.selectByText(self.searchType,value)
    def click_searchButton(self):
        self.click(self.searchButton)
    def click_firstRowData(self):
        self.table_clickInTableByRow(self.resultTable,self.tableValueName,1)
    def input_comments(self,value):
        self.type(value,self.comments)
    def click_saveComments(self):
        self.click(self.commentSave)
    def click_nextStep(self):
        self.click(self.nextStep)

#问题挂起对象及其操作
class Module_QuestionFeedback_suspend(BasePage):

    def __init__(self,*args,**kwargs):
        super(Module_QuestionFeedback_suspend,self).__init__(*args,**kwargs)
        #搜索名称
        self.searchName=(By.XPATH,"// label[text() = '标题'] /../ descendant::input[ @ name = 'email']")
        #搜索类型
        self.searchType = (By.XPATH, "//label[text()='状态']/following-sibling::*/descendant::input")
        #搜索按钮
        self.searchButton=(By.XPATH,"//button[@id='quButton-inquire']")
        #搜索返回表格
        self.resultTable=(By.XPATH,"//table[@class='question-table']")
        #表格中的名称字段
        self.tableValueName=(By.XPATH,"//tbody[@id='t_body']/tr/td[2]")
        #备注
        self.comments=(By.ID,"questionTextareaVal")
        #备注保存按钮
        self.commentSave=(By.XPATH,"//a[text()='保存备注']")
        #下一步
        self.nextStep=(By.XPATH,"//a[text()='下一步']")
        #挂起
        self.suspend=(By.XPATH,"//a[text()='挂起']")

    def input_searchName(self,value):
        self.type(value,self.searchName)
    def choose_searchType(self,value):
        self.click(self.searchType)
        tempValue="//label[text()='状态']/following-sibling::*/descendant::dd[text()='"+value+"']"
        tempSelector=(By.XPATH,tempValue)
        self.move_to_element(tempSelector)
        self.click(tempSelector)
        # self.selectByText(self.searchType,value)
    def click_searchButton(self):
        self.click(self.searchButton)
    def click_firstRowData(self):
        self.table_clickInTableByRow(self.resultTable,self.tableValueName,1)
    def input_comments(self,value):
        self.type(value,self.comments)
    def click_saveComments(self):
        self.click(self.commentSave)
    def click_nextStep(self):
        self.click(self.nextStep)
    def click_suspendButton(self):
        self.click(self.suspend)


#问题关闭对象及其操作
class Module_QuestionFeedback_close(BasePage):

    def __init__(self,*args,**kwargs):
        super(Module_QuestionFeedback_close,self).__init__(*args,**kwargs)
        #搜索名称
        self.searchName=(By.XPATH,"// label[text() = '标题'] /../ descendant::input[ @ name = 'email']")
        #搜索类型
        self.searchType = (By.XPATH, "//label[text()='状态']/following-sibling::*/descendant::input")
        #搜索按钮
        self.searchButton=(By.XPATH,"//button[@id='quButton-inquire']")
        #搜索返回表格
        self.resultTable=(By.XPATH,"//table[@class='question-table']")
        #表格中的名称字段
        self.tableValueName=(By.XPATH,"//tbody[@id='t_body']/tr/td[2]")
        #备注
        self.comments=(By.ID,"questionTextareaVal")
        #备注保存按钮
        self.commentSave=(By.XPATH,"//a[text()='保存备注']")
        #下一步
        self.nextStep=(By.XPATH,"//a[text()='下一步']")
        #挂起
        self.suspend=(By.XPATH,"//a[text()='挂起']")
        #关闭
        self.close=(By.XPATH,"//a[text()='关闭问题']")

    def input_searchName(self,value):
        self.type(value,self.searchName)
    def choose_searchType(self,value):
        self.click(self.searchType)
        tempValue="//label[text()='状态']/following-sibling::*/descendant::dd[text()='"+value+"']"
        tempSelector=(By.XPATH,tempValue)
        self.move_to_element(tempSelector)
        self.click(tempSelector)
        # self.selectByText(self.searchType,value)
    def click_searchButton(self):
        self.click(self.searchButton)
    def click_firstRowData(self):
        self.table_clickInTableByRow(self.resultTable,self.tableValueName,1)
    def input_comments(self,value):
        self.type(value,self.comments)
    def click_saveComments(self):
        self.click(self.commentSave)
    def click_nextStep(self):
        self.click(self.nextStep)
    def click_suspendButton(self):
        self.click(self.suspend)
    def click_closeButton(self):
        self.click(self.close)





