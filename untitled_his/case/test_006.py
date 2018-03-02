# coding:utf-8
#1、直接售药及直接售药的退费（包括全退、部分退）。2、盘库，库存管理，成本管理、汇总查询，结算管理。
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





#直接售药
#直接售药及直接售药的退费（包括全退、部分退）
    def test_sell_drugs(self):
        time.sleep(2)
        browser.find_element_by_css_selector("a.ajax-charge.ShouFei_a > span").click()  #点击收费、发药
        time.sleep(2)
        browser.find_element_by_link_text(u"直接售药").click()  # 点击直接售药
        time.sleep(2)
        browser.find_element_by_name("name").click()  #
        browser.find_element_by_name("name").clear()  #
        browser.find_element_by_name("name").send_keys(u"直接售药")  # 输入姓名
        browser.find_element_by_name("mobile").click()  #
        browser.find_element_by_name("mobile").clear()  #
        browser.find_element_by_name("mobile").send_keys("18611059298")  # 输入手机号
        browser.find_element_by_id("female").click()  #
        browser.find_element_by_name("age").clear()  #
        browser.find_element_by_name("age").send_keys("30")  # 输入年龄
        browser.find_element_by_id("hidden_search_yao").clear()  #
        browser.find_element_by_id("hidden_search_yao").send_keys(u"阿奇霉素注射液")  # 输入药品阿奇霉素注射液
        time.sleep(1)
        browser.find_element_by_xpath("//tbody[@id='cont_yaos']/tr/td[4]").click()  # 选择药品阿奇霉素注射液
        time.sleep(1)
        browser.find_element_by_id("hidden_search_yao").clear()  #
        browser.find_element_by_id("hidden_search_yao").send_keys(u"达克宁")  # 输入药品达克宁
        time.sleep(1)
        browser.find_element_by_xpath("//tbody[@id='cont_yaos']/tr/td[3]").click()  # 选择药品达克宁
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[1]/form/table/tbody/tr[2]/td[9]/input').clear()  #
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[1]/form/table/tbody/tr[2]/td[9]/input').send_keys("2")  # 输入数量
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="select2-charge3_fee-container"]').click()  #点击费别处的请选择
        browser.find_element_by_css_selector("input.select2-search__field").clear()  #
        browser.find_element_by_css_selector("input.select2-search__field").send_keys(u"VIP会员")  # 输入费别
        browser.find_element_by_css_selector("input.select2-search__field").send_keys(Keys.ENTER) #选择费别
        time.sleep(1)
        browser.find_element_by_css_selector("input.privilege").clear()  #
        browser.find_element_by_css_selector("input.privilege").send_keys("16.28")  # 输入优惠金额
        time.sleep(2)
        target = browser.find_element_by_xpath('//*[@id="suer_order"]')  # 滑动到代收付页面最底部
        browser.execute_script("arguments[0].scrollIntoView();", target)  # 滑动到代收付页面最底部
        time.sleep(2)
        browser.find_element_by_id("suer_order").click()  # 点击收费
        time.sleep(2)
        browser.current_window_handle
        time.sleep(2)
        browser.find_element_by_css_selector("p.charge3_poup_btn").click()  # 弹窗中点击确定
        time.sleep(2)
        browser.current_window_handle
        time.sleep(2)
        browser.find_element_by_xpath("(//input[@name='chioce_radio'])[3]").click()  # 收费弹窗中点击微信
        time.sleep(1)
        browser.find_element_by_xpath("(//input[@name='chioce_radio'])[4]").click()  # 收费弹窗中点击支付宝
        time.sleep(1)
        browser.find_element_by_xpath("(//input[@name='chioce_radio'])[2]").click()  # 收费弹窗中点击刷卡
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="suerPrint"]').click()  #收费弹窗中点击确定
        time.sleep(4)
        browser.back()
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/ul/li[4]').click()  #点击结算管理
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="table_excel"]/tbody/tr[1]/td[14]/a').click()  #点击详情
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[2]/div[9]/span').click()  #点击修改打印账单
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="settledate1"]').clear()  #修改日期
        browser.find_element_by_xpath('//*[@id="settledate1"]').send_keys(u"2017-12-18")  #修改日期
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[2]/div[5]/table/tbody/tr[1]/td[2]/input').send_keys(u"修改药品名称")  #修改药品名称
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[2]/div[5]/table/tbody/tr[1]/td[5]/input').send_keys(u"修改药品名称")  #修改售价单位
        browser.find_element_by_xpath('//*[@id="printgroup1"]/span[1]').click()  #点击打印
        time.sleep(2)
        browser.back()  # 浏览器返回
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="table_excel"]/tbody/tr[1]/td[14]/a').click()  # 点击详情
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[2]/div[9]/a/span').click()  #点击退费
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[2]/div[7]/div[2]/p').send_keys(u"不想要了")  #
        time.sleep(2)
        target = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[2]/div[11]/span')  # 滑动到提交处
        browser.execute_script("arguments[0].scrollIntoView();", target)  # 滑动到代收付页面最底部
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[2]/div[11]/span').click()  #点击提交
        time.sleep(2)
        browser.current_window_handle
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="layui-layer1"]/div[2]/div/p').click()  # 弹窗中点击确定
        time.sleep(2)
        browser.current_window_handle
        time.sleep(2)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layui-layer2"]/div[3]/a[1]')))  #
        ys.click()  #点击确认
        time.sleep(4)
        browser.back()  # 浏览器返回
        time.sleep(3)
        browser.find_element_by_css_selector("a.ajax-charge.ShouFei_a > span").click()  # 点击收费、发药
        time.sleep(2)
        browser.find_element_by_link_text(u"直接售药").click()  # 点击直接售药
        time.sleep(2)
        browser.find_element_by_name("name").click()  #
        browser.find_element_by_name("name").clear()  #
        browser.find_element_by_name("name").send_keys(u"直接售药")  # 输入姓名
        time.sleep(2)
        browser.find_element_by_name("mobile").click()  #
        browser.find_element_by_name("mobile").clear()  #
        browser.find_element_by_name("mobile").send_keys("18611059298")  # 输入手机号
        browser.find_element_by_id("female").click()  #
        browser.find_element_by_name("age").clear()  #
        browser.find_element_by_name("age").send_keys("30")  # 输入年龄
        browser.find_element_by_id("hidden_search_yao").clear()  #
        browser.find_element_by_id("hidden_search_yao").send_keys(u"阿奇霉素注射液")  # 输入药品阿奇霉素注射液
        time.sleep(1)
        browser.find_element_by_xpath("//tbody[@id='cont_yaos']/tr/td[4]").click()  # 选择药品阿奇霉素注射液
        time.sleep(1)
        browser.find_element_by_id("hidden_search_yao").clear()  #
        browser.find_element_by_id("hidden_search_yao").send_keys(u"达克宁")  # 输入药品达克宁
        time.sleep(1)
        browser.find_element_by_xpath("//tbody[@id='cont_yaos']/tr/td[3]").click()  # 选择药品达克宁
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[1]/form/table/tbody/tr[2]/td[9]/input').clear()  #
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[1]/form/table/tbody/tr[2]/td[9]/input').send_keys("2")  # 输入数量
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="select2-charge3_fee-container"]').click()  # 点击费别处的请选择
        browser.find_element_by_css_selector("input.select2-search__field").clear()  #
        browser.find_element_by_css_selector("input.select2-search__field").send_keys(u"VIP会员")  # 输入费别
        browser.find_element_by_css_selector("input.select2-search__field").send_keys(Keys.ENTER)  # 选择费别
        time.sleep(2)
        target = browser.find_element_by_xpath('//*[@id="suer_order"]')  # 滑动到代收付页面最底部
        browser.execute_script("arguments[0].scrollIntoView();", target)  # 滑动到代收付页面最底部
        time.sleep(2)
        browser.find_element_by_id("suer_order").click()  # 点击收费
        time.sleep(2)
        browser.current_window_handle
        time.sleep(2)
        browser.find_element_by_css_selector("p.charge3_poup_btn").click()  # 弹窗中点击确定
        time.sleep(2)
        browser.current_window_handle
        time.sleep(2)
        browser.find_element_by_xpath("(//input[@name='chioce_radio'])[3]").click()  # 收费弹窗中点击微信
        time.sleep(1)
        browser.find_element_by_xpath("(//input[@name='chioce_radio'])[4]").click()  # 收费弹窗中点击支付宝
        time.sleep(1)
        browser.find_element_by_xpath("(//input[@name='chioce_radio'])[2]").click()  # 收费弹窗中点击刷卡
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="suerPrint"]').click()  # 收费弹窗中点击确定
        time.sleep(2)
        browser.back()  # 浏览器返回
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/ul/li[4]').click()  # 点击结算管理
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="table_excel"]/tbody/tr[1]/td[14]/a').click()  # 点击详情
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[2]/div[9]/span').click()  # 点击打印账单
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="settledate1"]').clear()  #修改日期
        browser.find_element_by_xpath('//*[@id="settledate1"]').send_keys(u"2017-12-18")  #修改日期
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[2]/div[5]/table/tbody/tr[1]/td[2]/input').send_keys(u"修改药品名称")  #修改药品名称
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[2]/div[5]/table/tbody/tr[1]/td[5]/input').send_keys(u"修改药品名称")  #修改售价单位
        browser.find_element_by_xpath('//*[@id="printgroup1"]/span[1]').click()  #点击打印
        time.sleep(2)
        browser.back()  # 浏览器返回
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="table_excel"]/tbody/tr[1]/td[14]/a').click()  # 点击详情
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[2]/div[9]/a/span').click()  # 点击退费
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[2]/div[5]/table/tbody/tr[1]/td[1]/label').click()  # 选择退费项目
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[2]/div[7]/div[2]/p').send_keys(u"不想要了")  #
        time.sleep(2)
        target = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[2]/div[11]/span')  # 滑动到提交处
        browser.execute_script("arguments[0].scrollIntoView();", target)  # 滑动到代收付页面最底部
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[2]/div[11]/span').click()  # 点击提交
        time.sleep(2)
        browser.current_window_handle
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="layui-layer1"]/div[2]/div/p').click()  # 弹窗中点击确定
        time.sleep(2)
        browser.current_window_handle
        time.sleep(2)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layui-layer2"]/div[3]/a[1]')))  #
        ys.click()  # 点击确认
        time.sleep(2)
        browser.back()  # 浏览器返回
        time.sleep(2)







# #盘库
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="medical"]').click()  #点击药房
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="content"]/div[3]/div/div/ul/li[3]').click()  #点击盘库单管理
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="startDate"]').clear()  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="startDate"]').send_keys(u"2010-11-07")  #开始日期输入2010-11-07
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="home_search"]').click()  #点击查询
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="home_param"]/div[3]/select').click()  #点击盘点人
        time.sleep(1)
        # InputType = Select(browser.find_element_by_xpath('//*[@id="home_param"]/div[3]/select'))
        # InputType.select_by_value("170831113200005")#盘点人选择董焕焕
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="home_search"]').click()  #点击查询
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="home_param"]/div[3]/select').click()  #点击盘点人
        time.sleep(1)
        InputType = Select(browser.find_element_by_xpath('//*[@id="home_param"]/div[3]/select'))
        InputType.select_by_value("")  # 盘点人选择请选择
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="home_param"]/div[2]/select').click()  #点击库房
        time.sleep(1)
        InputType = Select(browser.find_element_by_xpath('//*[@id="home_param"]/div[2]/select'))
        InputType.select_by_value("1")  # 库房选择全库
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="home_search"]').click()  #点击查询
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="home_param"]/div[2]/select').click()  #点击库房
        time.sleep(1)
        InputType = Select(browser.find_element_by_xpath('//*[@id="home_param"]/div[2]/select'))
        InputType.select_by_value("2")  # 库房选择药品
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="home_search"]').click()  # 点击查询
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="home_param"]/div[2]/select').click()  # 点击库房
        time.sleep(1)
        InputType = Select(browser.find_element_by_xpath('//*[@id="home_param"]/div[2]/select'))
        InputType.select_by_value("3")  # 库房选择耗材
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="home_search"]').click()  # 点击查询
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="home_param"]/div[2]/select').click()  # 点击库房
        time.sleep(1)
        InputType = Select(browser.find_element_by_xpath('//*[@id="home_param"]/div[2]/select'))
        InputType.select_by_value("")  # 库房选择请选择
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="home_param"]/div[1]/select').click()  #点击状态处的请选择
        time.sleep(1)
        InputType = Select(browser.find_element_by_xpath('//*[@id="home_param"]/div[1]/select'))
        InputType.select_by_value("1")  # 库房选择待审核
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="home_search"]').click()  # 点击查询
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="home_param"]/div[1]/select').click()  # 点击状态处的请选择
        time.sleep(1)
        InputType = Select(browser.find_element_by_xpath('//*[@id="home_param"]/div[1]/select'))
        InputType.select_by_value("2")  # 库房选择已审核
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="home_search"]').click()  # 点击查询
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="home_param"]/div[1]/select').click()  # 点击状态处的请选择
        time.sleep(1)
        InputType = Select(browser.find_element_by_xpath('//*[@id="home_param"]/div[1]/select'))
        InputType.select_by_value("0")  # 库房选择暂存
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="home_search"]').click()  # 点击查询
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="home_param"]/div[1]/select').click()  # 点击状态处的请选择
        time.sleep(1)
        InputType = Select(browser.find_element_by_xpath('//*[@id="home_param"]/div[1]/select'))
        InputType.select_by_value("")  # 库房选择请选择
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="search"]').send_keys(u"P170929094000029")  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="home_param"]/div[6]').click()  #点击查询
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[1]/div[2]/button').click()  #点击新增盘库单
        time.sleep(2)
        browser.current_window_handle  # 此行代码用来定位当前页面
        time.sleep(2)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#layui-layer12 > div.layui-layer-btn.layui-layer-btn-c > a.layui-layer-btn0')))  #
        ys.click()  #在弹窗中点击是
        # browser.find_element_by_xpath('//*[@id="layui-layer12"]/div[3]/a[1]').click()  #在弹窗中点击是
        time.sleep(2)
        browser.current_window_handle  # 此行代码用来定位当前页面
        time.sleep(2)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layui-layer13"]/div[3]/a[1]')))  #
        ys.click()  # #在弹窗中点击是
        time.sleep(5)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ajax-content"]/div/div/div[2]/ul/li[1]/ul/li/div[3]/div/input[3]')))  #
        ys.click()  #点击库存非0
        time.sleep(5)
        ys = WebDriverWait(browser, 40, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ajax-content"]/div/div/div[2]/ul/li[1]/ul/li/div[3]/div/input[1]')))  #
        ys.click()  # 点击隐藏库存
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/div[2]/ul/li[1]/ul/li/div[1]/select').click()  #点击库房
        time.sleep(5)
        InputType = Select(browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/div[2]/ul/li[1]/ul/li/div[1]/select'))
        InputType.select_by_value("1")#选择药品
        time.sleep(10)
        browser.find_element_by_xpath('//*[@id="select2-DrugName-container"]').click()  #点击药品搜索
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u"阿奇霉素注射液")  #
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="searchMedical_body"]/tr[1]/td[13]/input').clear()  #
        browser.find_element_by_xpath('//*[@id="searchMedical_body"]/tr[1]/td[13]/input').send_keys(u"15")
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/div[2]/div[2]/div/button[2]').click()  #点击暂存
        time.sleep(2)
        browser.current_window_handle  # 此行代码用来定位当前页面
        time.sleep(2)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layui-layer19"]/div[3]/a[1]')))  #
        ys.click()  # 点击确定
        time.sleep(5)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[1]/div[2]/button').click()  #点击新增盘库单
        time.sleep(5)
        browser.find_element_by_xpath('//*[@id="menu0"]/span[1]').click()  #点击修改
        time.sleep(10)
        browser.find_element_by_xpath('//*[@id="select2-DrugName1-container"]').click()  #点击搜索药品
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u"硝酸咪康唑阴道软胶囊")  #
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)#搜索药品“硝酸咪康唑阴道软胶囊”
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="detailTable"]/tbody/tr[1]/td[13]/input').clear()  #
        browser.find_element_by_xpath('//*[@id="detailTable"]/tbody/tr[1]/td[13]/input').send_keys(u"20")
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[2]/div[4]/div/button[1]').click()  #点击生产全盘单
        time.sleep(10)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[1]/div[2]/button').click()  #点击新增盘库单
        time.sleep(5)
        browser.find_element_by_xpath('//*[@id="menu0"]/span[1]').click()  #点击详情
        time.sleep(10)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ajax-content"]/div/div[2]/div[3]/button[2]')))  #
        ys.click()  #点击返回
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="menu0"]/span[4]').click()  #点击审核
        time.sleep(10)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ajax-content"]/div/div[2]/div[3]/button[1]')))  #
        ys.click()  # 点击审核
        time.sleep(5)



# #库存管理
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="medical"]').click()  # 点击药房
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="content"]/div[3]/div/div/ul/li[4]').click()  #点击库存管理
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[2]/span').click()  #点击导出Excel
        time.sleep(5)
        browser.find_element_by_xpath('//*[@id="head_form"]/div/ul[1]/li/ul/li[2]/div[1]/label[1]/input').click()  #勾选数量大于0
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="head_form"]/div/ul[1]/li/ul/li[2]/div[1]/label[2]/input').click()  #勾选库存预警
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="head_form"]/div/ul[1]/li/ul/li[1]/div[3]/select').click()  #
        time.sleep(2)
        InputType = Select(browser.find_element_by_xpath('//*[@id="head_form"]/div/ul[1]/li/ul/li[1]/div[3]/select'))
        InputType.select_by_value("90")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="head_form"]/div/ul[1]/li/ul/li[2]/div[2]/label[2]/input').click()  #勾选降序
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="head_form"]/div/ul[1]/li/ul/li[2]/div[4]').click()  #点击查询
        time.sleep(10)
        browser.find_element_by_xpath('//*[@id="head_form"]/div/ul[1]/li/ul/li[2]/div[1]/label[2]/input').click()  #去掉库存预警
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="head_form"]/div/ul[1]/li/ul/li[1]/div[3]/select').click()  #
        time.sleep(2)
        InputType = Select(browser.find_element_by_xpath('//*[@id="head_form"]/div/ul[1]/li/ul/li[1]/div[3]/select'))
        InputType.select_by_value("")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="head_form"]/div/ul[1]/li/ul/li[2]/div[4]').click()  #点击查询
        time.sleep(5)
        browser.find_element_by_xpath('//*[@id="head_form"]/div/ul[1]/li/ul/li[1]/div[1]/select[1]').click()  #点击请选择
        time.sleep(1)
        InputType = Select(browser.find_element_by_xpath('//*[@id="head_form"]/div/ul[1]/li/ul/li[1]/div[1]/select[1]'))
        InputType.select_by_value("1")
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="head_form"]/div/ul[1]/li/ul/li[1]/div[1]/span[2]/span[1]/span/span[2]').click()  #点击全部
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u"未分类")  #
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="head_form"]/div/ul[1]/li/ul/li[1]/div[2]/select').click()  #点击药品状态
        time.sleep(1)
        InputType = Select(browser.find_element_by_xpath('//*[@id="head_form"]/div/ul[1]/li/ul/li[1]/div[2]/select'))
        InputType.select_by_value("1")#药品状态选择启用
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="search"]').send_keys(u"阿莫西林颗粒")  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="head_form"]/div/ul[1]/li/ul/li[2]/div[4]').click()  # 点击查询
        time.sleep(3)
        browser.find_element_by_xpath('//*[@id="table_fenye"]/tbody/tr/td[12]/span[1]').click()  #点击修改
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="table_fenye"]/tbody/tr/td[9]/input[1]').clear()  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="table_fenye"]/tbody/tr/td[9]/input[1]').send_keys(u"2") #修改预警值
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="table_fenye"]/tbody/tr/td[10]/select').click()  #点击是否启用
        time.sleep(2)
        InputType = Select(browser.find_element_by_xpath('//*[@id="table_fenye"]/tbody/tr/td[10]/select'))
        InputType.select_by_value("1")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="table_fenye"]/tbody/tr/td[11]/select').click()  #点击是否允许折扣
        time.sleep(2)
        InputType = Select(browser.find_element_by_xpath('//*[@id="table_fenye"]/tbody/tr/td[11]/select'))
        InputType.select_by_value("1")#是否允许折扣，选择是
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="table_fenye"]/tbody/tr/td[12]/span[2]').click()  #点击保存
        time.sleep(2)


#成本管理
        browser.find_element_by_xpath('/html/body/div[3]/aside/section/ul/li[8]').click()  #点击药房
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="content"]/div[3]/div/div/ul/li[5]').click()  #点击成本管理
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="search"]').send_keys(u"达克宁")  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="head_form"]/div/ul/li/ul/li/div[2]').click()  #点击查询
        time.sleep(5)
        browser.find_element_by_class_name("modify").click()  #点击修改测试环境
        # browser.find_element_by_xpath('//*[@id="9116"]/td[9]/span[1]').click()  #点击修改准正式环境
        time.sleep(1)
        browser.find_element_by_class_name("inpnum").clear()  #测试环境
        # browser.find_element_by_xpath('//*[@id="9116"]/td[6]/input').clear()  #准正式环境
        browser.find_element_by_class_name("inpnum").send_keys(u"20")  #测试环境
        # browser.find_element_by_xpath('//*[@id="9116"]/td[6]/input').send_keys(u"20")  #准正式环境
        time.sleep(1)
        browser.find_element_by_class_name("save").click()  #点击保存测试环境
        # browser.find_element_by_xpath('//*[@id="9116"]/td[9]/span[2]').click()  # 点击保存准正式环境
        time.sleep(2)







# #汇总查询
        time.sleep(3)
        browser.find_element_by_xpath('/html/body/div[3]/aside/section/ul/li[8]').click()  #点击药房
        time.sleep(3)
        browser.find_element_by_xpath('//*[@id="content"]/div[3]/div/div/ul/li[6]/a').click()  #点击汇总查询
        time.sleep(1)
        browser.find_element_by_id("startDate").click()  #
        browser.find_element_by_id("startDate").clear()  #
        browser.find_element_by_id("startDate").send_keys("2010-11-08")  #开始日期输入"2010-11-08"
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[2]/select').click()  #点击全部
        time.sleep(1)
        InputType = Select(browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[2]/select'))
        InputType.select_by_value("1")#自采入库
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[4]').click()  #点击查询
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[2]/select').click()  # 点击全部
        time.sleep(2)
        InputType = Select(browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[2]/select'))
        InputType.select_by_value("2")#外购入库
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[4]').click()  # 点击查询
        time.sleep(3)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[2]/select').click()  # 点击全部
        time.sleep(2)
        InputType = Select(browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[2]/select'))
        InputType.select_by_value("14")#退货入库
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[4]').click()  # 点击查询
        time.sleep(2)


        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[2]/select').click()  # 点击全部
        time.sleep(1)
        InputType = Select(browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[2]/select'))
        InputType.select_by_value("3")  #科室出库
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[4]').click()  # 点击查询
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[2]/select').click()  # 点击全部
        time.sleep(1)
        InputType = Select(browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[2]/select'))
        InputType.select_by_value("4")  #报废出库
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[4]').click()  # 点击查询
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[2]/select').click()  # 点击全部
        time.sleep(1)
        InputType = Select(browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[2]/select'))
        InputType.select_by_value("5")  #退货出库
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[4]').click()  # 点击查询
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[2]/select').click()  # 点击全部
        time.sleep(1)
        InputType = Select(browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[2]/select'))
        InputType.select_by_value("6")  #调拨出库
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[4]').click()  # 点击查询
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[2]/select').click()  # 点击全部
        time.sleep(1)
        InputType = Select(browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[2]/select'))
        InputType.select_by_value("7")  #处方发药
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[4]').click()  # 点击查询
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[2]/select').click()  # 点击全部
        time.sleep(1)
        InputType = Select(browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[2]/select'))
        InputType.select_by_value("8")  #直接售药发药
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[4]').click()  # 点击查询
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[2]/select').click()  # 点击全部
        time.sleep(1)
        InputType = Select(browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[2]/select'))
        InputType.select_by_value("11")  #库存盘盈
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[4]').click()  # 点击查询
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[2]/select').click()  # 点击全部
        time.sleep(1)
        InputType = Select(browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[2]/select'))
        InputType.select_by_value("12")  #库存盘亏
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[4]').click()  # 点击查询
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[2]/select').click()  # 点击全部
        time.sleep(1)
        InputType = Select(browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[2]/select'))
        InputType.select_by_value("13")  #调价
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[4]').click()  # 点击查询
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[2]/select').click()  # 点击全部
        time.sleep(1)
        InputType = Select(browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[2]/select'))
        InputType.select_by_value("")  # 选择全部
        time.sleep(1)
        browser.find_element_by_id("search").clear()  #
        browser.find_element_by_id("search").send_keys(u"阿莫")  #
        browser.find_element_by_id("data_search").click()  #点击查询
        time.sleep(2)



#结算管理
        time.sleep(4)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/aside/section/ul/li[9]/a')))  #
        ys.click()  #点击收费、发药
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/ul/li[4]').click()  #点击结算管理
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="char5_date1"]').click()  #点击开始日期
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="laydate_YY"]/label').click()  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="laydate_ys"]/li[1]').click()  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="laydate_ok"]').click()  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="select2-charge5_cashier-container"]').click()  #点击全部
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u"黄艳南")  #
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="select2-charge5_cashier-container"]').click()  # 点击全部
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u"全部")  #
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)  #
        Select(browser.find_element_by_css_selector("select.form-control.payment")).select_by_visible_text(u"现金")
        time.sleep(1)
        Select(browser.find_element_by_css_selector("select.form-control.payment")).select_by_visible_text(u"刷卡")
        time.sleep(1)
        Select(browser.find_element_by_css_selector("select.form-control.payment")).select_by_visible_text(u"微信")
        time.sleep(1)
        Select(browser.find_element_by_css_selector("select.form-control.payment")).select_by_visible_text(u"支付宝")
        time.sleep(1)
        browser.find_element_by_css_selector("option[value=\"4\"]").click()
        time.sleep(1)
        Select(browser.find_element_by_css_selector("select.form-control.payment")).select_by_visible_text(u"个人汇款")
        time.sleep(1)
        browser.find_element_by_css_selector("option[value=\"5\"]").click()
        time.sleep(1)
        Select(browser.find_element_by_css_selector("select.form-control.payment")).select_by_visible_text(u"公司汇款")
        time.sleep(1)
        Select(browser.find_element_by_css_selector("select.form-control.payment")).select_by_visible_text(u"储值卡")
        time.sleep(1)
        browser.find_element_by_css_selector("option[value=\"7\"]").click()
        time.sleep(1)
        Select(browser.find_element_by_css_selector("select.form-control.payment")).select_by_visible_text(u"其它")
        time.sleep(1)
        browser.find_element_by_css_selector("option[value=\"8\"]").click()
        time.sleep(1)
        Select(browser.find_element_by_css_selector("select.form-control.payment")).select_by_visible_text(u"全部")
        time.sleep(1)
        Select(browser.find_element_by_css_selector("select.form-control.kinds")).select_by_visible_text(u"门诊")
        time.sleep(1)
        Select(browser.find_element_by_css_selector("select.form-control.kinds")).select_by_visible_text(u"零售")
        time.sleep(1)
        browser.find_element_by_css_selector("select.form-control.kinds > option[value=\"2\"]").click()
        time.sleep(1)
        Select(browser.find_element_by_css_selector("select.form-control.kinds")).select_by_visible_text(u"全部")
        time.sleep(1)
        browser.find_element_by_id("orderNumber").clear()
        browser.find_element_by_id("orderNumber").send_keys("171107125600026")
        browser.find_element_by_css_selector("button.searchBtn").click()
        time.sleep(1)
        browser.find_element_by_id("orderNumber").clear()
        browser.find_element_by_id("orderNumber").send_keys("")
        browser.find_element_by_id("patientMessage").clear()
        browser.find_element_by_id("patientMessage").send_keys(u"董焕焕")
        browser.find_element_by_css_selector("button.searchBtn").click()
        time.sleep(1)
        browser.find_element_by_id("patientMessage").clear()
        browser.find_element_by_id("patientMessage").send_keys("")
        Select(browser.find_element_by_css_selector("select.form-control.PatientType")).select_by_visible_text(u"自费")
        time.sleep(1)
        Select(browser.find_element_by_css_selector("select.form-control.PatientType")).select_by_visible_text(u"保险")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div/div[1]/div/span').click()  #点击导出Excel
        time.sleep(2)









if __name__ == '__main__':
    unittest.main()