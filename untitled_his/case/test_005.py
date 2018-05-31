# coding:utf-8
'''#1、预约，签到，接诊，挂账。2、快速接诊、药品（耗材）入库及入库的红冲。3、药品（耗材）出库及出库的红冲。'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from commonshare.His import Browser
import unittest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import datetime
from commonshare.his_common import His
from commonshare.his_common import browser
p = His()

today = datetime.datetime.now()
days = datetime.timedelta(days=1)
n_days = today + days
tom = n_days.strftime('%Y-%m-%d')
now = today.strftime('%Y-%m-%d')
print (today.strftime('%Y-%m-%d'))
print (n_days.strftime('%Y-%m-%d'))

class TestHis(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        p.setUp()

    @classmethod
    def tearDownClass(cls):
        p.tearDown()

    # 登录
    def test001(self):
        p.login()

    #签到接诊
    def test002(self):
        browser.find_element_by_xpath('/html/body/div[3]/aside/section/ul/li[2]/ul/li[1]/a').click()  # 点击预约挂号
        time.sleep(5)
        browser.find_element_by_xpath('//*[@id="registerName_input"]').send_keys(u"董焕焕")  # 输入姓名
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="appointment_nav"]/ul').click()  # 点击空白处
        browser.find_element_by_xpath('//*[@id="telephonNum"]').send_keys("18611059298")  # 输入手机号
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="regis_data"]').clear()  # 选择就诊日期
        browser.find_element_by_xpath('//*[@id="regis_data"]').send_keys(tom)
        browser.find_element_by_xpath('//*[@id="addRegister_save"]').click()  # 点击保存
        time.sleep(5)
        print ("预约挂号成功")


        browser.find_element_by_xpath('//*[@id="appointment_nav"]/ul/li[2]/a').click()  # 点击患者列表
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="appointRegis_nextDate_button"]').click()  # 点击下一天
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="querybtn"]').click()  # 点击查询
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="appointRegister_patientCart_content"]/tr[1]/td[11]/a').click()  # 点击改约
        time.sleep(3)
        browser.find_element_by_xpath('//*[@id="regis_data"]').clear()  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="regis_data"]').send_keys(now)  # 预约日期处输入今天的时间
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="presprint_1"]').click()  # 点击保存并打印
        time.sleep(2)
        browser.back()
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="appointment_nav"]/ul/li[2]/a').click()  # 点击患者列表
        time.sleep(2)

        browser.find_element_by_xpath('//*[@id="select2-plistSearchByDocter-container"]').click()  # 点击全部
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u"董焕焕")  # 输入董焕焕
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)   # 选择董焕焕医生
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="querybtn"]').click()  # 点击查询
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="select2-plistSearchByDocter-container"]').click()  # 点击医生筛选
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u'全部')  # 点击
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)#选择全部
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="searchPatint"]').send_keys(u"董焕焕")  # 搜索框中输入董焕焕
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="querybtn"]').click()  # 点击查询
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="searchPatint"]').clear()  # 搜索框中输入董焕焕
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="querybtn"]').click()  # 点击查询
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="appointRegis_cart_tab"]/li[1]').click()  # 点击已预约
        time.sleep(2)
        browser.find_element_by_xpath( '//*[@id="appointRegister_patientCart_content"]/tr/td[11]/p[1]').click()  # 点击签到
        time.sleep(5)
        browser.find_element_by_xpath('/html/body/div[3]/aside/section/ul/li[2]/ul/li[2]/a').click()  # 点击医生工作台
        time.sleep(5)
        browser.find_element_by_xpath('//*[@id="doctor_patient_cart_content"]/div[1]/div[2]/span[1]').click()  # 点击接诊
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="seeDoctoring_nav"]/ul/li[2]/a').click()#点击检验项目
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="select2-inspectSearchInput-container"]').click()  # 点击检验项目处的请选择
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u"过敏原检测(食物组)")  #输入过敏原检测(食物组)
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)#选择过敏原检测(食物组)
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="select2-inspectSearchInput-container"]').click()  # 点击检验项目处的请选择
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u"ABO血型")  #输入ABO血型
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)#选择ABO血型
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="inspect_save"]').click()  # 点击保存
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="inspect_presprint"]').click()#点击打印
        time.sleep(2)
        browser.back()#点击返回
        time.sleep(2)
        print ("填写检验项目成功")

    # 接诊界面填写检查项目
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="seeDoctoring_nav"]/ul/li[3]/a').click()  # 点击检查项目
        time.sleep(3)
        browser.find_element_by_xpath('//*[@id="checkoutBox"]/div[1]/div/span[2]/span[1]/span').click()  # 点击检查项目处的请选择
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u"多普勒听胎心")#输入多普勒听胎心
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)#选择多普勒听胎心
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="select2-checkoutSearchLis-container"]').click()  # 点击检查项目处的请选择
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u"泌尿系超声")#输入泌尿系超声
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)#选择泌尿系超声
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="saveCheckoutItems"]').click()  # 点击保存
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="checkoutPresprint"]').click()#点击打印
        time.sleep(2)
        browser.back()#浏览器返回
        time.sleep(2)
        print ("填写检查项目成功")

        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div[1]/div[2]/p[2]/a').click()  # 点击结束就诊
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="offMadicalMess"]/div/a/button').click()  # 点击是
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/div[3]/aside/section/ul/li[2]/ul/li[7]/a').click()# 点击收费/发药
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/ul/li[2]/a').click()#点击收费
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[2]/ul/li/div/div[2]').click()#点击待收费
        time.sleep(2)
        target = browser.find_element_by_xpath('//*[@id="buying_credit"]')  # 滑动到代收付页面最底部
        browser.execute_script("arguments[0].scrollIntoView();", target)  # 滑动到代收付页面最底部
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="buying_credit"]').click()  # 点击挂账
        time.sleep(3)
        browser.back()


    #快速接诊
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/div[3]/aside/section/ul/li[2]/ul/li[2]/a').click()#点击医生工作台
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="fasterLookDoctorBtn"]').click()  #点击快速接诊
        time.sleep(3)
        browser.current_window_handle  # 此行代码用来定位当前页面
        time.sleep(3)
        browser.find_element_by_id("registerName_input").send_keys(u"快速接诊")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="fasterRigis_form"]/div[6]/div[1]/span').click()#点击空白
        browser.find_element_by_id("telephonNum").click()
        browser.find_element_by_id("telephonNum").clear()
        browser.find_element_by_id("telephonNum").send_keys("18611059298")
        time.sleep(1)
        browser.find_element_by_id("sexWoman").click()
        time.sleep(1)
        browser.find_element_by_id("registAgeInput").clear()
        browser.find_element_by_id("registAgeInput").send_keys("20")
        time.sleep(1)
        browser.find_element_by_id("fasterDo").click()
        time.sleep(2)


    #药品（耗材）入库、出库
    def test003(self):
        # 入库
        browser.find_element_by_xpath('/html/body/div[3]/aside/section/ul/li[5]/a/span[1]').click()  # 点击诊所管理
        time.sleep(3)
        browser.find_element_by_xpath('/html/body/div[3]/aside/section/ul/li[5]/ul/li[1]/a').click()  # 点击药房
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="layui-layer11"]/span/a').click()  # 点击关闭
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="content"]/div[3]/div/div/ul/li[1]/a/span').click()  # 点击入库单管理
        time.sleep(1)
        browser.find_element_by_xpath(
            '//*[@id="ajax-content"]/div/div[1]/div[1]/div[2]/a/button').click()  # 点击新增入库单
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="choosekey"]').send_keys(u"阿奇霉素注射")  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="choose"]/tbody/tr/td[3]').click()
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr/td[6]/input').send_keys(u"1111")  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr/td[7]/input').send_keys(now)  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[1]/td[8]/input').send_keys(u"2023-10-11")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr/td[9]/input').send_keys(10)
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr/td[11]/input[2]').clear()
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr/td[11]/input[2]').send_keys(10)
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="choosekey"]').send_keys(u"硫酸庆大霉素注射液")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="choose"]/tbody/tr/td[2]').click()
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[2]/td[6]/input').send_keys(u"1111")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[2]/td[7]/input').send_keys(now)
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[2]/td[8]/input').send_keys(u"2023-10-11")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[2]/td[9]/input').send_keys(10)
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[2]/td[11]/input[2]').clear()
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[2]/td[11]/input[2]').send_keys(10)
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="choosekey"]').send_keys(u"达克宁")
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="choose"]/tbody/tr[1]/td[2]').click()
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[3]/td[11]/span').click()
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[3]/td[12]/span').click()#点击删除
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/form/div/ul/li/ul/li/div[3]/span/span[1]/span/span[2]/b').click()
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u"同仁堂")
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit_save"]').click()  # 点击提交审核
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="StockBills_menu0"]/span[1]').click()  # 点击详情
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[2]/div[5]/span[4]').click()  # 点击取消
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="StockBills_menu0"]/span[2]').click()  # 点击修改
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="choosekey"]').send_keys(u"三伏贴")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="choose"]/tbody/tr[2]').click()
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[3]/td[6]/input').send_keys(u"1111")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[3]/td[7]/input').send_keys(now)
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[3]/td[8]/input').send_keys(u"2023-10-11")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[3]/td[9]/input').send_keys(10)
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[3]/td[11]/input[4]').clear()
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[3]/td[11]/input[4]').send_keys(10)
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="choosekey"]').send_keys(u"达克宁")
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="choose"]/tbody/tr[1]/td[3]').click()
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[4]/td[6]/input').send_keys(now)
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[4]/td[7]/input').send_keys(now)
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[4]/td[8]/input').send_keys(u"2023-10-11")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[4]/td[9]/input').send_keys(10)
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[4]/td[11]/input[4]').clear()
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[4]/td[11]/input[4]').send_keys(10)
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit_save"]').click()
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="StockBills_menu0"]/span[4]').click()  # 点击审核
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit_check"]').click()  # 在审核详情页点击审核



        #药品入库红冲
        # time.sleep(2)
        # browser.find_element_by_xpath('//*[@id="StockBills_menu0"]/span').click()  # 点击详情
        # time.sleep(2)
        # browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[2]/div[5]/span[5]').click()  # 点击红冲
        # time.sleep(2)
        # browser.current_window_handle  # 此行代码用来定位当前页面
        # time.sleep(2)
        # browser.find_element_by_xpath('//*[@id="gainBtn"]').click()  # 点击获取验证码
        # time.sleep(30)
        # ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layui-layer48"]/div[2]/div/p/span')))  #
        # ys.click()  #点击确定




        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="content"]/div[3]/div/div/ul/li[4]/a').click()  # 点击库存管理
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="search"]').send_keys(u"达克宁")  # 输入达克宁
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="home_search"]/span[2]').click()  # 点击查询
        time.sleep(5)
        browser.find_element_by_xpath('/html/body/div[3]/aside/section/ul/li[5]/ul/li[1]/a').click()  # 点击药房
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="content"]/div[3]/div/div/ul/li[1]/a/span').click()  # 点击入库单管理
        time.sleep(1)
        browser.find_element_by_xpath(
            '//*[@id="ajax-content"]/div/div[1]/div[1]/div[2]/a/button').click()  # 点击新增入库单
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="choosekey"]').send_keys(u"阿奇霉素注射")  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="choose"]/tbody/tr/td[3]').click()
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr/td[6]/input').send_keys(u"1111")  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr/td[7]/input').send_keys(now)  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[1]/td[8]/input').send_keys(u"2023-10-11")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr/td[9]/input').send_keys(10)
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr/td[11]/input[2]').clear()
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr/td[11]/input[2]').send_keys(10)
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="choosekey"]').send_keys(u"硫酸庆大霉素注射液")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="choose"]/tbody/tr/td[2]').click()
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[2]/td[6]/input').send_keys(u"1111")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[2]/td[7]/input').send_keys(now)
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[2]/td[8]/input').send_keys(u"2023-10-11")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[2]/td[9]/input').send_keys(10)
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[2]/td[11]/input[2]').clear()
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[2]/td[11]/input[2]').send_keys(10)
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="choosekey"]').send_keys(u"达克宁")
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="choose"]/tbody/tr[1]/td[2]').click()
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[3]/td[11]/span').click()
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[3]/td[12]/span').click()#点击删除
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/form/div/ul/li/ul/li/div[3]/span/span[1]/span/span[2]/b').click()
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u"同仁堂")
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit_save"]').click()  # 点击提交审核
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="StockBills_menu0"]/span[1]').click()  # 点击详情
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[2]/div[5]/span[4]').click()  # 点击取消
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="StockBills_menu0"]/span[2]').click()  # 点击修改
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="choosekey"]').send_keys(u"三伏贴")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="choose"]/tbody/tr[2]').click()
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[3]/td[6]/input').send_keys(u"1111")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[3]/td[7]/input').send_keys(now)
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[3]/td[8]/input').send_keys(u"2023-10-11")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[3]/td[9]/input').send_keys(10)
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[3]/td[11]/input[4]').clear()
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[3]/td[11]/input[4]').send_keys(10)
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="choosekey"]').send_keys(u"达克宁")
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="choose"]/tbody/tr[1]/td[3]').click()
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[4]/td[6]/input').send_keys(now)
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[4]/td[7]/input').send_keys(now)
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[4]/td[8]/input').send_keys(u"2023-10-11")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[4]/td[9]/input').send_keys(10)
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[4]/td[11]/input[4]').clear()
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[4]/td[11]/input[4]').send_keys(10)
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit_save"]').click()
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="StockBills_menu0"]/span[4]').click()  # 点击审核
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit_check"]').click()  # 在审核详情页点击审核






        # 出库
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="content"]/div[3]/div/div/ul/li[2]/a/span').click()
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[1]/div[2]/a/button').click()
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="choosekey"]').send_keys(u"达克宁")
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="choose"]/tbody/tr[1]').click()
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr/td[11]/input[4]').clear()
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr/td[11]/input[4]').send_keys(5)
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="choosekey"]').send_keys(u"三伏贴")
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="choose"]/tbody/tr[1]/td[3]').click()
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="choosekey"]').send_keys(u"701跌打镇痛膏")
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="choose"]/tbody/tr/td[3]').click()  # 选择701跌打镇痛膏
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[3]/td[12]/span').click()  # 删除701跌打镇痛膏
        time.sleep(5)
        browser.find_element_by_xpath(
            '//*[@id="ajax-content"]/div/div/form/div/ul/li/ul/li/div[3]/span/span[1]/span/span[2]').click()  # 点击领用科室
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u"心血管内科")  # 在科室处输入心血管内科
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)  # 选择心血管内科
        time.sleep(2)
        #点击领用人
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/form/div/ul/li/ul/li/div[5]/span/span[1]/span/span[2]/b').click()
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u"董焕焕")  # 在领用人处输入董焕焕
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)  # 选择董焕焕领用人
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="stockIn_edit_save"]/button').click()  # 提交审核
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="StockBills_menu0"]/span[1]').click()  # 点击详情
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[2]/div[3]/span[4]').click()  # 在详情页点击取消
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="StockBills_menu0"]/span[2]').click()  # 点击修改
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[1]/td[12]/input[5]').clear()  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[1]/td[12]/input[5]').send_keys(9)  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="choosekey"]').send_keys(u"阿奇霉素注射")  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="choose"]/tbody/tr[1]/td[3]').click()  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="stockIn_edit_save"]').click()  # 点击保存
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="StockBills_menu0"]/span[4]').click()  # 点击审核
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="stockIn_edit_check"]').click()  # 在审核页点击审核
        time.sleep(2)




        #药品出库红冲
        # browser.find_element_by_xpath('//*[@id="content"]/div[3]/div/div/ul/li[4]/a/span').click()  # 点击库存管理
        # time.sleep(2)
        # browser.find_element_by_xpath('//*[@id="search"]').send_keys(u"阿奇霉素注射液")  #
        # time.sleep(2)
        # browser.find_element_by_xpath('//*[@id="home_search"]/span[2]').click()  # 点击查询
        # time.sleep(2)
        # browser.find_element_by_xpath('//*[@id="content"]/div[3]/div/div/ul/li[2]/a/span').click()  # 点击出库单管理
        # time.sleep(2)
        # browser.find_element_by_xpath('//*[@id="StockBills_menu0"]/span').click()  # 点击详情
        # time.sleep(2)
        # browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[2]/div[3]/span[5]').click()  # 点击红冲
        # time.sleep(2)
        # browser.current_window_handle  # 此行代码用来定位当前页面
        # time.sleep(2)
        # browser.find_element_by_xpath('//*[@id="gainBtn"]').click()  # 点击获取验证码
        # time.sleep(20)
        # ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layui-layer125"]/div[2]/div/p/span')))  #
        # ys.click()  #点击确定
        # time.sleep(2)



        # 耗材入库、审核
        browser.find_element_by_xpath('//*[@id="content"]/div[3]/div/div/ul/li[1]/a').click()#点击入库单管理
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[1]/div[2]/a/button').click()#点击新增入库单
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/form/div/ul/li/ul/li/div[1]/select').click()  #点击类型
        time.sleep(1)
        InputType = Select(browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/form/div/ul/li/ul/li/div[1]/select'))
        InputType.select_by_value("2")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="choosekey"]').send_keys(u"一次性换药包")  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="choose"]/tbody/tr/td[2]').click()  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr/td[6]/input').send_keys("111")  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr/td[7]/input').send_keys(now)  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr/td[8]/input').send_keys(u"2023-10-11")  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr/td[9]/input').send_keys(10)  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr/td[11]/input[2]').clear()  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr/td[11]/input[2]').send_keys(10)  #
        time.sleep(2)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="choosekey"]')))  #
        ys.send_keys(u"一次性纱布块")  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="choose"]/tbody/tr/td[2]').click()  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[2]/td[6]/input').send_keys("111")  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[2]/td[7]/input').send_keys(now)  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[2]/td[8]/input').send_keys(u"2023-10-11")  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[2]/td[9]/input').send_keys(10)  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[2]/td[11]/input[2]').clear()  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[2]/td[11]/input[2]').send_keys(10)  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="choosekey"]').send_keys(u"一次性自粘敷贴")  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="choose"]/tbody/tr[1]/td[2]').click()  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[3]/td[12]/span').click()  #删除一次性自粘敷贴
        time.sleep(3)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/form/div/ul/li/ul/li/div[3]/span/span[1]/span/span[2]').click()  #
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u"同仁堂")  #
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit_save"]').click()  #点击提交审核
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="StockBills_menu0"]/span[1]').click()  #点击详情
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[2]/div[5]/span[4]').click()  #点击取消
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="StockBills_menu0"]/span[2]').click()  #点击修改
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="choosekey"]').send_keys(u"碘伏棉签")  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="choose"]/tbody/tr/td[2]').click()  #选择碘伏棉签
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[3]/td[6]/input').send_keys(222)#
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[3]/td[7]/input').send_keys(now)  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[3]/td[8]/input').send_keys(u"2023-10-11")  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[3]/td[9]/input').send_keys(10)  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[3]/td[11]/input[4]').clear()  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[3]/td[11]/input[4]').send_keys(10)  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="choosekey"]').send_keys(u"碘伏消毒液")  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="choose"]/tbody/tr[1]/td[4]').click()
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[4]/td[12]/span').click()  #删除碘伏消毒液
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="stockIn_edit_save"]').click()  #点击保存
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="StockBills_menu0"]/span[4]').click()  #点击审核
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="stockIn_edit_check"]').click()  #在详情页点击审核
        time.sleep(2)
        # 耗材出库、审核
        browser.find_element_by_xpath('//*[@id="content"]/div[3]/div/div/ul/li[2]/a/span').click()  #点击出库单管理
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[1]/div[2]/a/button').click()  #点击新增出库单
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/form/div/ul/li/ul/li/div[1]/select').click()  #点击类型
        time.sleep(1)
        OutputType = Select(browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/form/div/ul/li/ul/li/div[1]/select'))
        OutputType.select_by_value("2")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="choosekey"]').send_keys(u"一次性换药包")  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="choose"]/tbody/tr[1]').click()  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr/td[11]/input[4]').clear()  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr/td[11]/input[4]').send_keys(5)  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="choosekey"]').send_keys(u"一次性纱布块")  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="choose"]/tbody/tr[1]/td[4]').click()  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="choosekey"]').send_keys(u"碘伏棉签")  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="choose"]/tbody/tr[1]/td[3]').click()  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[3]/td[12]/span').click()  # 点击删除
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/form/div/ul/li/ul/li/div[3]/span/span[1]/span/span[2]').click()  #选择领用科室
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u"全科")  #
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/form/div/ul/li/ul/li/div[5]/span/span[1]/span/span[2]/b').click()  #点击领用人
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u"沈志卫")  #
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="stockIn_edit_save"]/button').click()#点击提交审核
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="StockBills_menu0"]/span[1]').click()  #点击详情
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[2]/div[3]/span[4]').click()  #点击取消
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="StockBills_menu0"]/span[2]').click()  #点击修改
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[2]/td[12]/input[5]').clear()  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit"]/tbody/tr[2]/td[12]/input[5]').send_keys(3)  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="choosekey"]').send_keys(u"碘伏棉签") #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="choose"]/tbody/tr[1]').click()  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="stockIn_edit_save"]').click()  #点击保存
        time.sleep(3)
        browser.find_element_by_xpath('//*[@id="StockBills_menu0"]/span[4]').click()  #点击审核
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="stockIn_edit_check"]').click()#在审核页点击审核
        time.sleep(2)






if __name__ == '__main__':
    unittest.main()