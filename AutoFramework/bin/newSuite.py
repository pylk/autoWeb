#coding=utf-8
import os
import subprocess

import time

from AutoFramework.utils.configReader import YamlReader,BASE_PATH,LOG_PATH
import sys, getopt


'''
    使用nose测试框架集成测试套件
newSuite.py目前只能执行baseLine，如需执行all或者debug模式，可以在运行时用命令行的方式
如下：
python AutoFramework.bin.newSuite -m "debug" -n "debug"
-m 参数代表运行那个模块，如all, debug，只要在配置文件config.yml配置了相应用例即可。
-n 参数代表报告的名字
'''


opts, args = getopt.getopt(sys.argv[1:], "hm:n:")
runModule="baseLine"
reportName="baseLine"

for op, value in opts:
    if op == "-m":
        runModule = value
    elif op == "-n":
        reportName = value
    elif op == "-h":
        print("你需要输入格式为：newSuite.py runModle(eg:all/debug) reportName(eg:test)!!")
        sys.exit()

conf=YamlReader().data
caseList=conf['suite'][runModule]
print(caseList)
print(",".join(caseList))

try:
    testList=",".join(caseList)
    caseDir = os.path.join(BASE_PATH, "testcase")
    caseDir = caseDir + os.sep
    os.chdir(caseDir)
    print(os.path.abspath(os.path.curdir))
    print("".join(testList))
    # subprocess.call("nosetests --tests=" + testList + " --with-html --html-out-file=20171017Report4.html --plugins=[HtmlOutput()] --force-flaky --max-runs=3 --min-passes=1")
    # # 大报告
    # reportName=LOG_PATH+os.sep+"Report_debug2.html"
    rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    subprocess.call("nosetests --tests=" + testList + " --with-html --html-file="+reportName+rq+"_Report.html --html-template-file=//reportTemp/report2.jinja") #--force-flaky --max-runs=2")
    print("test finished!!!")
    "+LOG_PATH+os.sep+"
    subprocess.call("nosetests -w "+caseDir+" --tests "+"".join(caseList)+" --collect-only -v")
    # 小报告
    run(argv=['nosetests', '--with-html-output', '--html-out-file=result.html', '--tests=' + testList], plugins=[HtmlOutput()])
except Exception as e:
    print(str(e))




# subprocess.call("nosetests "+"-w //A_trash/testcase/"+"--with-html --html-file=//logs/myReport.html --html-template-file=//reportTemp/report2.jinja" )
# nosetests test_oper/ --with-html --html-file=myReport.html --html-template-file=AutoFramework/reportTemp/report2.jinja --force-flaky --max-runs=2
# nosetests test_oper/ --with-html --html-file=logs/myReport.html --html-template-file=AutoFramework/reportTemp/report2.jinja








