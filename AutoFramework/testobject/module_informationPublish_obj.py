#coding=utf-8
import time

from AutoFramework.core.pom import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random

#信息发布，组维护的增删改查，对象及其操作
class Module_informationPublish_groupMaintence(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_informationPublish_groupMaintence,self).__init__(*args,**kwargs)
        #添加群组
        self.addGroup=(By.XPATH,"//button[@id='addTC']")
        #组名称查找输入框
        self.groupNameSearchBox=(By.XPATH,"//input[@id='name']")
        #查询按钮
        self.searchButton=(By.XPATH,"//button[text()='查询']")
        #新增组名
        self.groupName=(By.NAME,"GroupName")
        #新增组成员
        self.groupMember=(By.XPATH,"//div[@id='tagsinput_addTag']")
        #保存按钮
        self.addGroupButton=(By.XPATH,"//button[@id='savaGroupInfo']")

        #用户搜索框
        self.searchName=(By.XPATH,"//input[@id='searchName']")
        #用户搜索按钮
        self.searchNameButton=(By.XPATH,"//label[text()='用户姓名：']/following-sibling::button[text()='查询']")

        #选择一个组 公司领导
        # self.chooseGroup=(By.XPATH,"//span[text()='公司领导']")
        #用户列表
        self.userTable=(By.XPATH,"//table[@id='userTable']")
        #添加按钮
        self.addButton=(By.XPATH,"//button[text()='添加']")

        #用户组编辑
        self.groupEdit=(By.XPATH,"//a[@title='编辑']")
        #用户组删除
        self.groupDelete=(By.XPATH,"//a[@title='删除']")
        #用户组列表
        self.groupList=(By.XPATH,"//table[@id='recordTable']")
        #被删除用户
        self.deletingUser=(By.XPATH,"//a[@name='江浩']")
        #修改按钮
        self.modifyButton=(By.XPATH,"//button[@id='updateGroupInfo']")

        #确定删除
        self.confirmDelete=(By.XPATH,"//span[text()='Ok']")


    def click_addGroup(self):
        self.click(self.addGroup)
    def input_groupName(self,value):
        self.type(value,self.groupName)
    def click_addGroupMember(self):
        self.click(self.groupMember)
    def input_searchNameAndSearch(self,value):
        self.type(value,self.searchName)
        self.click(self.searchNameButton)
    def choose_oneUser(self):
        self.table_SelectByIndex(self.userTable,1)
    def click_addButton(self):
        self.click(self.addButton)
    def click_addGroupButton(self):
        self.click(self.addGroupButton)



    ##后续部分用来做修改，和删除的操作
    def input_groupNameSearchBox(self,value):
        self.type(value,self.groupNameSearchBox)
    def click_searchButton(self):
        self.click(self.searchButton)
    def click_groupEdit(self):
        self.table_clickInTableByRow(self.groupList,self.groupEdit,1)
    def click_deletingUser(self):
        self.move_to_element(self.deletingUser)
        self.click(self.deletingUser)
        # self.js_exec(self.deletingUser)
    def click_modifyButton(self):
        self.click(self.modifyButton)


    ##后续部分用来做组删除
    def click_groupDelete(self):
        self.table_clickInTableByRow(self.groupList, self.groupDelete, 1)
    def click_confirmDelete(self):
        self.click(self.confirmDelete)
        self.shot("确定删除组")

#事件消息发布
class Module_informationPublish_EventMsgPub(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_informationPublish_EventMsgPub,self).__init__(*args,**kwargs)
        self.newAddButton=(By.XPATH,"//button[text()='新增']")
        self.newTitle=(By.XPATH,"//input[@id='ptopic']")
        self.newType=(By.XPATH,"//select[@id='msgtype']")
        self.msgName=(By.XPATH,"//input[@id='msgname']")
        self.publishInstitude=(By.XPATH,"//select[@id='msgdepart']/following-sibling::*/button")
        self.onePubInstitude=(By.XPATH,"//b[text()=' 超级管理部门']/../descendant::input")
        self.eventTime=(By.XPATH,"//input[@id='msgtime']")
        self.timeIframe=(By.XPATH,"//iframe[@hidefocus='true']")
        self.confirmEventTime=(By.XPATH,"//input[@value='确定']")
        self.pubTime=(By.XPATH,"//input[@id='ptime']")
        self.receiveGroup=(By.XPATH,"//select[@id='pgroup']/following-sibling::*/button/span")
        self.oneReceiveGroup=(By.XPATH,"//span[text()='test']/../descendant::input")
        self.publishButton=(By.XPATH,"//button[text()='发布']")


    def click_newAddButton(self):
        self.click(self.newAddButton)
    def input_newTitle(self,value):
        self.type(value,self.newTitle)
    def select_newType(self,value):
        self.selectByText(self.newType,value)
    def input_msgName(self,value):
        self.type(value,self.msgName)
    def click_pubInstitude(self):
        self.click(self.publishInstitude)
        self.click(self.onePubInstitude)
        self.click(self.msgName)
    def click_eventTime(self):
        self.click(self.eventTime)
        # self.move_to_element(self.confirmEventTime)
        self.switchFrame(self.find_element(self.timeIframe))
        self.click(self.confirmEventTime)
        self.switchBackFromIframe()
    def click_receiveGroup(self):
        self.click(self.receiveGroup)
        self.move_to_element(self.oneReceiveGroup)
        self.click(self.oneReceiveGroup)
        self.click(self.pubTime)
    def click_publishButton(self):
        self.click(self.publishButton)

#事件消息查找
class Module_informationPublish_EventMsgRecord(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_informationPublish_EventMsgRecord,self).__init__(*args,**kwargs)
        self.searchType=(By.XPATH,"//select[@id='querytype']")
        self.searchDesc=(By.XPATH,"//input[@id='querydesc']")
        self.searchButton=(By.XPATH,"//button[text()='查询']")
        self.msgTable = (By.XPATH, "//table[@id='tables']")

    def select_searchType(self,value):
        self.selectByText(self.searchType,value)
    def input_searchDesc(self,value):
        self.type(value,self.searchDesc)
    def click_searchButton(self):
        self.click(self.searchButton)
    def count_result(self):
        return self.table_getRowNum(self.msgTable)


#事件消息删除
class Module_informationPublish_EventMsgModify(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_informationPublish_EventMsgModify,self).__init__(*args,**kwargs)
        self.searchType=(By.XPATH,"//select[@id='querytype']")
        self.searchDesc=(By.XPATH,"//input[@id='querydesc']")
        self.searchButton=(By.XPATH,"//button[text()='查询']")

        self.msgTable=(By.XPATH,"//table[@id='tables']")
        self.msgDeleteLink=(By.XPATH,"//a[text()='删除']")

    def select_searchType(self,value):
        self.selectByText(self.searchType,value)
    def input_searchDesc(self,value):
        self.type(value,self.searchDesc)
    def click_searchButton(self):
        self.click(self.searchButton)

    def click_deleteLink(self):
        try:
            self.table_clickInTableByRow(self.msgTable,self.msgDeleteLink,1)
            # self.getDriver().switch_to_alert().accept()
        except Exception as e:
            print("exception raise:"+str(e))
    def click_accept(self):
        self.switchAlertAccept()









