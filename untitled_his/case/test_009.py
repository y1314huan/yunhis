# coding:utf-8
#为模板管理脚本
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from commonshare.His import Browser
import unittest
import time
from selenium.webdriver.support.ui import Select
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
        browser.get("http://yun.oasisapp.cn:9080/uc/authentication/check?login=true&phone=&redirectUrl=http://yun.oasisapp.cn:8080/yunhis/security_check.action")
        ## 测试地址

        # browser.get("http://47.93.156.153:9090/uc/authentication/check?login=true&phone=&redirectUrl=http://47.93.156.153:8090/yunhis/security_check.action")
        # # 准正式地址

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

    #模板管理
    def test_Template(self):
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/div[3]/aside/section/ul/li[13]/a').click()  # 点击模板管理
        # 处方模板
        browser.find_element_by_link_text(u"处方模板").click()  # 点击处方模板
        time.sleep(2)
        browser.find_element_by_id("remove_cf_btn").click()  # 点击删除
        time.sleep(2)
        browser.current_window_handle
        time.sleep(2)
        browser.find_element_by_css_selector("button.sure_ok_1").click()  # 点击确定
        time.sleep(1)
        browser.find_element_by_id("newly_temp_cf").click()  # 点击新建处方模板
        time.sleep(1)
        browser.find_element_by_css_selector("input.temp_name_info").clear()  # 清除模板名称输入框
        time.sleep(1)
        browser.find_element_by_css_selector("input.temp_name_info").send_keys(u"新建处方模板")  # 输入新建模板名称
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="cf_temp_tbody_list"]/tr/td[2]/input').send_keys(u"阿莫西林胶囊")  # 输入阿莫西林胶囊
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="170712201200147"]').click()  # 选择阿莫西林胶囊
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="cf_temp_tbody_list"]/tr/td[3]/select').click()  # 点击用法
        time.sleep(1)
        InputType = Select(browser.find_element_by_xpath('//*[@id="cf_temp_tbody_list"]/tr/td[3]/select'))  # 选择用法
        InputType.select_by_value("10")  # 选择用法“冲服”
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="frequency_drug"]').click()  # 点击用药频次
        time.sleep(1)
        InputType = Select(browser.find_element_by_xpath('//*[@id="frequency_drug"]'))  # 选择用药频次
        InputType.select_by_value("100000000002")  # 选择用法“每天三次”
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="cf_temp_tbody_list"]/tr/td[5]/input').clear()
        browser.find_element_by_xpath('//*[@id="cf_temp_tbody_list"]/tr/td[5]/input').send_keys(5)  # 输入单次计量
        time.sleep(1)
        browser.find_element_by_css_selector("#cf_temp_tbody_list > tr > td:nth-child(6) > input").clear()
        browser.find_element_by_css_selector("#cf_temp_tbody_list > tr > td:nth-child(6) > input").send_keys(4)  # 输入天数
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="cf_temp_tbody_list"]/tr/td[7]/input').clear()  #
        browser.find_element_by_xpath('//*[@id="cf_temp_tbody_list"]/tr/td[7]/input').send_keys("2")  # 输入开药量
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="add_drug_trs"]').click()  # 点击添加药品
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="cf_temp_tbody_list"]/tr[2]/td[2]/input').send_keys(u"达克宁")  # 输入达克宁
        time.sleep(5)
        browser.find_element_by_xpath('//*[@id="100000000000711"]').click()  # 选择达克宁
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="cf_temp_tbody_list"]/tr[2]/td[6]/input').send_keys(3)  # 输入天数
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="cf_keep_btn_1"]').click()  # 点击保存
        time.sleep(2)
        browser.find_element_by_id("remove_cf_btn").click()  # 点击删除
        time.sleep(2)
        browser.current_window_handle
        time.sleep(2)
        browser.find_element_by_css_selector("button.sure_ok_1").click()  # 点击确定
        time.sleep(1)

        # 中药处方模板
        browser.find_element_by_link_text(u"中草药处方模板").click()  # 点击中药处方模板
        time.sleep(1)
        browser.find_element_by_id("remove_btn").click()  # 点击删除
        time.sleep(2)
        browser.current_window_handle
        time.sleep(2)
        browser.find_element_by_css_selector("button.sure_ok_1").click()  # 点击确认
        time.sleep(1)

        browser.find_element_by_id("newly_temp_zy").click()  # 点击新增 中药处方模板
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="zyForm"]/div/div[1]/span/input').send_keys(u"新增草药处方模板")  # 输入中药 处方模板名称
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="MedicineBody"]/tr/td[1]/input').send_keys(u"红花")  # 输入红花
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="medicine_tbody_info"]/tr[1]/td[1]').click()  # 选择红花
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="MedicineBody"]/tr/td[2]/input').clear()  #
        browser.find_element_by_xpath('//*[@id="MedicineBody"]/tr/td[2]/input').send_keys(u"20")  # 红花20g
        browser.find_element_by_xpath('//*[@id="usagelist"]').click()
        time.sleep(2)
        InputType = Select(browser.find_element_by_xpath('//*[@id="usagelist"]'))  # 选择用法
        InputType.select_by_value("8")  # 选择用法“泡服”
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="AddMedicineBtn"]').click()  # 点击添加药品
        time.sleep(1)
        browser.find_element_by_xpath("(//input[@type='text'])[8]").send_keys(u"土白芍")
        browser.find_element_by_xpath("(//input[@type='text'])[9]").send_keys("20")
        time.sleep(3)
        browser.find_element_by_xpath("(//tbody[@id='medicine_tbody_info']/tr/td)[7]").click()
        time.sleep(2)
        browser.find_element_by_css_selector("input.numM").send_keys("7")  # 输入剂数
        time.sleep(2)
        target = browser.find_element_by_xpath('//*[@id="keep_btn_1"]')  # 滑动到代收付页面最底部
        browser.execute_script("arguments[0].scrollIntoView();", target)  # 滑动到代收付页面最底部
        time.sleep(2)
        browser.find_element_by_css_selector("textarea.textremark").send_keys(u"饭后服用")  # 填写备注
        time.sleep(2)
        browser.find_element_by_id("keep_btn_1").click()  # 点击保存
        time.sleep(2)
        browser.find_element_by_id("remove_btn").click()  # 点击删除
        time.sleep(2)
        browser.current_window_handle
        time.sleep(2)
        browser.find_element_by_css_selector("button.sure_ok_1").click()  # 点击确认
        time.sleep(1)


        #病例模板
        browser.find_element_by_xpath('//*[@id="clinic_templet"]/ul/li[1]/a').click()
        time.sleep(2)
        browser.find_element_by_css_selector("i.btn.delete_temp").click()  # 点击病例末班删除
        time.sleep(3)
        browser.current_window_handle
        time.sleep(3)
        browser.find_element_by_css_selector("button.sure_ok").click()  # 点击确定
        time.sleep(3)
        browser.refresh()
        time.sleep(3)
        browser.find_element_by_xpath('//*[@id="newly_temp"]').click()  # 点击新建病例模板
        time.sleep(3)
        browser.find_element_by_xpath('//*[@id="templet_form1"]/ul/li[1]/span').send_keys(u"病例模板")  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="templet_form1"]/ul/li[2]/span').send_keys(u"主诉：感冒、发烧、头疼")  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="templet_form1"]/ul/li[3]/span').send_keys(u"现病史：高血压")  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="templet_form1"]/ul/li[4]/span').send_keys(u"既往史：糖尿病")  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="templet_form1"]/ul/li[5]/span').send_keys(u"个人史:高血压、糖尿病")  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="templet_form1"]/ul/li[6]/span').send_keys(u"过敏史：花粉过敏")  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="templet_form1"]/ul/li[7]/span').send_keys(u"家族史：高血压")  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="advice_Btn_s1"]').click()  # 点击保存
        time.sleep(2)
        browser.find_element_by_css_selector("i.btn.delete_temp").click()  # 点击病例末班删除
        time.sleep(3)
        browser.current_window_handle
        time.sleep(3)
        browser.find_element_by_css_selector("button.sure_ok").click()  # 点击确定
        time.sleep(1)

        # 处理意见模板
        browser.find_element_by_link_text(u"处理意见模板").click()  # 点击处理意见
        time.sleep(1)
        browser.find_element_by_link_text(u"删除").click()  # 点击删除
        time.sleep(2)
        browser.current_window_handle
        time.sleep(2)
        browser.find_element_by_css_selector("button.sure_ok_1").click()  # 点击确定
        time.sleep(1)
        browser.find_element_by_id("templet_btn").click()  # 点击新建处理意见
        time.sleep(2)
        browser.current_window_handle
        time.sleep(2)
        browser.find_element_by_css_selector("li > input[type=\"text\"]").clear()  # 清除处理意见名称
        browser.find_element_by_css_selector("li > input[type=\"text\"]").send_keys(u"处理意见模板")  # 输入处理意见名称
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="layui-layer5"]/div[2]/div/ul/li[2]/input').send_keys(u"好好休息")  # 输入处理意见内容
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="btn_tip"]/button').click()  # 点击保存
        time.sleep(2)
        browser.find_element_by_link_text(u"删除").click()  # 点击删除
        time.sleep(2)
        browser.current_window_handle
        time.sleep(2)
        browser.find_element_by_css_selector("button.sure_ok_1").click()  # 点击确定
        time.sleep(1)









if __name__ == '__main__':
    unittest.main()