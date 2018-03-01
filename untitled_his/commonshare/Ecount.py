# coding:utf-8
#!/usr/bin/python
# -*- coding: UTF-8 -*-
import datetime
today = datetime.datetime.now()
days = datetime.timedelta(days=1)
n_days = today + days
tom = n_days.strftime('%Y-%m-%d')
now = today.strftime('%Y-%m-%d')
print today.strftime('%Y-%m-%d')
print n_days.strftime('%Y-%m-%d')
fir = today.strftime('%Y-%m-01')
import MySQLdb
#连接MySQL数据库， 其中，host为mysql的IP，因为我是本机的mysql，所以ip为127.0.0.1，port为默认端口3306，db即为要操作的数据库
conn = MySQLdb.connect(host='60.205.106.190', port=3306, user='root', passwd='oasisadmin', db='oasis_his', charset='utf8')
###########当月的数据库统计##########################################################################################################################

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



from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from locale import *





class TestHis(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browser = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")  # chromedriver.exe文件的路径
        global browser
        browser.maximize_window()
        browser.get("http://yun.oasisapp.cn:9080/uc/authentication/check?login=true&phone=&redirectUrl=http://yun.oasisapp.cn:8080/yunhis/security_check.action")
        ## 测试地址


        # browser.get("http://47.93.156.153:9090/uc/authentication/check?login=true&phone=&redirectUrl=http://47.93.156.153:8090/yunhis/security_check.action")
        # # 准正式地址

        time.sleep(2)
    @classmethod
    def tearDownClass(cls):
        # browser.quit()
        time.sleep(2)
        print "TearDown"

    #登录
    def test001(self):
        browser.find_element_by_id("username").clear()  # 清空账号输入框
        browser.find_element_by_id("username").send_keys("17444444444")  # 输入用户名
        browser.find_element_by_id("password").clear()  # 清空密码输入框
        browser.find_element_by_id("password").send_keys("444444")  # 输入密码
        browser.find_element_by_id("loginBtn").click()  # 点击登录
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="#clinics"]/li[2]').click()  # 选择泓华金融街诊所准正式
        time.sleep(5)
        print "登录成功"


    def test_count(self):

###############结算管理-当日#####################################################
        browser.find_element_by_xpath('/html/body/div[3]/aside/section/ul/li[9]/a').click()  # 点击收费、发药
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/ul/li[4]/a').click()  #点击结算管理
        time.sleep(2)
        setlocale(LC_NUMERIC, 'English_US')
        #结算管理-当日保险支付
        baoxian = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/div[3]/table/tfoot/tr/td[8]').text  # 保险
        if baoxian == " ":
            BaoXian = int(0)
        else:
            BaoXian = atof(baoxian)#把带有千位分隔符的浮点数字符串形式转化为数字
        # 结算管理-当日优惠金额
        youhui = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/div[3]/table/tfoot/tr/td[9]').text  #
        if youhui == " ":
            YouHui = int(0)
        else:
            YouHui = atof(youhui)
        # 结算管理-当日实收金额
        shishou = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/div[3]/table/tfoot/tr/td[10]').text  #
        if shishou == " ":
            ShiShou = int(0)
        else:
            ShiShou = atof(shishou)

        #结算管理-当日退费
        tuifei = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/div[3]/table/tfoot/tr/td[11]').text  #
        if tuifei == " ":
            TuiFei = int(0)
        else:
            TuiFei = atof(tuifei)
        bxtuifei= browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/div[3]/table/tfoot/tr/td[12]').text  #

        if bxtuifei == " ":
            BXTuiFei = int(0)
        else:
            BXTuiFei = atof(bxtuifei)
        time.sleep(5)
############挂账管理当日挂账###########################################################################################################################################
        browser.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/ul/li[5]').click()  # 点击挂账管理
        time.sleep(2)
        guazhang = browser.find_element_by_xpath('//*[@id="gztable"]/tfoot/tr/th[8]').text  # 挂账
        if guazhang == "  ":
            GuaZhang = int(0)
        else:
            GuaZhang = atof(guazhang)

###############退费管理-当天###################################################################################################
        browser.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/ul/li[8]/a').click()#点击退费管理
        time.sleep(2)

        dttfje = browser.find_element_by_xpath('//*[@id="table"]/tfoot/tr/th[8]').text  #
        if dttfje == " ":
            dtTfje = int(0)
        else:
            dtTfje = atof(dttfje)
        print dtTfje
        print int(TuiFei-dtTfje)
        if int(TuiFei-dtTfje)==0:
            print u"退费管理中当天退费金额测试通过"
        else:
            print u"退费管理中当天退费金额测试不通过"

##############今日日报########################################################################################################################################
        browser.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/ul/li[7]').click()  #点击今日日报
        time.sleep(5)
        drss = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/div[1]/table/tbody/tr[6]/td[3]/span').text  #当日实收
        Drss = atof(drss)
        drbx = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/div[1]/table/tbody/tr[7]/td[2]/span').text # 保险
        Drbx = atof(drbx)
        drgz = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/div[1]/table/tbody/tr[8]/td[2]').text # 当日挂账
        Drgz = atof(drgz)
        dryh = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/div[1]/table/tbody/tr[9]/td[2]/span').text  # 当日优惠
        Dryh = atof(dryh)
        drtf = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/div[1]/table/tbody/tr[10]/td[2]/span').text  # 当日退费
        Drtf = atof(drtf)
        drhj = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/div[1]/table/tbody/tr[11]/td[2]/span').text  # 当日合计
        Drhj = atof(drhj)
        time.sleep(5)
        a = Drss+Drbx+Drgz-Drtf
        print int(ShiShou-Drss),int(BaoXian-Drbx),int(YouHui-Dryh),int(TuiFei+BXTuiFei-Drtf),int(a-Drhj),int(GuaZhang-Drgz)
        if int(ShiShou-Drss)==0 and int(BaoXian-Drbx)==0 and int(YouHui-Dryh)==0 and int(TuiFei+BXTuiFei-Drtf)==0 and int(a-Drhj)==0 and int(GuaZhang-Drgz)==0:
            print u"今日日报当天合计测试通过"
        else:
            print u"今日日报当天合计测试不通过"
        time.sleep(5)
###################结算管理-本月统计########################################################################################################################################
        browser.find_element_by_xpath('/html/body/div[3]/aside/section/ul/li[9]/a').click()  # 点击收费、发药
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/ul/li[4]/a').click()  # 点击结算管理
        time.sleep(2)
        # 去掉元素的readonly属性
        js = 'document.getElementById("char5_date1").removeAttribute("readonly");'
        browser.execute_script(js)

        # 用js方法输入日期
        # 前面已经定义好此变量fir = today.strftime('%Y-%m-1')，这里也可以输入定量如："2016-12-25"
        js_value = 'document.getElementById("char5_date1").value="fir"'
        browser.execute_script(js_value)

        # # 清空文本后输入值
        browser.find_element_by_xpath('//*[@id="char5_date1"]').clear()
        browser.find_element_by_xpath('//*[@id="char5_date1"]').send_keys(fir)#此处是变量还是常量应该与前面保持一致
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/ul[2]/li[4]/button').click()#点击搜索
        time.sleep(2)
        #结算管理-本月保险
        setlocale(LC_NUMERIC, 'English_US')
        baoxian1 = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/div[3]/table/tfoot/tr/td[8]').text  # 保险
        if baoxian1 == " ":
            BaoXian1 = int(0)
        else:
            BaoXian1 = atof(baoxian1)#把带有千位分隔符的浮点数字符串形式转化为数字
        print BaoXian1
        #结算管理-本月优惠
        youhui1 = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/div[3]/table/tfoot/tr/td[9]').text  #
        if youhui1 == " ":
            YouHui1 = int(0)
        else:
            YouHui1 = atof(youhui1)
        print YouHui1
        #结算管理-本月实收
        shishou1 = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/div[3]/table/tfoot/tr/td[10]').text  #
        if shishou1 == " ":
            ShiShou1 = int(0)
        else:
            ShiShou1 = atof(shishou1)
        print ShiShou1
        # 结算管理-本月实收退费
        tuifei1 = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/div[3]/table/tfoot/tr/td[11]').text  #
        if tuifei1 == " ":
            TuiFei1 = int(0)
        else:
            TuiFei1 = atof(tuifei1)
        print TuiFei1
        # 结算管理-本月保险退费
        bxtuifei1= browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/div[3]/table/tfoot/tr/td[12]').text  #
        if bxtuifei1 == " ":
            BXTuiFei1 = int(0)
        else:
            BXTuiFei1 = atof(bxtuifei1)
        print BXTuiFei1
        time.sleep(5)
############挂账管理-本月#################################################################################################################################3
        browser.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/ul/li[5]').click()  # 点击挂账管理
        time.sleep(2)


        # 去掉元素的readonly属性
        js = 'document.getElementById("char5_date1").removeAttribute("readonly");'
        browser.execute_script(js)

        # 用js方法输入日期
        # 前面已经定义好此变量fir = today.strftime('%Y-%m-1')，这里也可以输入定量如："2016-12-25"
        js_value = 'document.getElementById("char5_date1").value="fir"'
        browser.execute_script(js_value)

        # # 清空文本后输入值
        browser.find_element_by_xpath('//*[@id="char5_date1"]').clear()
        browser.find_element_by_xpath('//*[@id="char5_date1"]').send_keys(fir)#此处是变量还是常量应该与前面保持一致
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/div/ul/li[5]/button').click()#点击搜索
        time.sleep(5)

        guazhang1 = browser.find_element_by_xpath('//*[@id="gztable"]/tfoot/tr/th[8]').text  # 挂账
        if guazhang1 == "  ":
            GuaZhang1 = int(0)
        else:
            GuaZhang1 = atof(guazhang1)
        print GuaZhang1
########今日日报-本月#####################################################################################################################################################
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/ul/li[7]').click()  #点击今日日报
        time.sleep(2)
        byss = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/div[1]/table/tbody/tr[6]/td[5]/span').text  #本月实收
        Byss = atof(byss)
        print Byss
        bybx = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/div[1]/table/tbody/tr[7]/td[4]/span').text  #本月保险
        Bybx = atof(bybx)
        print Bybx
        bygz = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/div[1]/table/tbody/tr[8]/td[4]/span').text  #
        Bygz = atof(bygz)
        print Bygz
        byyh = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/div[1]/table/tbody/tr[9]/td[4]/span').text  #本月优惠
        Byyh = atof(byyh)
        print Byyh
        bytf = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/div[1]/table/tbody/tr[10]/td[4]/span').text  #本月退费
        Bytf = atof(bytf)
        print Bytf
        byhj = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/div[1]/table/tbody/tr[11]/td[4]').text  #本月合计
        Byhj = atof(byhj)
        print Byhj
        time.sleep(5)
###############退费管理-本月###################################################################################################
        browser.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/ul/li[8]/a').click()#点击退费管理
        time.sleep(2)
        # 去掉元素的readonly属性
        js = 'document.getElementById("char5_date1").removeAttribute("readonly");'
        browser.execute_script(js)
        # 用js方法输入日期
        # 前面已经定义好此变量fir = today.strftime('%Y-%m-1')，这里也可以输入定量如："2016-12-25"
        js_value = 'document.getElementById("char5_date1").value="fir"'
        browser.execute_script(js_value)
        # # 清空文本后输入值
        browser.find_element_by_xpath('//*[@id="char5_date1"]').clear()
        browser.find_element_by_xpath('//*[@id="char5_date1"]').send_keys(fir)#此处是变量还是常量应该与前面保持一致
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/ul[2]/li[3]/button').click()#点击搜索
        time.sleep(2)

        tfje = browser.find_element_by_xpath('//*[@id="table"]/tfoot/tr/th[8]').text  #
        if tfje == " ":
            Tfje = int(0)
        else:
            Tfje = atof(tfje)
        print Tfje
        if int(num-Tfje)==0:
            print u"退费管理中本月退费金额测试通过"
        else:
            print u"退费管理中本月退费金额测试不通过"


        print int(BaoXian1 - Bybx),int(YouHui1 - Byyh),int(ShiShou1 - Byss),int(Tfje + (float(Befor)-float(Insur)) - Bytf),int(Byss + Bybx + Bygz - Bytf - Byhj),int(GuaZhang1 - Bygz)
        if int(BaoXian1 - Bybx) == 0 and int(YouHui1 - Byyh) == 0 and int(ShiShou1 - Byss) == 0 and int(Tfje + (float(Befor)-float(Insur)) - Bytf) == 0 and int(Byss + Bybx + Bygz - Bytf - Byhj) == 0 and int(GuaZhang1 - Bygz) == 0:
            print u"今日日报本月合计测试通过"
        else:
            print u"今日日报本月合计测试不通过"
        time.sleep(2)


#报表统计
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/div[3]/aside/section/ul/li[11]/a/span[1]').click()#点击报表统计
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="date1"]').clear()#清除账单开始时间
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="date1"]').send_keys(fir)  # 输入账单开始时间
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="date1"]').click()
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="laydate_ok"]').click()
        time.sleep(5)
        rbbzf = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/div/div[2]/div[1]/table/tfoot/tr/td[2]').text  #
        if rbbzf == "-":
            rbbZf = int(0)
        else:
            rbbZf = atof(rbbzf)
        time.sleep(1)

        rbbxyf = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/div/div[2]/div[1]/table/tfoot/tr/td[3]').text  #
        if rbbxyf == "-":
            rbbXyf = int(0)
        else:
            rbbXyf = atof(rbbxyf)
        time.sleep(1)

        rbbzcyf = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/div/div[2]/div[1]/table/tfoot/tr/td[4]').text  #
        if rbbzcyf == "-":
            rbbZcyf = int(0)
        else:
            rbbZcyf = atof(rbbzcyf)
        time.sleep(1)

        rbbzcy = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/div/div[2]/div[1]/table/tfoot/tr/td[5]').text  #
        if rbbzcy == "-":
            rbbZcy = int(0)
        else:
            rbbZcy = atof(rbbzcy)
        time.sleep(1)

        rbbjc = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/div/div[2]/div[1]/table/tfoot/tr/td[6]').text  #
        if rbbjc == "-":
            rbbJc = int(0)
        else:
            rbbJc = atof(rbbjc)
        time.sleep(1)

        rbbjy = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/div/div[2]/div[1]/table/tfoot/tr/td[7]').text  #
        if rbbjy == "-":
            rbbJy = int(0)
        else:
            rbbJy = atof(rbbjy)
        time.sleep(1)

        rbbll = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/div/div[2]/div[1]/table/tfoot/tr/td[8]').text  #
        if rbbll == "-":
            rbbLl = int(0)
        else:
            rbbLl = atof(rbbll)
        time.sleep(1)

        rbbzl = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/div/div[2]/div[1]/table/tfoot/tr/td[9]').text  #
        if rbbzl == "-":
            rbbZl = int(0)
        else:
            rbbZl = atof(rbbzl)
        time.sleep(1)

        rbbqt = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/div/div[2]/div[1]/table/tfoot/tr/td[10]').text  #
        if rbbqt == "-":
            rbbQt = int(0)
        else:
            rbbQt = atof(rbbqt)
        time.sleep(1)

        rbbhc = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/div/div[2]/div[1]/table/tfoot/tr/td[11]').text  #
        if rbbhc == "-":
            rbbHc = int(0)
        else:
            rbbHc = atof(rbbhc)
        time.sleep(1)




        rbbsydj = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/div/div[2]/div[1]/table/tfoot/tr/td[12]').text  #
        if rbbsydj  == "-":
            rbbSydj = int(0)
        else:
            rbbSydj = atof(rbbsydj)
        time.sleep(1)

        rbbyh = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/div/div[2]/div[1]/table/tfoot/tr/td[13]').text  #
        if rbbyh == "-":
            rbbYh = int(0)
        else:
            rbbYh = atof(rbbyh)
            print rbbYh
        time.sleep(1)

        rbbhj = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/div/div[2]/div[1]/table/tfoot/tr/td[14]').text  #
        if rbbhj == "-":
            rbbHj = int(0)
        else:
            rbbHj = atof(rbbhj)
        time.sleep(2)


        browser.find_element_by_xpath('//*[@id="content"]/div[2]/div/ul/li[4]/a/span').click()  # 点击收费报表
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="date1"]').clear()  # 清除账单开始时间
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="date1"]').send_keys(fir)  # 输入账单开始时间
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="inquiry"]').click()  #点击查询
        time.sleep(2)
        target = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/section/div/div[3]/div[5]/table/tbody/tr[10]/td[1]')  #滑动到优惠金额处
        browser.execute_script("arguments[0].scrollIntoView();", target)  #
        time.sleep(2)

        sfbbzf = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/section/div/div[3]/div[5]/table/tbody/tr[1]/td[5]').text  #
        if sfbbzf == "-":
            sfbbZf = int(0)
        else:
            sfbbZf = atof(sfbbzf)
        time.sleep(1)

        sfbbzycf = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/section/div/div[3]/div[5]/table/tbody/tr[2]/td[5]').text  #
        if sfbbzycf == "-":
            sfbbZycf = int(0)
        else:
            sfbbZycf = atof(sfbbzycf)
        time.sleep(1)

        sfbbyp = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/section/div/div[3]/div[5]/table/tbody/tr[3]/td[5]').text  #
        if sfbbyp == "-":
            sfbbYp = int(0)
        else:
            sfbbYp = atof(sfbbyp)
        time.sleep(1)


        sfbbjc = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/section/div/div[3]/div[5]/table/tbody/tr[4]/td[5]').text  #
        if sfbbjc == "-":
            sfbbJc = int(0)
        else:
            sfbbJc = atof(sfbbjc)
        time.sleep(1)

        sfbbjy = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/section/div/div[3]/div[5]/table/tbody/tr[5]/td[5]').text  #
        if sfbbjy == "-":
            sfbbJy = int(0)
        else:
            sfbbJy = atof(sfbbjy)
        time.sleep(1)


        sfbbzl = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/section/div/div[3]/div[5]/table/tbody/tr[6]/td[5]').text  #
        if sfbbzl == "-":
            sfbbZl = int(0)
        else:
            sfbbZl = atof(sfbbzl)
        time.sleep(1)

        sfbbqt = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/section/div/div[3]/div[5]/table/tbody/tr[7]/td[5]').text  #
        if sfbbqt == "-":
            sfbbQt = int(0)
        else:
            sfbbQt = atof(sfbbqt)
        time.sleep(1)

        sfbbhc = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/section/div/div[3]/div[5]/table/tbody/tr[8]/td[5]').text  #
        if sfbbhc == "-":
            sfbbHc = int(0)
        else:
            sfbbHc = atof(sfbbhc)
        time.sleep(1)

        sfbbsydj = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/section/div/div[3]/div[5]/table/tbody/tr[9]/td[5]').text  #
        if sfbbsydj == "-":
            sfbbSydj = int(0)
        else:
            sfbbSydj = atof(sfbbsydj)
        time.sleep(1)

        sfbbyh = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/section/div/div[3]/div[5]/table/tbody/tr[10]/td[5]').text  #
        if sfbbyh == "-":
            sfbbYh = int(0)
        else:
            sfbbYh = atof(sfbbyh)
            print sfbbYh
        time.sleep(1)

        print int(rbbZf-sfbbZf), int(rbbXyf+rbbZcyf-sfbbYp), int(rbbZcy-sfbbZycf), int(rbbJc-sfbbJc), int(rbbJy-sfbbJy), int(rbbLl+rbbZl-sfbbZl),\
            int(rbbQt-sfbbQt),int(rbbHc-sfbbHc),int(rbbSydj-sfbbSydj),int(rbbYh-sfbbYh),\
            int(rbbHj-sfbbZf-sfbbZycf-sfbbYp-sfbbJc-sfbbJy-sfbbZl-sfbbQt-sfbbHc-sfbbSydj-sfbbYh)
        if int(rbbZf-sfbbZf) == 0 and int(rbbXyf+rbbZcyf-sfbbYp) == 0 and int(rbbZcy-sfbbZycf) == 0 and int(rbbJc-sfbbJc) == 0 and int(rbbJy-sfbbJy) == 0 and int(rbbLl+rbbZl-sfbbZl) == 0 and \
            int(rbbQt-sfbbQt) == 0 and int(rbbHc-sfbbHc) == 0 and int(rbbSydj-sfbbSydj) == 0 and int(rbbYh-sfbbYh) == 0 and \
            int(rbbHj-sfbbZf-sfbbZycf-sfbbYp-sfbbJc-sfbbJy-sfbbZl-sfbbQt-sfbbHc-sfbbSydj-sfbbYh) == 0:
            print u"诊所日报表科室收费当月统计与收费报表收费项目当月统计测试通过"
        else:
            print u"诊所日报表科室收费当月统计与收费报表收费项目当月统计测试不通过"
        time.sleep(5)

#### 收费报表，收费报表结算方式与计算管理中的收费方式#####################################################################################################################################################################################
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="content"]/div[2]/div/ul/li[4]/a/span').click()  # 点击收费报表
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="date1"]').clear()  # 清除账单开始时间
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="date1"]').send_keys(fir)  # 输入账单开始时间
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="inquiry"]').click()  # 点击查询
        time.sleep(1)
        #收费报表—收费情况—本期未结金额
        sfbbwj = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/section/div/div[3]/div[1]/table/tbody/tr[1]/td[5]').text  #
        if sfbbwj == "-":
            sfbbWj = int(0)
        else:
            sfbbWj = atof(sfbbwj)
        print sfbbWj

        # 收费报表—收费情况—本期退费
        sfbbtf = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/section/div/div[3]/div[1]/table/tbody/tr[2]/td[5]').text  #
        if sfbbtf == "-":
            sfbbTf = int(0)
        else:
            sfbbTf = atof(sfbbtf)
        print sfbbTf

        # 收费报表—收费情况—本期收费
        sfbbsf = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/section/div/div[3]/div[1]/table/tbody/tr[3]/td[5]').text  #
        if sfbbsf == "-":
            sfbbSf = int(0)
        else:
            sfbbSf = atof(sfbbsf)
        print sfbbSf


        # 滑动到优惠金额处
        time.sleep(2)
        target = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/section/div/div[3]/div[5]/table/tbody/tr[10]/td[1]')
        browser.execute_script("arguments[0].scrollIntoView();", target)  #
        time.sleep(2)
        # 收费报表-结算方式-刷卡
        sfbbsk = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/section/div/div[3]/div[4]/table/tbody/tr[1]/td[5]').text  #
        if sfbbsk == "-":
            sfbbSk = int(0)
        else:
            sfbbSk = atof(sfbbsk)
        print sfbbSk
        time.sleep(1)
        # 收费报表-结算方式-支付宝
        sfbbzfb = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/section/div/div[3]/div[4]/table/tbody/tr[2]/td[5]').text  #
        if sfbbzfb == "-":
            sfbbZfb = int(0)
        else:
            sfbbZfb = atof(sfbbzfb)
        print sfbbZfb
        time.sleep(1)
        # 收费报表-结算方式-储值卡
        sfbbczk = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/section/div/div[3]/div[4]/table/tbody/tr[3]/td[5]').text  #
        if sfbbczk == "-":
            sfbbCzk = int(0)
        else:
            sfbbCzk = atof(sfbbczk)
        print sfbbCzk
        time.sleep(1)

        # 收费报表-结算方式-保险
        sfbbbx = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/section/div/div[3]/div[4]/table/tbody/tr[4]/td[5]').text  #
        if sfbbbx == "-":
            sfbbBx = int(0)
        else:
            sfbbBx = atof(sfbbbx)
        print sfbbbx
        time.sleep(1)

        # 收费报表-结算方式-其他
        sfbbqtzf = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/section/div/div[3]/div[4]/table/tbody/tr[5]/td[5]').text  #
        if sfbbqtzf == "-":
            sfbbQtzf = int(0)
        else:
            sfbbQtzf = atof(sfbbqtzf)
        print sfbbQtzf
        time.sleep(1)
        # 收费报表-结算方式-微信
        sfbbwx = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/section/div/div[3]/div[4]/table/tbody/tr[6]/td[5]').text  #
        if sfbbwx == "-":
            sfbbWx = int(0)
        else:
            sfbbWx = atof(sfbbwx)
        print sfbbWx
        time.sleep(1)
        # 收费报表-结算方式-公司汇款
        sfbbgshk = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/section/div/div[3]/div[4]/table/tbody/tr[6]/td[5]').text  #
        if sfbbgshk == "-":
            sfbbGshk = int(0)
        else:
            sfbbGshk = atof(sfbbgshk)
        print sfbbGshk
        time.sleep(1)
        # 收费报表-结算方式-个人汇款
        sfbbgrhk = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/section/div/div[3]/div[4]/table/tbody/tr[8]/td[5]').text  #
        if sfbbgrhk == "-":
            sfbbGrhk = int(0)
        else:
            sfbbGrhk = atof(sfbbgrhk)
        print sfbbGrhk
        time.sleep(1)

        # 收费报表-结算方式-现金
        sfbbxj = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/section/div/div[3]/div[4]/table/tbody/tr[9]/td[5]').text  #
        if sfbbxj == "-":
            sfbbXj = int(0)
        else:
            sfbbXj = atof(sfbbxj)
        print sfbbXj
        time.sleep(1)

#############收费、发药，结算管理-当月##########################################################################################################################################################################################################
        browser.find_element_by_xpath('/html/body/div[3]/aside/section/ul/li[9]/a').click()  # 点击收费、发药
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/ul/li[4]/a').click()  # 点击结算管理
        time.sleep(2)
        # 去掉元素的readonly属性
        js = 'document.getElementById("char5_date1").removeAttribute("readonly");'
        browser.execute_script(js)

        # 用js方法输入日期
        # 前面已经定义好此变量fir = today.strftime('%Y-%m-1')，这里也可以输入定量如："2016-12-25"
        js_value = 'document.getElementById("char5_date1").value="fir"'
        browser.execute_script(js_value)

        # # 清空文本后输入值
        browser.find_element_by_xpath('//*[@id="char5_date1"]').clear()
        browser.find_element_by_xpath('//*[@id="char5_date1"]').send_keys(fir)#此处是变量还是常量应该与前面保持一致
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/ul[2]/li[4]/button').click()#点击搜索
        time.sleep(2)
        #结算管理-现金支付
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/ul[1]/li[3]/select').click()  # 点击支付方式
        time.sleep(1)
        InputType = Select(browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/ul[1]/li[3]/select'))
        InputType.select_by_value("1")#现金支付
        time.sleep(2)
        xjzf = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/div[3]/table/tfoot/tr/td[10]').text  #
        if xjzf == " ":
            Xjzf = int(0)
        else:
            Xjzf = atof(xjzf)
        print Xjzf
        time.sleep(2)
        # 结算管理-刷卡支付
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/ul[1]/li[3]/select').click()  # 点击支付方式
        InputType = Select(browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/ul[1]/li[3]/select'))
        InputType.select_by_value("2")  # 刷卡支付
        time.sleep(4)
        skzf = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/div[3]/table/tfoot/tr/td[10]').text  #
        if skzf == " ":
            Skzf = int(0)
        else:
            Skzf = atof(skzf)
        print Skzf
        time.sleep(2)
        # 结算管理-微信支付
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/ul[1]/li[3]/select').click()  # 点击支付方式
        InputType = Select(browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/ul[1]/li[3]/select'))
        InputType.select_by_value("3")  # 微信支付
        time.sleep(2)
        wxzf = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/div[3]/table/tfoot/tr/td[10]').text  #
        if wxzf == " ":
            Wxzf = int(0)
        else:
            Wxzf = atof(wxzf)
        print Wxzf
        time.sleep(2)
        # 结算管理-支付宝支付
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/ul[1]/li[3]/select').click()  # 点击支付方式
        InputType = Select(browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/ul[1]/li[3]/select'))
        InputType.select_by_value("4")  # 支付宝支付
        time.sleep(2)
        zfbzf = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/div[3]/table/tfoot/tr/td[10]').text  #
        if zfbzf == " ":
            Zfbzf = int(0)
        else:
            Zfbzf = atof(zfbzf)
        print Zfbzf
        time.sleep(2)
        # 结算管理-个人汇款
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/ul[1]/li[3]/select').click()  # 点击支付方式
        InputType = Select(browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/ul[1]/li[3]/select'))
        InputType.select_by_value("5")  # 个人汇款支付
        time.sleep(2)
        grhkzf = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/div[3]/table/tfoot/tr/td[10]').text  #
        if grhkzf == " ":
            Grhkzf = int(0)
        else:
            Grhkzf = atof(grhkzf)
        print Grhkzf
        time.sleep(2)
        # 结算管理-公司汇款
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/ul[1]/li[3]/select').click()  # 点击支付方式
        InputType = Select(browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/ul[1]/li[3]/select'))
        InputType.select_by_value("6")  # 公司汇款支付
        time.sleep(2)
        gshkzf = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/div[3]/table/tfoot/tr/td[10]').text  #
        if gshkzf == " ":
            Gshkzf = int(0)
        else:
            Gshkzf = atof(gshkzf)
        print Gshkzf
        time.sleep(2)
        # 结算管理-储值卡支付
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/ul[1]/li[3]/select').click()  # 点击支付方式
        InputType = Select(browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/ul[1]/li[3]/select'))
        InputType.select_by_value("7")  # 储值卡支付
        time.sleep(2)
        czkzf = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/div[3]/table/tfoot/tr/td[10]').text  #
        if czkzf == " ":
            Czkzf = int(0)
        else:
            Czkzf = atof(czkzf)
        print Czkzf
        time.sleep(2)
        # 结算管理-其他支付
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/ul[1]/li[3]/select').click()  # 点击支付方式
        InputType = Select(browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/ul[1]/li[3]/select'))
        InputType.select_by_value("8")  # 其他支付
        time.sleep(2)
        qtzf = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/div[3]/table/tfoot/tr/td[10]').text  #
        if qtzf == " ":
            Qtzf = int(0)
        else:
            Qtzf = atof(qtzf)
        print Qtzf
        time.sleep(2)
        # 结算管理-保险支付
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/ul[2]/li[3]/select').click()  # 点击患者类型
        InputType = Select(browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/ul[2]/li[3]/select'))
        InputType.select_by_value("1")  # 保险
        time.sleep(2)
        bxzf = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/div[3]/table/tfoot/tr/td[8]').text  #
        if bxzf == " ":
            Bxzf = int(0)
        else:
            Bxzf = atof(bxzf)
        print Bxzf
        time.sleep(2)
        print int(sfbbSk-Skzf), int(sfbbZfb-Zfbzf), int(sfbbCzk-Czkzf), int(), int(sfbbQtzf-Qtzf), int(sfbbWx-Wxzf), \
            int(sfbbGshk-Gshkzf), int(sfbbGshk-Grhkzf),int(sfbbXj-Xjzf)
        if int(sfbbSk-Skzf)==0 and int(sfbbZfb-Zfbzf)==0 and int(sfbbCzk-Czkzf)==0 and int()==0 and int(sfbbQtzf-Qtzf)==0 and int(sfbbWx-Wxzf)==0 and \
            int(sfbbGshk-Gshkzf)==0 and int(sfbbGshk-Grhkzf)==0 and int(sfbbXj-Xjzf)==0:
            print u"结算管理中当月的支付方式统计与收费报表当月结算方式统计测试通过"
        else:
            print u"结算管理中当月的支付方式统计与收费报表当月结算方式统计测试不通过"
        time.sleep(2)
        if int(BaoXian1+ShiShou1-sfbbSf)==0 and int(Tfje-sfbbTf)==0 and int(GuaZhang1-sfbbWj)==0:
            print u"收费报表中本期的未结金额、退费、收费测试通过"
        else:
            print u"收费报表中本期的未结金额、退费、收费测试不通过"


if __name__ == '__main__':
    unittest.main()