#coding=utf-8
import paramiko
from AutoFramework.utils.logger import Logger

# logger=Logger(logger="Connector").getlog()

class FtpConnector():
    def __init__(self,ip,port,username, passwd):
        self.ip=ip
        self.port=int(port)
        self.conn=""
        conn = paramiko.Transport(self.ip, self.port)
        conn.connect(username, passwd)
        ftpConn = paramiko.SFTPClient.from_transport(conn)
        self.conn = ftpConn

    def getFtpConnection(self,username,passwd):
        conn=paramiko.Transport(self.ip,self.port)
        conn.connect(username,passwd)
        ftpConn=paramiko.SFTPClient.from_transport(conn)
        self.conn=ftpConn

    def download(self,remotePath,localPath):
        self.conn.get(remotePath, localPath)

    def upload(self,localPath,remotePath):
        self.conn.put(localpath=localPath, remotepath=remotePath)

    def closeFtpConnection(self):
        self.conn.close()








class RemoteConnector():
    def __init__(self,ip,port):
        self.ip = ip
        self.port = int(port)
        self.connection=""

    def getKeyConnection(self,user,key_path,key_password):
        self.username=user
        self.keyPath=key_path
        self.keyPasswd=key_password
        # 指定本地的RSA私钥文件,如果建立密钥对时设置的有密码，password为设定的密码，如无不用指定password参数
        pkey = paramiko.RSAKey.from_private_key_file(self.keyPath, self.keyPasswd)
        # 建立连接
        trans = paramiko.Transport(self.ip, self.port)
        trans.connect(self.username, pkey=pkey)
        # 将sshclient的对象的transport指定为以上的trans
        ssh = paramiko.SSHClient()
        ssh._transport = trans
        self.connection=ssh

    def getCredentialConnection(self,username,password):
        self.username=username
        self.password=password
        trans = paramiko.Transport(self.ip, self.port)
        # 建立连接
        trans.connect(username=self.username, password=self.password)

        # 将sshclient的对象的transport指定为以上的trans
        ssh = paramiko.SSHClient()
        ssh._transport = trans
        self.connection=ssh


    def exeCommand(self,command):
        # 执行命令，和传统方法一样
        stdin, stdout, stderr = self.connection.exec_command(command)
        output=stdout.read().decode()
        error=stderr.read().decode()
        if error!="":
            print("command error: \n" + error)
        return output
        # logger.info("command output: \n" + output)
        # if error!="":
            # logger.error("command error: \n" + error)


    def freeConnection(self):
        self.connection.close()

if __name__=="__main__":
    c=RemoteConnector("192.168.56.104",22)
    c.getCredentialConnection("root","kevin")
    c.exeCommand("ls /etc")
    c.freeConnection()