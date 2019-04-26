import pymysql
from AutoFramework.utils.configReader import YamlReader
# conn=pymysql.connect(host='192.168.56.10',port=3306,
#                      user='root',passwd='123456',db='mysql',charset='utf8')
# cur=conn.cursor()
# cur.execute("select version()")
# for i in cur:
#     print(i)
# cur.close()
# conn.close()


class mysqlSearch():
    def __init__(self,host,port,user,passwd,db,charset="utf8"):
        self.host=host
        self.port=port
        self.user=user
        self.passwd=passwd
        self.db=db
        self.charset=charset
        self.conn=pymysql.connect(host=self.host,port=int(self.port),user=self.user,passwd=self.passwd,db=self.db,charset=self.charset)
        self.cur = self.conn.cursor()

    def doSearch(self,sql="select version()"):
        resArry=[]
        self.cur.execute(sql)
        for i in self.cur:
            resArry.append(i)
        return resArry

    def doUpdate(self,sql=""):
        pass

    def doDelete(self,sql=""):
        pass

    def doInseart(self,sql="",textPath=""):
        pass

    def __del__(self):
        self.cur.close()
        self.conn.close()

if __name__=='__main__':
    conf = YamlReader().data
    # print(conf["mysqldb"]["ip"],conf["mysqldb"]["port"],conf["mysqldb"]["username"],conf["mysqldb"]["password"])
    conn=mysqlSearch(conf["mysqldb"]["ip"],conf["mysqldb"]["port"],conf["mysqldb"]["username"],conf["mysqldb"]["password"],conf["mysqldb"]["defaultDB"])
    print(conn.doSearch(sql=conf["dbQueries"]["statisticSearch"]["sql"]))
    # print(conn.doSearch())