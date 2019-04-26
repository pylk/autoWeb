# coding=utf-8
import inspect
import re
import unittest
import os

from HTMLReport import HTMLReport
from xlrd import open_workbook
from AutoFramework.utils.configReader import DATA_PATH, LOG_PATH
from functools import wraps
import time

from AutoFramework.utils.excelReader import getTestData
from AutoFramework.utils.regularExp import REoperation
import datetime



def getModuleName():
    '''
    获取模块的名称
    :return:
    '''
    # last = inspect.stack()
    modulePath=inspect.stack()[1][1]
    os.path.basename(modulePath)
    moduleFile=os.path.basename(modulePath)
    modulename=moduleFile.split(".")[0]
    # print("last is:",last)
    # print("modulePath:",modulePath)
    # print("moduleFile:", moduleFile)
    # print("modileName:", modulename)
    return modulename


def getMethodName():
    '''
    获取当前方法的名称
    :return:
    '''
    # print('methodName :'+inspect.stack()[1][3])
    return inspect.stack()[1][3]


def getLastMethodName(num=2):
    '''
    获取当前方法的名称
    :return:
    '''
    # print('methodName :'+inspect.stack()[1][3])
    return inspect.stack()[int(num)][3]

def removeDir(dirPath):
    '''
    删除目录
    :param dirPath:
    :return:
    '''
    if not os.path.isdir(dirPath):
        return
    files = os.listdir(dirPath)
    try:
        for file in files:
            filePath = os.path.join(dirPath, file)
            if os.path.isfile(filePath):
                os.remove(filePath)
            elif os.path.isdir(filePath):
                removeDir(filePath)
        os.rmdir(dirPath)
    except Exception:
        print(Exception)

# class dataIter():
#     def __init__(self,seleniumdriver):
#         self.driver=seleniumdriver
#         (self.data, self.rownum) = ([1,2,3],4)
#
#     def __call__(self,func):
#         @wraps(func)
#         def wrapParam(*args,**kwargs):
#             if self.rownum <= 2:
#                 print('one time')
#                 return func(*args,**kwargs)
#             elif self.rownum > 2:
#                 for i in range(0, self.rownum - 1):
#                     func(i)
#                 # return func(i)
#         return wrapParam


def delFile(path):
    if os.path.exists(path):
        os.remove(path)
    else:
        print("file not exist")

def delFileByRegx(path,str):
    files=os.listdir(path)
    for name in files:
        result = re.search(str, name)
        if result and os.path.exists(path+os.sep+name):
            os.remove(path+os.sep+name)
        else:
            continue


def delFileExceptByRegx(path,str):
    files=os.listdir(path)
    for name in files:
        result = re.search(str, name)
        if result and os.path.exists(path+os.sep+name):
            continue
        else:
            os.remove(path + os.sep + name)

def findFileByRegx(path,str):
    files=os.listdir(path)
    for name in files:
        result = re.search(str, name)
        if result and os.path.exists(path+os.sep+name):
            return name




def getCsvData(filePath):
    #filePath=DATA_PATH+os.sep+"batch_adds.csv"
    list=[]
    tempContent=[]
    f=open(filePath,"r",encoding="utf-8")
    lines=f.readlines()
    for line in lines:
            tempContent.append(line.strip().split(","))
    # print(tempContent)
    return tempContent



def timeAround(type='day',delta=1,format="%Y-%m-%d %H:%M:%S"):
    '''
    时间加减函数,按照当前时间加减并格式输出
    :param type: day,hour,minite,second
    :param delta:
    :return:
    '''
    curT=datetime.datetime.now()
    timeSpace=None
    if type=="day":
        timeSpace=datetime.timedelta(days=delta)
    elif type=="minite":
        timeSpace = datetime.timedelta(minutes=delta)
    elif type=="second":
        timeSpace=datetime.timedelta(seconds=delta)
    else:
        print("no such type")

    newT=curT+timeSpace
    return (curT.strftime(format),newT.strftime(format))



def killProcess(processName):
    import os
    import platform
    command=""
    if "windows".lower() in platform.platform().lower():
        command = "taskkill /F /IM " +processName
    elif "linux".lower() in platform.platform().lower():
        command ="killall "+ processName
    os.system(command)


if __name__=="__main__":
    print(findFileByRegx(DATA_PATH, 'hs_code_admin'))

    getModuleName()





