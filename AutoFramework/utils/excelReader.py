#coding=utf-8
from xlrd import open_workbook
from AutoFramework.utils.configReader import DATA_PATH
import os

def getTestData(moduleName):
    '''
    获取excel中与模块名相同sheet，并返回以行为单位的列表
    比如 excel中有3行，第一行是标题，后续是内容
    name,class
    fiona,2
    jessie,3
    返回列表为：
    [{name:fiona,class:2},{name,jessie,class:3}]
    :param moduleName:
    :return:

    '''
    excelfile = open_workbook(DATA_PATH + os.sep + "testData.xlsx")
    sheetName = moduleName
    sheet = excelfile.sheet_by_name(sheetName)
    rownum = sheet.nrows
    colnum = sheet.ncols
    titleRow = sheet.row_values(0)
    # print(titleRow)
    dataContainer = []
    for index in range(1, rownum):
        dataContainer.append(dict(zip(titleRow, sheet.row_values(index))))
    # print(dataContainer[1]['搜索关键字'])
    return (dataContainer,rownum)

# (data,num)=getTestData("BaiduOper")
# print(data)
# print(num)