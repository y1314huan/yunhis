# coding:utf-8
#1、挂账管理的多种支付。2、保险回款

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
browser = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")  # chromedriver.exe文件的路径
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










#挂账管理
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/div[3]/aside/section/ul/li[9]').click()  #点击收费发药
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/ul/li[5]').click()  #点击挂账管理
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="char5_date1"]').click()  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="laydate_YY"]/label').click()  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="laydate_ys"]/li[1]').click()  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="laydate_ok"]').click()  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/div/ul/li[2]/span/span[1]/span/span[2]').click()  #点击收银员
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u"董焕焕")  #测试
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/div/ul/li[2]/span/span[1]/span/span[2]').click()  # 点击收银员测试
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u"全部")  #
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)  #
        time.sleep(1)
        browser.find_element_by_id("orderNumber").send_keys("171031192600205")
        time.sleep(1)
        browser.find_element_by_css_selector("button.searchBtn").click()
        time.sleep(1)
        browser.find_element_by_id("orderNumber").clear()
        browser.find_element_by_id("orderNumber").send_keys("")
        browser.find_element_by_id("patientMessage").clear()
        browser.find_element_by_id("patientMessage").send_keys(u"董焕焕")
        browser.find_element_by_css_selector("button.searchBtn").click()
        time.sleep(1)
        browser.find_element_by_id("patientMessage").clear()
        browser.find_element_by_id("patientMessage").send_keys("18611059298")
        browser.find_element_by_css_selector("button.searchBtn").click()
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/div/div/div').click()  #导出Excel表格
        time.sleep(2)
        browser.find_element_by_id("patientMessage").clear()
        browser.find_element_by_css_selector("button.searchBtn").click()
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="gztable"]/tbody/tr[1]/td[10]').click()  #点击详情
        time.sleep(2)
        target = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[2]/div[2]/div[7]/span[2]')  #
        browser.execute_script("arguments[0].scrollIntoView();", target)  #滑动到打印
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[2]/div[2]/div[7]/span[1]').click()  #点击收费
        time.sleep(5)


        browser.current_window_handle  # 此行代码用来定位当前页面
        time.sleep(5)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layui-layer11"]/div[2]/div/ul/li[2]/div[1]/i[1]')))  #
        ys.click()  #选择现金
        time.sleep(5)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layui-layer11"]/div[2]/div/ul/li[2]/div[1]/input')))  #
        ys.clear()
        ys.send_keys(u"645.00") # 输入现金金额
        time.sleep(5)
        ys = WebDriverWait(browser, 20, 0.5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="layui-layer11"]/div[2]/div/ul/li[2]/div[2]/i[1]')))  #
        ys.click()  # 选择刷卡
        time.sleep(5)
        ys = WebDriverWait(browser, 20, 0.5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="layui-layer11"]/div[2]/div/ul/li[2]/div[2]/input')))  #
        ys.clear()
        ys.send_keys(u"500.00")  # 输入刷卡金额
        time.sleep(5)
        # ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layui-layer11"]/div[2]/div/ul/li[3]/div[1]/i[1]')))  #
        # ys.click()  #选择微信
        # time.sleep(5)
        # ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layui-layer11"]/div[2]/div/ul/li[3]/div[1]/input')))  #
        # ys.clear()
        # ys.send_keys(u"0.01")  # 输入微信金额
        # time.sleep(5)
        # ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layui-layer11"]/div[2]/div/ul/li[3]/div[2]/i[1]')))  #
        # ys.click()  #选择支付宝
        # time.sleep(5)
        # ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layui-layer11"]/div[2]/div/ul/li[3]/div[2]/input')))  #
        # ys.clear()
        # ys.send_keys(u"0.01")  # 输入支付宝金额
        # time.sleep(5)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layui-layer11"]/div[2]/div/ul/li[4]/div[1]/i[1]')))  #个人汇款
        ys.click()  # 选择个人汇款
        time.sleep(5)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layui-layer11"]/div[2]/div/ul/li[4]/div[1]/input')))  # 输入个人汇款金额
        ys.clear()
        ys.send_keys(u"500")  # 输入个人汇款金额
        time.sleep(5)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="layui-layer11"]/div[2]/div/ul/li[4]/div[2]/i[1]')))  # 公司汇款
        ys.click()  # 选择公司汇款
        time.sleep(5)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layui-layer11"]/div[2]/div/ul/li[4]/div[2]/input')))  # 公司汇款
        ys.clear()
        ys.send_keys(u"500")  # 输入公司汇款金额
        time.sleep(5)
        # ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layui-layer11"]/div[2]/div/ul/li[5]/div[1]/i[1]')))  # 选择储值卡
        # ys.click()  # 选择储值卡
        # time.sleep(5)
        # ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layui-layer11"]/div[2]/div/ul/li[5]/div[1]/input')))  # 储值卡输入金额
        # ys.clear()
        # ys.send_keys(u"500")   # 储值卡输入金额
        time.sleep(5)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="layui-layer11"]/div[2]/div/ul/li[5]/div[2]/i[1]')))  # 选择其他
        ys.click()  # 选择其他
        time.sleep(5)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="layui-layer11"]/div[2]/div/ul/li[5]/div[2]/input')))  # 其他输入金额
        ys.clear()
        ys.send_keys(u"1000")  # 其他输入金额
        time.sleep(5)
        target = browser.find_element_by_xpath('//*[@id="print_buying"]')  #滑动到确定
        browser.execute_script("arguments[0].scrollIntoView();", target)  #
        time.sleep(2)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="print_buying"]')))  #
        ys.click()  #点击确定
        time.sleep(5)
        browser.back()








# #保险回款
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/div[3]/aside/section/ul/li[9]').click()  #点击收费发药
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/ul/li[6]/a').click()  #点击保险回款
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="char6_date1"]').click()  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="laydate_YY"]/label').click()  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="laydate_ys"]/li[1]').click()  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="laydate_ok"]').click()  #
        time.sleep(10)
        ys = WebDriverWait(browser, 40, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ajax-content"]/div/div/div[1]/ul[1]/li[2]/input[1]')))  #
        ys.send_keys(u"0")  #待回款金额
        time.sleep(5)
        ys = WebDriverWait(browser, 40, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ajax-content"]/div/div/div[1]/ul[1]/li[2]/input[2]')))  #
        ys.send_keys(u"700")  #待回款金额
        time.sleep(5)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ajax-content"]/div/div/div[1]/ul[1]/li[2]/input[2]')))#
        ys.clear()  #清除待回款金额
        time.sleep(5)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ajax-content"]/div/div/div[1]/ul[1]/li[2]/input[1]')))#
        ys.clear()  #清除待回款金额
        time.sleep(20)
        ys = WebDriverWait(browser, 30, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ajax-content"]/div/div/div[1]/ul[1]/li[3]/span/span[1]/span/span[2]')))  #
        ys.click()  #点击保险公司
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u"兴业银行")  #
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)
        time.sleep(5)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/div[1]/ul[1]/li[3]/span/span[1]/span/span[2]').click()  #点击保险公司
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u"全部")  #
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)
        time.sleep(10)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="charge6_no"]')))#
        ys.click()#
        time.sleep(10)
        browser.find_element_by_xpath('//*[@id="charge6_nozero"]').click()  #勾选拒付非0
        time.sleep(5)
        browser.find_element_by_xpath('//*[@id="charge6_no"]').click()  #去掉勾选0回款
        time.sleep(5)
        browser.find_element_by_xpath('//*[@id="charge6_nozero"]').click()  #去掉勾选拒付非0
        time.sleep(5)
        browser.find_element_by_xpath('//*[@id="patientMessage"]').send_keys(u"董焕焕")  #
        time.sleep(10)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#ajax-content > div > div > div.charge6_head > ul.container-fluid.charge6_head2 > li > button")))  #
        ys.click()  #点击查询
        time.sleep(5)
        browser.find_element_by_xpath('//*[@id="patientMessage"]').clear()  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="patientMessage"]').send_keys(u"18611059298")  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/div[1]/ul[2]/li/button').click()  #点击查询
        time.sleep(8)
        browser.find_element_by_xpath('//*[@id="charge6_table"]/tbody/tr[1]/td[11]/span[1]').click()  #点击回款
        time.sleep(2)
        browser.current_window_handle  # 此行代码用来定位当前页面
        time.sleep(2)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, "charge6_popu1Inp")))  #
        ys.send_keys(u"0.01")  #
        time.sleep(1)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="charge6_popu1time"]')))  #
        ys.clear()  #
        ys.send_keys(u"2017-11-01")  #
        time.sleep(1)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, "charge6_popu1_remark")))  #
        ys.send_keys(u"保险回款")  #
        time.sleep(2)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, "charge6_popu1_btn")))  #
        ys.click()  #点击确定
        time.sleep(8)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#charge6_table > tbody > tr:nth-child(1) > td.long.noExl > span.refuseMoney")))  #
        ys.click()  #点击拒付
        time.sleep(5)
        browser.current_window_handle  # 此行代码用来定位当前页面
        time.sleep(2)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, 'charge6_popu2Inp')))  #
        ys.send_keys(u"200")
        time.sleep(1)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, "charge6_popu2time")))  #
        ys.clear()  #
        ys.send_keys(u"2017-11-05")
        time.sleep(1)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, "charge6_popu2_remark")))  #
        ys.send_keys(u"拒付")
        time.sleep(1)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, "charge6_popu2_btn")))  #
        ys.click()  #点击确定
        time.sleep(8)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#charge6_table > tbody > tr:nth-child(1) > td.long.noExl > span.seeNote")))#
        ys.click()#点击查看备注
        time.sleep(2)
        browser.current_window_handle  # 此行代码用来定位当前页面
        time.sleep(5)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, 'layui-layer-setwin')))  #
        ys.click()  #点击关闭
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/div[2]/div/span').click()  #点击导出Excel
        time.sleep(2)








if __name__ == '__main__':
    unittest.main()