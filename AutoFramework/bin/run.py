import subprocess
import unittest
import time
import os
from HTMLReport import HTMLReport
from AutoFramework.HTMLTestRunnerCN.python3x import HTMLTestReportCN
from selenium import webdriver
from AutoFramework.utils.configReader import CONFIG_FILE, LOG_PATH,CHROMEDRIVER
from AutoFramework.utils.yamlReader import YamlReader


class RunTests(unittest.TestCase):
    """description of class"""

    def __init__(self):
        super(RunTests,self).__init__()
        self.testSuitlist = YamlReader(CONFIG_FILE).data["testSuit"]["baseLine"]
        suitNum=len(self.testSuitlist)


    # use nosetests command to execute test case list
    def LoadAndRunTestCases(self):
        curTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
        path = os.path.dirname(LOG_PATH + os.sep)
        name = 'testReport' + str(curTime)
        suite = unittest.TestSuite()
        runner = HTMLReport.TestRunner(name, path)
        # runner = HTMLTestReportCN.HTMLTestRunner.TestRunner(name, path)

        for testSet in sorted(self.testSuitlist):
            url=self.testSuitlist[testSet]["url"]
            driverType=self.testSuitlist[testSet]["browserType"]
            print(driverType+"###"+url)

            d=None
            if driverType=="chrome":
                d=webdriver.Chrome(executable_path=CHROMEDRIVER)
            d.get(url)

            testCases=self.testSuitlist[testSet]["caseSet"]



            for case in testCases:
                print(case)

            d.get("about:")
                    # print(case)
                    # subprocess.call("nosetests " + str(item).replace("\\n", ""), shell=True)
                    # python - m  AutoFramework.bin.mySuite
                    # C:\Users\kevin\PycharmProjects\AutoFramework


if __name__ == "__main__":
    newrun = RunTests()
    newrun.LoadAndRunTestCases()