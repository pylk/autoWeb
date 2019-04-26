#-*- coding:utf-8 -*-
# author:isyuan
# datetime:22/03/2019 16:42
# software: PyCharm
from AutoFramework.testobject.baidu_obj import BaiduObj
import unittest
from AutoFramework.utils.configReader import YamlReader,getDriver
import pysnooper

class Test_baidu_login(unittest.TestCase):
    def setUp(self):
        self.d= getDriver()
        self.d.get(YamlReader().data['BAIDU']['INFO']['url'])
        self.login=BaiduObj(self.d)
        self.conf=YamlReader().data

    @pysnooper.snoop()#通过装饰器debug函数变量值
    def test_baidu_login(self):
        user=self.conf['BAIDU']['INFO']['user']
        passwd=self.conf['BAIDU']['INFO']['pass']
        self.login.bdLogin(user,passwd)
        self.assertEqual(2,2,"testError")

    def tearDown(self):
        self.d.quit()

#todo: 1.通过unittest.main()来执行单个测试用例的方式

if __name__ == '__main__':
    unittest.main()


#todo:2.通过testsuit来选择执行测试用例的方式

# if __name__ == "__main__":
#     # 构造测试集
#     suite=unittest.TestSuite()
#     suite.addTest(Test_baidu_login("test_baidu_login"))
#     # 执行测试
#     runner=unittest.TextTestRunner()
#     runner.run(suite)


#todo:3.通过testLoader 逐一添加测试脚本

# if __name__ == "__main__":
#     suite1=unittest.TestLoader().loadTestsFromTestCase(Test_baidu_login)
#     suite=unittest.TestSuite([suite1])
#     unittest.TextTestRunner(verbosity=2).run(suite)

#todo:4、通过TestLoader 类中提供的discover（）选择用例文件目录

# if __name__ == '__main__':
#     suite=unittest.defaultTestLoader.discover(r"C:\Software\pycharm\stu\python\scripts\AutoWeb\AutoFramework\testcase","test_*.py")
#     unittest.TextTestRunner().run(suite)





