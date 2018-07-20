# coding:utf-8
#医生工作台其他收费项目价格的修改
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

    # #登录
    # def test001(self):
    #     browser.find_element_by_id("username").clear()  # 清空账号输入框
    #     browser.find_element_by_id("username").send_keys("17444444444")  # 输入用户名
    #     browser.find_element_by_id("password").clear()  # 清空密码输入框
    #     browser.find_element_by_id("password").send_keys("444444")  # 输入密码
    #     browser.find_element_by_id("loginBtn").click()  # 点击登录
    #     time.sleep(2)
    #     browser.find_element_by_xpath(".//*[@id='#clinics']/li[2]").click()  # 选择泓华金融街诊所测试和准正式
    #     # browser.find_element_by_xpath('//*[@id="#clinics"]/li[1]').click()#正式环境云his测试诊所
    #     time.sleep(5)
    #     print ("登录成功")


    #签到接诊
    def test002(self):
        browser.find_element_by_xpath('/html/body/div[3]/aside/section/ul/li[2]/ul/li[1]/a').click()  # 点击预约挂号
        time.sleep(5)
        browser.find_element_by_xpath('//*[@id="registerName_input"]').send_keys(u"修改其他收费")  # 输入姓名
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="telephonNum"]').send_keys("18611059298")  # 输入手机号
        browser.find_element_by_xpath('//*[@id="appointment_nav"]/ul').click()  # 点击空白处
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="select2-Order_startTime-container"]').click()  # 点击就诊时间的开始时间
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u"8:00")  # 就诊时间的开始时间输入9:00
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)  # 就诊时间的开始时间选择9:00
        browser.find_element_by_xpath('//*[@id="select2-Order_endTime-container"]').click()  # 点击结束时间
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u"8:30")  # 在结束时间输入10:00
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)  # 选择10:00
        browser.find_element_by_xpath('//*[@id="addRegister_save"]').click()  # 点击保存
        time.sleep(5)
        print("预约挂号成功")
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/div[3]/aside/section/ul/li[2]/ul/li[2]/a').click()  # 点击医生工作台
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="doctor_patient_cart_content"]/div/div[2]/span[1]').click()  #点击接诊
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="seeDoctoring_nav"]/ul/li[5]/a').click()  #点击处方
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="addOtherFee"]').send_keys(u"专家异地出诊交通费1")  #输入专家异地出诊交通费1
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="addOtherRelateList"]/p/span[1]').click()  #选择专家异地出诊交通费1
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="otherFeeContent"]/form/div/div[3]/input').clear()  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="otherFeeContent"]/form/div/div[3]/input').send_keys(u"3")  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="otherFeeContent"]/form/span/input').clear()  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="otherFeeContent"]/form/span/input').send_keys(u"2000")  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div[1]/div[2]/p[3]').click()  #点击结束就诊
        time.sleep(2)
        browser.current_window_handle  # 此行代码用来定位当前页面
        time.sleep(2)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="offMadicalMess"]/div/a/button')))  #
        ys.click()  #
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/div[3]/aside/section/ul/li[2]/ul/li[7]/a').click()  #点击收费发药
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/ul/li[2]/a').click()  #点击收费
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="constList"]/div[2]/ul/li[1]/div/div[3]').click()  #点击追加
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="addOtherFee"]').send_keys(u"2")  #输入专家异地出诊交通费2
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="addOtherRelateList"]/p/span[1]').click()  #专家异地出诊交通费2
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="addSave"]').click()  #点击保存并收费
        time.sleep(4)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/aside/section/ul/li[2]/ul/li[2]/a')))  #
        ys.click()  #点击医生工作台
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="patient_state_tab"]/li[3]').click()  # 点击已完成
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="doctor_patient_cart_content"]/div[1]/div[2]/a[2]').click()  #点击完善病例
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="seeDoctoring_nav"]/ul/li[5]/a').click()  #点击处方
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="addOtherFee"]').send_keys(u"2")  #输入专家异地出诊交通费2
        time.sleep(4)
        browser.find_element_by_xpath('//*[@id="addOtherRelateList"]/p/span[1]').click()  #选择专家异地出诊交通费2
        time.sleep(5)
        browser.find_element_by_xpath('//*[@id="addOtherFee"]').send_keys(u"3")  #输入专家异地出诊交通费3
        time.sleep(5)
        browser.find_element_by_xpath('//*[@id="addOtherRelateList"]/p/span[1]').click()  #选择专家异地出诊交通费3
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="prescription_save"]').click()  #点击保存
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/div[3]/aside/section/ul/li[2]/ul/li[7]/a').click()  #点击收费发药
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/ul/li[2]/a').click()  #点击收费
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="constList"]/div[2]/ul/li[1]/div/div[3]').click()  #点击追加
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="addOtherFee"]').send_keys(u"3")  #专家异地出诊交通费3
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="addOtherRelateList"]/p/span[1]').click()  #选择专家异地出诊交通费3
        time.sleep(5)
        browser.find_element_by_xpath('//*[@id="addSave"]').click()  #点击保存与收费
        time.sleep(5)
        browser.find_element_by_xpath('//*[@id="checkform"]/div/div[2]/div[6]/div/table/tbody/tr[2]/td[8]/i').click()  #点击删除
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="addOtherFee"]').send_keys(u"4")  #输入专家异地出诊交通费4
        time.sleep(5)
        browser.find_element_by_xpath('//*[@id="addOtherRelateList"]/p/span[1]').click()  #选择专家异地出诊交通费4
        time.sleep(4)
        browser.find_element_by_xpath('//*[@id="addSave"]').click()  #点击保存与收费
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/form/div/div[2]/div[5]/div/table/thead/tr/th[8]').click()  # 点击空白
        time.sleep(2)
        target = browser.find_element_by_xpath('//*[@id="buying_credit"]')  #滑动到挂账
        browser.execute_script("arguments[0].scrollIntoView();", target)  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/form/div/div[2]/div[10]/p[1]/i').click()  #点击收费
        time.sleep(2)
        browser.current_window_handle  # 此行代码用来定位当前页面
        time.sleep(5)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layui-layer43"]/div[2]/div/ul/li[2]/div[1]/i[1]')))  #
        ys.click()  #选择现金
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="layui-layer43"]/div[2]/div/ul/li[2]/div[1]/input').clear()  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="layui-layer43"]/div[2]/div/ul/li[2]/div[1]/input').send_keys(u"11000.00")  #
        time.sleep(3)
        browser.find_element_by_xpath('//*[@id="print_buying"]').click()  #点击确定
        time.sleep(3)
        browser.back()







if __name__ == '__main__':
    unittest.main()