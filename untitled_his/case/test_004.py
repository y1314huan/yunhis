# coding:utf-8
#历史处方的查看、引用
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import datetime
browser = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")  # chromedriver.exe文件的路径
# p = Browser()
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
        global browser
        browser.maximize_window()
        # browser.get("http://yun.oasisapp.cn:9080/uc/authentication/check?login=true&phone=&redirectUrl=http://yun.oasisapp.cn:8080/yunhis/security_check.action")
        # ## 测试地址

        browser.get("http://47.93.156.153:9090/uc/authentication/check?login=true&phone=&redirectUrl=http://47.93.156.153:8090/yunhis/security_check.action")
        # 准正式地址

        # browser.get("http://his.oasiscare.cn/uc/authentication/check?login=true&phone=&redirectUrl=http://his.oasiscare.cn:80/yunhis/security_check.action")
        # #正式地址
        time.sleep(2)
        print ("setUp")
    @classmethod
    def tearDownClass(cls):
        browser.quit()
        time.sleep(2)
        print ("TearDown")

    #登录
    def test001(self):
        browser.find_element_by_id("username").clear()  # 清空账号输入框
        browser.find_element_by_id("username").send_keys("17444444444")  # 输入用户名
        browser.find_element_by_id("password").clear()  # 清空密码输入框
        browser.find_element_by_id("password").send_keys("444444")  # 输入密码
        browser.find_element_by_id("loginBtn").click()  # 点击登录
        time.sleep(2)
        # browser.find_element_by_xpath('//*[@id="#clinics"]/li[1]').click()#正式环境云his测试诊所
        browser.find_element_by_xpath('//*[@id="#clinics"]/li[2]').click()  # 选择泓华金融街诊所测试和准正式
        time.sleep(5)
        print ("登录成功")






    def test_HistoricalCases(self):
        browser.find_element_by_xpath('/html/body/div[3]/aside/section/ul/li[3]/a').click()  # 点击预约挂号
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="registerName_input"]').send_keys(u"董焕焕")  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="registerName_searchRelate"]/p[1]').click()  # 列表中选择董焕焕
        time.sleep(3)
        browser.find_element_by_xpath('//*[@id="presprint_1"]').click()  # 点击保存与打印
        time.sleep(2)
        browser.back()
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/div[3]/aside/section/ul/li[4]/a/span[1]').click()  # 点击医生工作台
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="doctorDesk_nav"]/ul/li[1]/a').click()  # 点击今日就诊
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="doctor_patient_cart_content"]/div/div[2]/span[1]').click()  # 点击接诊
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="seeDoctoring_nav"]/ul/li[1]/a').click()  # 点击病例
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="HistoryCase"]').click()  # 点击历史病例
        time.sleep(2)
        browser.current_window_handle
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, "layui-layer-setwin")))  # 点击总关闭
        ys.click()
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="seeDoctoring_nav"]/ul/li[2]/a').click()  # 点击检验项目
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="HistoryCase"]').click()  # 点击查看历史病例
        time.sleep(2)
        browser.current_window_handle
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, "layui-layer-setwin")))  # 点击总关闭
        ys.click()
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="seeDoctoring_nav"]/ul/li[3]/a').click()  # 点击检查项目
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="HistoryCase"]').click()  # 点击查看历史病例
        time.sleep(2)
        browser.current_window_handle
        time.sleep(2)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, "layui-layer-setwin")))  # 点击总关闭
        ys.click()
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="seeDoctoring_nav"]/ul/li[4]/a').click()  # 点击治疗
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="HistoryCase"]').click()  # 点击查看历史病例
        time.sleep(2)
        browser.current_window_handle
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, "layui-layer-setwin")))  # 点击总关闭
        ys.click()
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="seeDoctoring_nav"]/ul/li[5]/a').click()  # 点击处方
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="HistoryCase"]').click()  # 点击查看历史病例
        time.sleep(2)
        browser.current_window_handle
        ys = WebDriverWait(browser ,20 ,0.5).until(EC.presence_of_element_located((By.XPATH ,'//*[@id="caseLists"]/li/div[1]/span[4]'))  )  # 点击总的展开
        ys.click()
        time.sleep(2)
        ys = WebDriverWait(browser ,20 ,0.5).until(EC.presence_of_element_located((By.XPATH ,'//*[@id="caseLists"]/li/div[2]/h4/span'))  )  # 点击病例处的展开
        ys.click()
        time.sleep(2)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="caseLists"]/li/div[2]/h4/span')))
        ys.click()# 点击病例处的收起
        time.sleep(2)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="caseLists"]/li/div[2]/div[5]/h4/span[1]')))  # 点击处方处的展开
        ys.click()
        time.sleep(2)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="caseLists"]/li/div[2]/div[5]/h4/span[1]')))  # 点击处方处的收起
        ys.click()
        time.sleep(2)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="caseLists"]/li/div[2]/div[6]/div/h4/span')))  # 点击中药处方处的展开
        ys.click()
        time.sleep(2)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="caseLists"]/li[1]/div[2]/div[6]/div/h4/span')))  # 点击中药处方处的收起
        ys.click()
        time.sleep(2)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="caseLists"]/li[1]/div[2]/div[5]/h4/span[2]')))  # 点击引用处方
        ys.click()
        time.sleep(2)
        target = browser.find_element_by_xpath('//*[@id="caseLists"]/li/div[2]/div[6]/div/h4')  #
        browser.execute_script("arguments[0].scrollIntoView();", target)  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="seeDoctoring_nav"]/ul/li[6]/a').click()  # 点击草药处方
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="HistoryCase"]').click()  # 点击查看历史病例
        time.sleep(2)
        browser.current_window_handle
        time.sleep(2)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="caseLists"]/li[1]/div[1]/span[4]')))
        ys.click()  #点击总的展开
        time.sleep(2)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="caseLists"]/li[1]/div[2]/div[6]/div/h4/span')))  #
        ys.click()  #点击中药处方的展开
        time.sleep(2)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="caseLists"]/li[1]/div[2]/div[6]/div/div/ul/li[1]/p[1]/span[2]')))  #
        ys.click()  #点击引用该处方
        time.sleep(2)


if __name__ == '__main__':
    unittest.main()