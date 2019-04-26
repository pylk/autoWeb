#coding:utf8
from AutoFramework.utils.Connector import RemoteConnector
from AutoFramework.utils.mail import sendMail


def check_all(ip,float_cpu_threshold=90.0,float_disk_threshold=90.0,float_mem_threshold=90.0):
    '''
    河南项目服务器检查
    author:oupeng
    :param ip:
    :return:
    '''
    result = []

    result.append("########## ip: "+ip+" ######")
    c=RemoteConnector(ip,22)
    c.getCredentialConnection("root","1234567")


    cpu=c.exeCommand(''' vmstat |grep '[0-9]'|awk '{print $15}' ''')
    cpu=str(100-float(cpu.strip()))
    if float(cpu)>float(float_cpu_threshold):
        result.append("ERROR: cpu large than threshold "+cpu)
    else:
        result.append("INFO: "+cpu+" cpu ok...........")
    # print("free cpu utilization: \n",cpu)



    mem=c.exeCommand(''' free -g|grep Mem|awk '{print $3/$2*100}'  ''')
    mem=str(mem.strip())
    if float(mem)>float(float_mem_threshold):
        result.append("ERROR: mem large than threshold "+cpu)
    else:
        result.append("INFO: "+mem+" mem ok...........")




    disk=c.exeCommand("df -h|sed -n '/\/dev/p'|awk '{print $5}'|grep -oE '[0-9]+'")
    dList=disk.strip().split('\n')
    for one in dList:
        if float(one) > float(float_disk_threshold):
            result.append("ERROR: disk large than threshold "+one)
        else:
            result.append("INFO: "+one+" disk ok.........")
    # print("used disk utilization: \n",dList)


    mysqlProcess=c.exeCommand('''ps -ef|grep -E '^mysql'|grep -v grep|awk '{printf "%s %s\\n",$1,$2}' ''')
    # mysqlProcess=mysqlProcess.strip()
    result.append("INFO: process mysql is: \n"+mysqlProcess)

    tomcatProcess=c.exeCommand('''ps -ef|grep tomcat-808|grep -v grep|awk '{printf "%s %s\\n",$1,$2}' ''')
    result.append("INFO: process tomcat is: \n"+tomcatProcess)

    nginxProcess=c.exeCommand(''' ps -ef|grep nginx|grep master|grep -v grep|awk '{printf "%s %s\\n",$1,$2}' ''')
    result.append("INFO: process nginx is: \n"+nginxProcess)

    imdgProcess=c.exeCommand(''' ps -ef|grep hazelcast|grep java|awk '{printf "%s %s\\n",$1,$2}' ''')
    result.append("INFO: process IMDG is: \n"+imdgProcess)
    #missing check IMDG
    c.freeConnection()

    return result




list=["10.80.73.2",
      # "10.80.73.3",
      # "10.80.73.4",
      # "10.80.73.5",
      # "10.80.73.6",
      # "10.80.73.7",
      # "10.80.73.8",
      # "10.80.73.9",
      # "10.80.73.10",
      # "10.80.73.11",
      # "10.80.73.12",
      # "10.80.73.13",
      "10.80.73.14"
      ]


all=""
flag=False
for one in list:
    ret=check_all(one)
    print(ret)
    # 判断是否又超出阈值
    # for check in ret:
    #     if "".join(check).startswith("ERROR:"):
    #         flag=True
    all=all+"\n".join(ret)
    all=all+"\n\n"

# print(flag)
# print(all)

# sendMail(all,mailto="yu1.wang@epro.com.cn")








