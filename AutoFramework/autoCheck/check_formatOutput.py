#coding:utf8
import csv,codecs

import time

from AutoFramework.utils.Connector import RemoteConnector
from AutoFramework.utils.mail import sendMail,sendMailWithTextAttach


def check_all(ip,float_cpu_threshold=90.0,float_disk_threshold=90.0,float_mem_threshold=90.0):
    '''
    河南项目服务器检查
    author:oupeng
    :param ip:
    :return:
    '''
    totoalResult = []
    ipRet=[]
    cpuRet=[]
    memRet = []
    swapRet=[]
    diskRet = []
    mysqlRet = []
    tomcatRet = []
    nginxRet = []
    imdgRet = []

    ipRet.append("IP: "+ip)
    c=RemoteConnector(ip,22)
    c.getCredentialConnection("root","1234567")


    # cpu=c.exeCommand("top -bn 1|sed -n '/^Cpu/p'|awk '{print $5}'|grep -oE '[0-9]+\.[0-9]+'")
    cpu=c.exeCommand(''' vmstat |grep '[0-9]'|awk '{print $15}' ''')
    cpu=str(100-float(cpu.strip()))
    if float(cpu)>float(float_cpu_threshold):
        cpuRet.append("ERROR CPU: "+cpu)
    else:
        cpuRet.append("CPU: "+cpu)
    # print("free cpu utilization: \n",cpu)



    mem=c.exeCommand(''' free -g|grep Mem|awk '{print $3/$2*100}'  ''')
    mem=str(mem.strip())
    if float(mem)>float(float_mem_threshold):
        memRet.append("ERROR MEM: "+mem)
    else:
        memRet.append("MEM: "+mem)


    swap=c.exeCommand(''' free -g|grep Swap|awk '{print $3/$2*100}'  ''')
    swap=str(swap.strip())
    if float(swap)>float(float_mem_threshold):
        swapRet.append("ERROR SWAP: "+swap)
    else:
        swapRet.append("SWAP: "+swap)



    disk=c.exeCommand("df -h|sed -n '/\/dev/p'|awk '{print $5}'|grep -oE '[0-9]+'")
    dList=disk.strip().split('\n')
    for one in dList:
        if float(one) > float(float_disk_threshold):
            diskRet.append("ERROR DISK: "+one)
        else:
            diskRet.append("DISK: "+one)
    # print("used disk utilization: \n",dList)


    mysqlProcess=c.exeCommand('''ps -ef|grep -E '^mysql'|grep -v grep|awk '{printf "%s %s\\n",$1,$2}' ''')
    # mysqlProcess=mysqlProcess.strip()

    for one in mysqlProcess.split("\n"):
        if one !="":
            mysqlRet.append("INFO: mysql: "+one)

    tomcatProcess=c.exeCommand('''ps -ef|grep tomcat-808|grep -v grep|awk '{printf "%s %s\\n",$1,$2}' ''')
    for one in tomcatProcess.split("\n"):
        if one != "":
            tomcatRet.append("INFO: tomcat: "+one)

    nginxProcess=c.exeCommand(''' ps -ef|grep nginx|grep master|grep -v grep|awk '{printf "%s %s\\n",$1,$2}' ''')
    for one in nginxProcess.split("\n"):
        if one != "":
            nginxRet.append("INFO: nginx: "+one)

    imdgProcess=c.exeCommand(''' ps -ef|grep hazelcast|grep java|awk '{printf "%s %s\\n",$1,$2}' ''')
    for one in imdgProcess.split("\n"):
        if one != "":
            imdgRet.append("INFO: Imdg: "+one)

    c.freeConnection()

    totoalResult.append(ipRet)
    totoalResult.append(cpuRet)
    totoalResult.append(memRet)
    totoalResult.append(swapRet)
    totoalResult.append(diskRet)
    totoalResult.append(mysqlRet)
    totoalResult.append(tomcatRet)
    totoalResult.append(nginxRet)
    totoalResult.append(imdgRet)

    return totoalResult






def start_check(list):
    all = []
    now= time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    # retHeader="default CPU\MEM\DISK threshold is 90%. data higher than this will marked as ERROR.\nIP_ADDR,CPU util%,MEM util%,DISK util%,MySql,Tomcat,Nignx,IMDG\n"
    retHeader = "Check Time:"+now+"\nCPU，MEM，DISK 默认阈值为90%，超过此值将标记为ERROR。\nIP地址,CPU利用率百分比%,内存利用率百分比%,交换分区利用率%,硬盘利用率百分比%,MySql进程号,Tomcat进程号,Nignx进程号,IMDG进程号\n"
    for one in list:
        ret=check_all(one)
        print(ret)
        # 判断是否又超出阈值
        # for check in ret:
        #     if "".join(check).startswith("ERROR:"):
        #         flag=True
        all.append(ret)

    with codecs.open("formatOutput.csv", "w", encoding='utf_8_sig') as f:
        # fhandle=csv.writer(f)
        f.write(retHeader)
        for server in all:
            # for item in server:
            # tempStr =str(",".join(server))+"\n"
            for item in server:
                if len(item) == 0:
                    f.write(",")
                elif len(item) == 1:
                    f.write(",".join(item) + ",")
                elif len(item) > 1:
                    f.write(" ".join(item) + ",")
            f.write('\n')




list=["10.80.73.2",
      "10.80.73.3",
      "10.80.73.4",
      "10.80.73.5",
      "10.80.73.6",
      "10.80.73.7",
      "10.80.73.8",
      "10.80.73.9",
      "10.80.73.10",
      "10.80.73.11",
      "10.80.73.12",
      "10.80.73.13",
      "10.80.73.14"
      ]
#yu1.wang@epro.com.cn
start_check(list)
sendMailWithTextAttach(subject="服务器巡检结果",content="你好:\n\n详细检查结果请看附件，新增swap",mailto="yu1.wang@epro.com.cn,oupeng@spic.com.cn",attachpath="C:\\Users\\kevin\\PycharmProjects\\Auto\\formatOutput.csv")






