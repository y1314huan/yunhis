#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb
#连接MySQL数据库， 其中，host为mysql的IP，因为我是本机的mysql，所以ip为127.0.0.1，port为默认端口3306，db即为要操作的数据库
conn = MySQLdb.connect(host='60.205.106.190', port=3306, user='root', passwd='oasisadmin', db='oasis_his', charset='utf8')



#退费之前的上一个账单的保险支付金额
cursor = conn.cursor()
#执行查询
rowNums = cursor.execute('SELECT SUM(beforinsurancemoney) FROM phy_refund where clinicid = 100000002 and modifytime >= "2017-12-01 00:00:00"')
#并获取查询的总行数：
print('查询的行数为' + str(rowNums))
#遍历结果，获取查询的结果
selectResultList = cursor.fetchall()
print str(selectResultList)
Str = str(selectResultList)
ZJ=Str.replace("((Decimal('","")
Befor=ZJ.replace("'),),)","")
print Befor


#退费时剩余未退费账单保险支付的金额
cursor = conn.cursor()
#执行查询
rowNums = cursor.execute('SELECT SUM(insurancemoney) FROM phy_refund where clinicid = 100000002 and modifytime >= "2017-12-01 00:00:00" ')
#并获取查询的总行数：
print('查询的行数为' + str(rowNums))
#遍历结果，获取查询的结果
selectResultList = cursor.fetchall()
print str(selectResultList)
Str = str(selectResultList)
ZJ1=Str.replace("((Decimal('","")
Insur=ZJ1.replace("'),),)","")
print Insur





# 从数据库中获取本次的退款金额（不含保险退的）
cursor = conn.cursor()
rowNums = cursor.execute('SELECT SUM(actualmoney) FROM phy_refund where clinicid = 100000002 and modifytime >= "2017-12-01 00:00:00"')#本次的退款金额（不含保险退的）
# 并获取查询的总行数：
print('查询的行数为' + str(rowNums))
# 遍历结果，获取查询的结果
selectResultList = cursor.fetchall()
print str(selectResultList)
str = str(selectResultList)
bef = str.replace("((Decimal('", "")
aft = bef.replace("'),),)", "")
num = float(aft)
print aft





#进行查询，首先要获取游标
# cursor = conn.cursor()
# #执行查询
# rowNums = cursor.execute('SELECT SUM(beforinsurancemoney)-SUM(insurancemoney)+SUM(actualmoney) FROM phy_refund where clinicid = 100000002 and modifytime >= "2017-12-01 00:00:00"')
# #并获取查询的总行数：
# print('查询的行数为' + str(rowNums))
# #遍历结果，获取查询的结果
# selectResultList = cursor.fetchall()
# print str(selectResultList)
# S = str(selectResultList)
# Q=S.replace("((Decimal('","")
# K=Q.replace("'),),)","")
# print K
