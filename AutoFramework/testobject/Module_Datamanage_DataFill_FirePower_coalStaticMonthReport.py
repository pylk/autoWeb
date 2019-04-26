from selenium.webdriver.common.by import By

from AutoFramework.core.pom import BasePage


class Module_Datamanage_DataFill_FirePower_Fill_coalStaticMonthReportFill(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_Datamanage_DataFill_FirePower_Fill_coalStaticMonthReportFill,self).__init__(*args,**kwargs)
        self.firePowerTree = (By.XPATH, "//span[text()='火电']/../../span[1]")
        self.xishui = (
        By.XPATH, "//span[text()='火电']/../following-sibling::*//span[text()='习水电厂']/../span[text()='习水电厂']")
        self.monthStaticNum1  = (By.ID,'inventoryCoalComsumption1')
        self.monthStaticNum2  = (By.ID, 'inventoryCoalComsumption2')
        self.monthStaticNum3  = (By.ID, 'inventoryCoalComsumption3')
        self.monthStaticNum4  = (By.ID, 'inventoryCoalComsumption4')
        self.monthStaticNum5  = (By.ID, 'inventoryCoalComsumption5')
        self.monthStaticNum6  = (By.ID, 'inventoryCoalComsumption6')
        self.monthStaticNum7  = (By.ID, 'inventoryCoalComsumption7')
        self.monthStaticNum8  = (By.ID, 'inventoryCoalComsumption8')
        self.monthStaticNum9  = (By.ID, 'inventoryCoalComsumption9')
        self.monthStaticNum10 = (By.ID, 'inventoryCoalComsumption10')
        self.monthStaticNum11 = (By.ID, 'inventoryCoalComsumption11')
        self.monthStaticNum12 = (By.ID, 'inventoryCoalComsumption12')

        self.fileMonth1   = (By.ID, 'file1')
        self.fileMonth2   = (By.ID, 'file2')
        self.fileMonth3   = (By.ID, 'file3')
        self.fileMonth4   = (By.ID, 'file4')
        self.fileMonth5   = (By.ID, 'file5')
        self.fileMonth6   = (By.ID, 'file6')
        self.fileMonth7   = (By.ID, 'file7')
        self.fileMonth8   = (By.ID, 'file8')
        self.fileMonth9   = (By.ID, 'file9')
        self.fileMonth10  = (By.ID, 'file10')
        self.fileMonth11  = (By.ID, 'file11')
        self.fileMonth12  = (By.ID, 'file12')
        self.saveButton   = (By.ID,'bc')
        self.submitButton = (By.ID,'tj')
        self.modifyButton = (By.ID,'xg')

    def click_firePowerTree(self):
        self.click(self.firePowerTree)
    def click_xishui(self):
        self.click(self.xishui)


    def input_monthStaticNum1(self, value):
        self.type(value, self.monthStaticNum1)
    def input_monthStaticNum2(self, value):
        self.type(value, self.monthStaticNum2)
    def input_monthStaticNum3(self, value):
        self.type(value, self.monthStaticNum3)
    def input_monthStaticNum4(self, value):
        self.type(value, self.monthStaticNum4)
    def input_monthStaticNum5(self, value):
        self.type(value, self.monthStaticNum5)
    def input_monthStaticNum6(self, value):
        self.type(value, self.monthStaticNum6)
    def input_monthStaticNum7(self, value):
        self.type(value, self.monthStaticNum7)
    def input_monthStaticNum8(self, value):
        self.type(value, self.monthStaticNum8)
    def input_monthStaticNum9(self, value):
        self.type(value, self.monthStaticNum9)
    def input_monthStaticNum10(self, value):
        self.type(value, self.monthStaticNum10)
    def input_monthStaticNum11(self, value):
        self.type(value, self.monthStaticNum11)
    def input_monthStaticNum12(self, value):
        self.type(value, self.monthStaticNum12)

    def uploadFile_fileMonth1(self, path):
        return self.upload_file(self.fileMonth1, path)
    def uploadFile_fileMonth2(self, path):
        return self.upload_file(self.fileMonth2, path)
    def uploadFile_fileMonth3(self, path):
        return self.upload_file(self.fileMonth3, path)
    def uploadFile_fileMonth4(self, path):
        return self.upload_file(self.fileMonth4, path)
    def uploadFile_fileMonth5(self, path):
        return self.upload_file(self.fileMonth5, path)
    def uploadFile_fileMonth6(self, path):
        return self.upload_file(self.fileMonth6, path)
    def uploadFile_fileMonth7(self, path):
        return self.upload_file(self.fileMonth7, path)
    def uploadFile_fileMonth8(self, path):
        return self.upload_file(self.fileMonth8, path)
    def uploadFile_fileMonth9(self, path):
        return self.upload_file(self.fileMonth9, path)
    def uploadFile_fileMonth10(self, path):
        return self.upload_file(self.fileMonth10, path)
    def uploadFile_fileMonth11(self, path):
        return self.upload_file(self.fileMonth11, path)
    def uploadFile_fileMonth12(self, path):
        return self.upload_file(self.fileMonth12, path)

    def click_saveButton(self):
        self.click(self.saveButton)
    def click_submitButton(self):
        self.click(self.submitButton)
    def click_modifyButton(self):
        self.click(self.modifyButton)

    def getAttr_fileMonth1(self):
        return self.getAttribute(self.fileMonth1,"style")
    def getAttr_fileMonth2(self):
        return self.getAttribute(self.fileMonth2,"style")
    def getAttr_fileMonth3(self):
        return self.getAttribute(self.fileMonth3,"style")
    def getAttr_fileMonth4(self):
        return self.getAttribute(self.fileMonth4,"style")
    def getAttr_fileMonth5(self):
        return self.getAttribute(self.fileMonth5,"style")
    def getAttr_fileMonth6(self):
        return self.getAttribute(self.fileMonth6,"style")
    def getAttr_fileMonth7(self):
        return self.getAttribute(self.fileMonth7,"style")
    def getAttr_fileMonth8(self):
        return self.getAttribute(self.fileMonth8,"style")
    def getAttr_fileMonth9(self):
        return self.getAttribute(self.fileMonth9,"style")
    def getAttr_fileMonth10(self):
        return self.getAttribute(self.fileMonth10,"style")
    def getAttr_fileMonth11(self):
        return self.getAttribute(self.fileMonth11,"style")
    def getAttr_fileMonth12(self):
        return self.getAttribute(self.fileMonth12,"style")
    def getAttr_monthStaticNum1(self):
        return self.getAttribute(self.monthStaticNum1,"readonly")
    def getAttr_monthStaticNum2(self):
        return self.getAttribute(self.monthStaticNum2,"readonly")
    def getAttr_monthStaticNum3(self):
        return self.getAttribute(self.monthStaticNum3,"readonly")
    def getAttr_monthStaticNum4(self):
        return self.getAttribute(self.monthStaticNum4,"readonly")
    def getAttr_monthStaticNum5(self):
        return self.getAttribute(self.monthStaticNum5,"readonly")
    def getAttr_monthStaticNum6(self):
        return self.getAttribute(self.monthStaticNum6,"readonly")
    def getAttr_monthStaticNum7(self):
        return self.getAttribute(self.monthStaticNum7,"readonly")
    def getAttr_monthStaticNum8(self):
        return self.getAttribute(self.monthStaticNum8,"readonly")
    def getAttr_monthStaticNum9(self):
        return self.getAttribute(self.monthStaticNum9,"readonly")
    def getAttr_monthStaticNum10(self):
        return self.getAttribute(self.monthStaticNum10,"readonly")
    def getAttr_monthStaticNum11(self):
        return self.getAttribute(self.monthStaticNum11,"readonly")
    def getAttr_monthStaticNum12(self):
        return self.getAttribute(self.monthStaticNum12,"readonly")


class Module_Datamanage_DataFill_FirePower_Modify_coalStaticMonthReportModify(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_Datamanage_DataFill_FirePower_Modify_coalStaticMonthReportModify,self).__init__(*args,**kwargs)
        self.firePowerTree = (By.XPATH, "//span[text()='火电']/../../span[1]")
        self.xishui = (
        By.XPATH, "//span[text()='火电']/../following-sibling::*//span[text()='习水电厂']/../span[text()='习水电厂']")
        self.monthStaticNum1  = (By.ID,'inventoryCoalComsumption1')
        self.monthStaticNum2  = (By.ID, 'inventoryCoalComsumption2')
        self.monthStaticNum3  = (By.ID, 'inventoryCoalComsumption3')
        self.monthStaticNum4  = (By.ID, 'inventoryCoalComsumption4')
        self.monthStaticNum5  = (By.ID, 'inventoryCoalComsumption5')
        self.monthStaticNum6  = (By.ID, 'inventoryCoalComsumption6')
        self.monthStaticNum7  = (By.ID, 'inventoryCoalComsumption7')
        self.monthStaticNum8  = (By.ID, 'inventoryCoalComsumption8')
        self.monthStaticNum9  = (By.ID, 'inventoryCoalComsumption9')
        self.monthStaticNum10 = (By.ID, 'inventoryCoalComsumption10')
        self.monthStaticNum11 = (By.ID, 'inventoryCoalComsumption11')
        self.monthStaticNum12 = (By.ID, 'inventoryCoalComsumption12')

        self.fileMonth1   = (By.ID, 'file1')
        self.fileMonth2   = (By.ID, 'file2')
        self.fileMonth3   = (By.ID, 'file3')
        self.fileMonth4   = (By.ID, 'file4')
        self.fileMonth5   = (By.ID, 'file5')
        self.fileMonth6   = (By.ID, 'file6')
        self.fileMonth7   = (By.ID, 'file7')
        self.fileMonth8   = (By.ID, 'file8')
        self.fileMonth9   = (By.ID, 'file9')
        self.fileMonth10  = (By.ID, 'file10')
        self.fileMonth11  = (By.ID, 'file11')
        self.fileMonth12  = (By.ID, 'file12')
        self.saveButton   = (By.ID,'bc')
        self.submitButton = (By.ID,'tj')
        self.modifyButton = (By.ID,'xg')

    def click_firePowerTree(self):
        self.click(self.firePowerTree)
    def click_xishui(self):
        self.click(self.xishui)


    def input_monthStaticNum1(self, value):
        self.type(value, self.monthStaticNum1)
    def input_monthStaticNum2(self, value):
        self.type(value, self.monthStaticNum2)
    def input_monthStaticNum3(self, value):
        self.type(value, self.monthStaticNum3)
    def input_monthStaticNum4(self, value):
        self.type(value, self.monthStaticNum4)
    def input_monthStaticNum5(self, value):
        self.type(value, self.monthStaticNum5)
    def input_monthStaticNum6(self, value):
        self.type(value, self.monthStaticNum6)
    def input_monthStaticNum7(self, value):
        self.type(value, self.monthStaticNum7)
    def input_monthStaticNum8(self, value):
        self.type(value, self.monthStaticNum8)
    def input_monthStaticNum9(self, value):
        self.type(value, self.monthStaticNum9)
    def input_monthStaticNum10(self, value):
        self.type(value, self.monthStaticNum10)
    def input_monthStaticNum11(self, value):
        self.type(value, self.monthStaticNum11)
    def input_monthStaticNum12(self, value):
        self.type(value, self.monthStaticNum12)

    def uploadFile_fileMonth1(self, path):
        return self.upload_file(self.fileMonth1, path)
    def uploadFile_fileMonth2(self, path):
        return self.upload_file(self.fileMonth2, path)
    def uploadFile_fileMonth3(self, path):
        return self.upload_file(self.fileMonth3, path)
    def uploadFile_fileMonth4(self, path):
        return self.upload_file(self.fileMonth4, path)
    def uploadFile_fileMonth5(self, path):
        return self.upload_file(self.fileMonth5, path)
    def uploadFile_fileMonth6(self, path):
        return self.upload_file(self.fileMonth6, path)
    def uploadFile_fileMonth7(self, path):
        return self.upload_file(self.fileMonth7, path)
    def uploadFile_fileMonth8(self, path):
        return self.upload_file(self.fileMonth8, path)
    def uploadFile_fileMonth9(self, path):
        return self.upload_file(self.fileMonth9, path)
    def uploadFile_fileMonth10(self, path):
        return self.upload_file(self.fileMonth10, path)
    def uploadFile_fileMonth11(self, path):
        return self.upload_file(self.fileMonth11, path)
    def uploadFile_fileMonth12(self, path):
        return self.upload_file(self.fileMonth12, path)

    def click_saveButton(self):
        self.click(self.saveButton)
    def click_submitButton(self):
        self.click(self.submitButton)
    def click_modifyButton(self):
        self.click(self.modifyButton)

    def getAttr_fileMonth1(self):
        return self.getAttribute(self.fileMonth1,"style")
    def getAttr_fileMonth2(self):
        return self.getAttribute(self.fileMonth2,"style")
    def getAttr_fileMonth3(self):
        return self.getAttribute(self.fileMonth3,"style")
    def getAttr_fileMonth4(self):
        return self.getAttribute(self.fileMonth4,"style")
    def getAttr_fileMonth5(self):
        return self.getAttribute(self.fileMonth5,"style")
    def getAttr_fileMonth6(self):
        return self.getAttribute(self.fileMonth6,"style")
    def getAttr_fileMonth7(self):
        return self.getAttribute(self.fileMonth7,"style")
    def getAttr_fileMonth8(self):
        return self.getAttribute(self.fileMonth8,"style")
    def getAttr_fileMonth9(self):
        return self.getAttribute(self.fileMonth9,"style")
    def getAttr_fileMonth10(self):
        return self.getAttribute(self.fileMonth10,"style")
    def getAttr_fileMonth11(self):
        return self.getAttribute(self.fileMonth11,"style")
    def getAttr_fileMonth12(self):
        return self.getAttribute(self.fileMonth12,"style")
    def getAttr_monthStaticNum1(self):
        return self.getAttribute(self.monthStaticNum1,"readonly")
    def getAttr_monthStaticNum2(self):
        return self.getAttribute(self.monthStaticNum2,"readonly")
    def getAttr_monthStaticNum3(self):
        return self.getAttribute(self.monthStaticNum3,"readonly")
    def getAttr_monthStaticNum4(self):
        return self.getAttribute(self.monthStaticNum4,"readonly")
    def getAttr_monthStaticNum5(self):
        return self.getAttribute(self.monthStaticNum5,"readonly")
    def getAttr_monthStaticNum6(self):
        return self.getAttribute(self.monthStaticNum6,"readonly")
    def getAttr_monthStaticNum7(self):
        return self.getAttribute(self.monthStaticNum7,"readonly")
    def getAttr_monthStaticNum8(self):
        return self.getAttribute(self.monthStaticNum8,"readonly")
    def getAttr_monthStaticNum9(self):
        return self.getAttribute(self.monthStaticNum9,"readonly")
    def getAttr_monthStaticNum10(self):
        return self.getAttribute(self.monthStaticNum10,"readonly")
    def getAttr_monthStaticNum11(self):
        return self.getAttribute(self.monthStaticNum11,"readonly")
    def getAttr_monthStaticNum12(self):
        return self.getAttribute(self.monthStaticNum12,"readonly")