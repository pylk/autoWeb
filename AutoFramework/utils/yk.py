# import mysql.connector
#
# # mysql1.py
# config = {
#     'host': '127.0.0.1',
#     'user': 'root',
#     'password': '123456',
#     'port': 3306,
#     'database': 'sakila',
#     'charset': 'utf8'
# }
# try:
#     cnn = mysql.connector.connect(**config)
# except mysql.connector.Error as e:
#     print('connect fails!{}'.format(e))
# cursor = cnn.cursor()
# try:
#     sql_query = 'SELECT city,last_update FROM `city` LIMIT 10;'
#     cursor.execute(sql_query)
#     for city,last_update in cursor:
#         print (city,last_update)
# except mysql.connector.Error as e:
#     print('query error!{}'.format(e))
# finally:
#     cursor.close()
#     cnn.close()



# coding: utf-8
#python 连接webservice接口
import suds
client = suds.client.Client('http://www.webxml.com.cn/WebServices/IpAddressSearchWebService.asmx?wsdl')
print(client)
res=client.service["IpAddressSearchWebServiceSoap"].getCountryCityByIp("8.8.8.8")
print(res)


res1=client.service['OtherBLZService']['soap'].getBank()
print(res1)