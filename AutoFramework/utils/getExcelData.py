# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import xlrd
from AutoFramework.utils.configReader import EXL_PATH
'''
----------------- 通过sheet name 取excel里面的某行数据；或者取 excel里面一个单元格的数据！ ----------------
'''
class getExcelData :
    # 定义3个类里面的 全局变量，file=excel路径；取第（n+1）个sheet， 取值第i行
    file= 'file.xlsx'    # ####文件路径
    sheetname='bugfree'  # ### 第n sheet
    i=1   # 第 i行

    def getRow(self):   #取第i行的所有数据
        exl= xlrd.open_workbook(self.file)
        # sheetn=exl.sheet_by_index(self.n)   # 通过 sheet index 定位sheet
        sheetn=exl.sheet_loaded(self.sheetname)  #通过 sheet name或者index 定位 sheet   ！！！！好用 ！
        rvi=sheetn.row_values(self.i)   #取第i 行的数据
        return rvi


    def getbyColName(self,colname):   # 取第i行，colname列的一个单元格数据
        exl= xlrd.open_workbook(self.file)
        sheetn=exl.sheet_by_name(self.sheetname)
        colnames=sheetn.row_values(0) #列名在第一行, 取列名
        rvi=sheetn.row_values(self.i)   #取第i 行的数据
        app={}
        for j in range(0,len(colnames)):
            app[colnames[j]] =rvi[j]
        #print(app)
        aix=app[colname]
        #print(aix)
        return aix


if __name__ == '__main__':   #如果是跑本py文件，则执行下面这一段代码，如果是其他文件调用本文件的方法函数类，则不执行以下代码段；
   ge=getExcelData()     #实例化一个类
   ge.sheetname='bugfree'     # sheetname 为 xxxx 的sheet
  # ge.file='E:\SeleniumData.xlsx'      ###############定义excel路径############
   ge.file=EXL_PATH
   #ge.i 定义取哪一行数据
   for j in range(1,3):    #例如 取1-2行值s
       ge.i=j
       uname=ge.getbyColName('uname')
       upwd=ge.getbyColName('upwd')
       print(uname+' '+upwd)
