20170901
目录介绍
bin 调用业务流程，引用unittest进行执行
business 继承core.pom.py,封装页面*Obj.py，及其元素操作*Oper.py，并组合程业务流程test_Transaction.py
config 配置全局变量，后期引用，目前未封装
core 页面封装类，作为页面类的基类，封装了selenium的操作
logs 输出执行日志和截图，并生成报告的目录
testData 测试数据，目前未想好引用方式
utlis 工具类，包含了日志打印，截图，ssh连接，ftp类

20170906
business中用例名称不统一--未修改
特殊用例和共有用例区分--无
发送邮件--无
数据读取--无 根据用例读取，还是用例集读取执行
用例是否执行配置文件，用例名称规范，用例筛选过滤，unittest resolve方法
数据库效验的utils类未编写（根据数据库类型）
定时任务，结合unittest没有做

20170907
添加drvers目录，用来存放驱动程序
testData目录，准备用yaml格式数据进行数据的管理，用到pyyaml模块，运行中的
信息也可以用load导入到yaml文件

20170920
命令行执行方式
进入AutoFramework目录，执行python -m AutoFramework.bin.mySuite，产生报告和日志和截图
进入AutoFramework目录，python -m unittest AutoFramework.bin.mySuite，无报告。原因是在mySuite.py中unittest不执行__name__==__"main"__以后的代码
nosetests AutoFramework.bin.mySuite
nosetests AutoFramework.bin.mySuite --with-html --html-file=myReport.html --html-template-file=AutoFramework/reportTemp/report2.jinja

#运行环境
chrome61 , driver 2.32
firefox 52.4, driver 0.17

