#coding=utf-8
"""
读取配置。这里配置文件用的yaml，也可用其他如XML,INI等，需在file_reader中添加相应的Reader进行处理。
"""
import os
import time
import yaml
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from xlrd import open_workbook


# 之前直接拼接的路径，修改了一下，用现在下面这种方法，可以支持linux和windows等不同的平台，
# os.path.split()和os.path.join()，不要直接+'\\xxx\\ss'这样
BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
# print(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(BASE_PATH, 'config')
CONFIG_FILE=os.path.join(CONFIG_PATH,'config.yml')
DATA_PATH = os.path.join(BASE_PATH, 'testData')
EXL_PATH = os.path.join(DATA_PATH, 'SeleniumData.xlsx')  ## for Angela;
DRIVER_PATH = os.path.join(BASE_PATH, 'drivers')
LOG_PATH = os.path.join(BASE_PATH, 'logs')
PAGE_OBJ_PATH = os.path.join(BASE_PATH, 'testobject')
CASE_PATH=os.path.join(BASE_PATH,'testcase')
CHROMEDRIVER=os.path.join(DRIVER_PATH,'chromedriver.exe')
FIREFOXDRIVER=os.path.join(DRIVER_PATH,'geckodriver.exe')
PHANTOMJSDRIVER=os.path.join(DRIVER_PATH,'phantomjs.exe')
WinRootPath=os.path.abspath('C:')
# REPORT_PATH = os.path.join(BASE_PATH, 'report')
rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))

tmpPath=os.path.join(LOG_PATH,rq)
if not os.path.exists(tmpPath):
    os.mkdir(tmpPath)
LOG_PATH = tmpPath


# def start_selenium_server():
#     if no:
#         os.chdir(DRIVER_PATH)
#         os.subprocess.call("java -jar selenium-server-standalone-3.6.0.jar")



def getDriver(glob="yes",host1="local",type1="chrome",executer1="default from config file"):
    d = None
    host=None
    type=None
    executer=None

    if glob=="yes":
        host=YamlReader().data['global']['host']
        type=YamlReader().data['global']['type']
        executer=YamlReader().data['global']['executer']
    elif glob=="no":
        host=host1
        type=type1
        executer=executer1
    else:
        raise "glob值非法！！"

    if host=="local":
        if type=="chrome":
            options = webdriver.ChromeOptions()
            prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': DATA_PATH}
            options.add_experimental_option('prefs', prefs)
            options.add_argument("--start-maximized")
            d=webdriver.Chrome(executable_path=CHROMEDRIVER,options=options)
            d.maximize_window()
        elif type=="firefox":
            profile=webdriver.FirefoxProfile()
            profile.set_preference("browser.download.folderList",2)
            profile.set_preference("browser.download.manager.showWhenStarting",False)
            profile.set_preference("browser.download.dir",DATA_PATH)
            profile.set_preference("browser.helperApps.neverAsk.saveToDisk","application/json;charset=UTF-8")
            d = webdriver.Firefox(executable_path=FIREFOXDRIVER,firefox_profile=profile)
            d.maximize_window()
        elif type=="phantomjs":
            d = webdriver.PhantomJS(executable_path=PHANTOMJSDRIVER)
            d.maximize_window()
        elif type=="ie":
            d = webdriver.Ie(executable_path="")
            d.maximize_window()
    elif host=="remote":

        if type=="chrome":
            d=webdriver.Remote(command_executor=executer,desired_capabilities=DesiredCapabilities.CHROME)
        elif type=="firefox":
            d = webdriver.Remote(command_executor=executer, desired_capabilities=DesiredCapabilities.FIREFOX)
            d.maximize_window()
        elif type=="phantomjs":
            d = webdriver.Remote(command_executor=executer, desired_capabilities=DesiredCapabilities.PHANTOMJS)
            d.maximize_window()
        elif type=="ie":
            d = webdriver.Remote(command_executor=executer, desired_capabilities=DesiredCapabilities.INTERNETEXPLORER)
            d.maximize_window()
    else:
        raise "host值非法"

    return d









class YamlReader:
    def __init__(self, yamlf=CONFIG_FILE):
        if os.path.exists(yamlf):
            self.yamlf = yamlf
        else:
            raise FileNotFoundError('文件不存在！')
        self._data = None

    @property
    def data(self):
        # 如果是第一次调用data，读取yaml文档，否则直接返回之前保存的数据
        if not self._data:
            with open(self.yamlf, 'rb') as f:
                self._data = list(yaml.safe_load_all(f))  # load后是个generator，用list组织成列表
        return self._data[0]



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