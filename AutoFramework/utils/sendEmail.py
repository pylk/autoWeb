# -*- coding:utf-8 -*-
# author:isyuan
# datetime:26/03/2019 14:53
# software: PyCharm
"""
import time
import os
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


class SendEmail:
    def __init__(self):
        self.report_dir = r'C:\Software\pycharm\stu\python\scripts\AutoWeb\AutoFramework\testReport'
        self.sendUser = "isscal@sina.com"
        self.sendPswd = 'haoran2014'
        self.receUser = 'isscal@163.com'
        self.stmp = "smtp.sina.com"
        self.now = time.strftime('%Y-%m-%d_%H-%M-%S')

    def send_mail(self):
        '''
        :param new_report:获取最新的文件
        :param now:当前生成报告的时间
        :return:
        '''
        # 获取路径下的所有文件
        self.lists = os.listdir(self.report_dir)
        # 获取最新的文件
        self.newReport = self.lists[-1]
        # 打开文件
        os.chdir(self.report_dir)
        self.f = open(self.newReport, 'rb')

        self.body_main = self.f.read()

        self.msg = MIMEMultipart()
        # 邮件标题
        self.msg['Subject'] = Header('自动化测试报告', 'utf-8')
        self.msg['From'] = self.sendUser
        self.msg['To'] = self.receUser
        # 邮件内容
        self.text = MIMEText(self.body_main, 'html', 'utf-8')
        self.msg.attach(self.text)

        # 发送附件
        self.att = MIMEApplication(open(self.newReport, 'rb').read())
        self.att['Content-Type'] = 'application/octet-stream'
        self.att.add_header('Content-Disposition', 'attachment', filename=('utf-8', '', self.now + "_report.html"))
        self.msg.attach(self.att)


        try:
            self.smtp = smtplib.SMTP()
            self.smtp.connect(self.stmp)
            self.smtp.login(self.sendUser, self.sendPswd)
            self.smtp.sendmail(self.sendUser, self.sendPswd, self.msg.as_string())
            self.smtp.close()
        except smtplib.SMTPException as e:
            print ("Error: 无法发送邮件", e)




    def useTime(self):
        self.startime = time.strftime("%H:%M:%S")
        print("开始时间为：%s" % self.startime)
        self.sendEmail = SendEmail()
        self.sendEmail.send_mail()
        self.endTime = time.strftime("%H:%M:%S")
        print("结束时间为：%s" % self.startime)


se = SendEmail()
se.useTime()

"""

import time
import os
import smtplib

from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


def send_mail():
    report_dir = r'C:\Software\pycharm\stu\python\scripts\AutoWeb\AutoFramework\testReport'
    senduser = 'isscal@163.com'
    sendpswd = '813312'
    receuser = '324598922@qq.com'

    lists = os.listdir(report_dir)
    #获取最近时间的
    new_report = lists[-1]
    os.chdir(report_dir)
    f = open(new_report,'rb')
    body_main = f.read()

    msg = MIMEMultipart()
    # 邮件标题
    msg['Subject'] = Header('自动化测试报告','utf-8')
    msg['From'] = senduser
    msg['To'] = receuser
    #邮件内容
    text = MIMEText(body_main,'html','utf-8')
    msg.attach(text)

    #发送附件
    att = MIMEApplication(open(new_report, 'rb').read())
    # att = MIMEText(sendfile, 'base64', 'utf-8')
    att['Content-Type'] = 'application/octet-stream'
    att.add_header('Content-Disposition', 'attachment', filename=('utf-8', '',now + "_report.html"))
    msg.attach(att)

    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com')
    smtp.login(senduser,sendpswd)
    smtp.sendmail(senduser,receuser,msg.as_string())


if __name__ == '__main__':
    startime = time.strftime('%H:%M:%S')
    print("开始时间为：%s" % startime)
    now = time.strftime('%Y-%m-%d_%H-%M-%S')
    send_mail()
    endtime = time.strftime('%H:%M:%S')
    print("结束时间为：%s" %endtime)
