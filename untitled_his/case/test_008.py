# coding:utf-8
#收费项目设置——查看账号管理列表，查看诊所信息、添加及修改检验项目、添加及修改
#检查项目、添加及修改治疗项目、添加及修改其他项目、添加及修改诊费管理、字典

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from commonshare.His import Browser
import unittest
import time
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        ## 测试地址


        browser.get("http://47.93.156.153:9090/uc/authentication/check?login=true&phone=&redirectUrl=http://47.93.156.153:8090/yunhis/security_check.action")
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
        browser.find_element_by_xpath(".//*[@id='#clinics']/li[2]").click()  # 选择泓华金融街诊所测试和准正式
        # browser.find_element_by_xpath('//*[@id="#clinics"]/li[1]').click()#正式环境云his测试诊所
        time.sleep(5)
        print ("登录成功")


#系统设置
    def test002(self):
        time.sleep(2)
        target = browser.find_element_by_xpath('/html/body/div[3]/aside/section/ul/li[17]/a/span[1]')  # 滑动到个人信息
        browser.execute_script("arguments[0].scrollIntoView();", target)  # 滑动到个人信息
        time.sleep(4)
        browser.find_element_by_xpath('/html/body/div[3]/aside/section/ul/li[14]/a/span[1]').click()#点击系统管理
        time.sleep(3)
        browser.find_element_by_css_selector("body > div.wrapper > aside > section > ul > li.treeview.active > ul > li:nth-child(1) > a").click() #点击诊所管理
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="clinic_info"]/a').click()  #点击诊所信息
        time.sleep(2)

# 添加检验项目
        browser.find_element_by_xpath('/html/body/div[3]/aside/section/ul/li[14]/ul/li[4]/a').click()  # 点击收费项目设置
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="collect_fees"]/ul/li[1]/a').click()  # 点击检验项目
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="checkout_btn"]').click()  # 点击添加检验项目
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="examine_item_name"]').send_keys(u"新增检验项目")  # 输入新增检验项目名称
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="examine_unit"]').send_keys(u"人次")  #输入单位人次
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="prices"]').send_keys(u"1000.99")#填写零售价
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="form_test"]/ul/li[4]/input').send_keys(u"500.55")#填写成本
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="form_test"]/ul/li[5]/select').click()#点击标本种类
        time.sleep(1)
        InputType = Select(browser.find_element_by_xpath('//*[@id="form_test"]/ul/li[5]/select'))
        InputType.select_by_value("组织")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="form_test"]/ul/li[6]/select').click()#选择试管颜色
        InputType = Select(browser.find_element_by_xpath('//*[@id="form_test"]/ul/li[6]/select'))
        InputType.select_by_value("黄色")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="form_test"]/ul/li[7]/input').send_keys(now)  # 输入报告时间
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="clinic_select"]').click()  #点击检验地点
        time.sleep(1)
        InputType = Select(browser.find_element_by_xpath('//*[@id="clinic_select"]'))#选择外送
        InputType.select_by_value("1")
        time.sleep(1)
        target = browser.find_element_by_xpath('//*[@id="form_test"]/ul/li[14]/input')  # 滑动到临床信息
        browser.execute_script("arguments[0].scrollIntoView();", target)  # 滑动到临床信息
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="form_test"]/ul/li[9]/input').send_keys(u"未标记")  #填写合并标记
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="form_test"]/ul/li[10]/select').click()  #点击是否允许折扣
        time.sleep(1)
        InputType = Select(browser.find_element_by_xpath('//*[@id="form_test"]/ul/li[10]/select'))  # 是否允许折扣选择否
        InputType.select_by_value("0")
        browser.find_element_by_xpath('//*[@id="form_test"]/ul/li[11]/input').send_keys(u"国际编码CC8298184093")  #输入国际编码
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="form_test"]/ul/li[12]/input[2]').click()  # 状态选择禁用
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="form_test"]/ul/li[13]/input').send_keys(u"输入备注")  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="form_test"]/ul/li[14]/input').send_keys(u"输入临床意义")  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="examine_btn_add"]').click()  #点击保存
        time.sleep(2)

#修改检验项目
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, "modify_btn")))  #
        ys.click()  #点击修改
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="examine_item_name_1"]').clear()  # 点击诊所管理
        browser.find_element_by_xpath('//*[@id="examine_item_name_1"]').send_keys(u"修改检验项目名称")  # 修改检验项目名称
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="examine_unit_1"]').clear()  # 点击诊所管理
        browser.find_element_by_xpath('//*[@id="examine_unit_1"]').send_keys(u"修改单位") #修改单位
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="jy_price"]').clear()
        browser.find_element_by_xpath('//*[@id="jy_price"]').send_keys(u"2000.99")  # 修改零售价
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="form_test_1"]/ul/li[5]/input').clear()  #修改成本价
        browser.find_element_by_xpath('//*[@id="form_test_1"]/ul/li[5]/input').send_keys(u"1000.99")  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="specimen_y"]').click()  #点击、修改标本种类
        InputType = Select(browser.find_element_by_xpath('//*[@id="specimen_y"]'))
        InputType.select_by_value("血浆（专用抗凝）")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="color_y"]').click()  #点击试管颜色
        InputType = Select(browser.find_element_by_xpath('//*[@id="color_y"]'))
        InputType.select_by_value("蓝色")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="triptime_y"]').clear()
        browser.find_element_by_xpath('//*[@id="triptime_y"]').send_keys(tom)  #修改报告时间
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="clinic_select_1"]').click()  #点击检验地点
        InputType = Select(browser.find_element_by_xpath('//*[@id="clinic_select_1"]'))#检验地点修改为诊所
        InputType.select_by_value("0")
        time.sleep(1)
        target = browser.find_element_by_xpath('//*[@id="mean_y"]')  # 滑动到临床意义
        browser.execute_script("arguments[0].scrollIntoView();", target)  # 滑动到临床意义
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="groups_y"]').clear()
        browser.find_element_by_xpath('//*[@id="groups_y"]').send_keys(u"修改合并标记")  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="isdiscount_y"]').click()  #点击是否允许折扣
        time.sleep(1)
        InputType = Select(browser.find_element_by_xpath('//*[@id="isdiscount_y"]'))  # 是否允许折扣选择是
        InputType.select_by_value("1")
        browser.find_element_by_xpath('//*[@id="radio_z"]').click()  # 状态选择正常
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="code_y"]').clear()
        browser.find_element_by_xpath('//*[@id="code_y"]').send_keys(u"修改国际编码")# 修改国际编码
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="comment_y"]').send_keys(u"修改备注")  # 修改备注
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="mean_y"]').clear()
        browser.find_element_by_xpath('//*[@id="mean_y"]').send_keys(u"修改临床意义")  # 修改临床意义
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="examine_btn_add_1"]').click()  # 点击保存
        time.sleep(2)
        browser.refresh()
        time.sleep(3)
        browser.find_element_by_xpath('//*[@id="chargingItem_leadingOut"]').click()  #点击导出Excel
        time.sleep(2)




#添加检查项目
        browser.find_element_by_xpath('//*[@id="collect_fees"]/ul/li[2]/a').click()  # #点击检查项目
        time.sleep(2)
        browser.refresh()
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="checkout_btn"]').click()  #点击添加检验项目
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="select2-inspect_item_change-container"]/span').click()   #点击检查类型
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u"CT")  # 选择检查类型
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="select2-inspect_position-container"]/span').click()  #点击部位
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u"头部")  #
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="inspect_item_name"]').send_keys(u"新增检查项目")  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="unit_id"]').send_keys(u"新增单位")  #
        time.sleep(2)
        browser.find_element_by_css_selector("#nowprice_id").send_keys(u"2000.99")  #
        time.sleep(1)
        target = browser.find_element_by_xpath('//*[@id="inspect_form"]/ul/li[6]/span/textarea')  # 滑动到备注
        browser.execute_script("arguments[0].scrollIntoView();", target)  # 滑动到备注
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="inspect_form"]/ul/li[4]/span[2]/input').send_keys(u"输入国际编码12421DD")  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="inspect_form"]/ul/li[5]/span[1]/input').send_keys(u"500.99")  #输入成本价
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="inspect_form"]/ul/li[5]/span[2]/select').click()  #点击是否允许折扣
        time.sleep(1)
        InputType = Select(browser.find_element_by_xpath('//*[@id="inspect_form"]/ul/li[5]/span[2]/select'))  # 是否允许折扣选择否
        InputType.select_by_value("0")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="inspect_form"]/ul/li[6]/span/textarea').send_keys(u"新增备注")  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="inspect_form"]/ul/li[7]/span/input[2]').click()  #状态选择禁用
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="inspect_data_btn"]').click()  #点击保存
        time.sleep(2)
        #修改检查项目
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, "inspect_modify_btn")))  #
        ys.click()  # 点击修改
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="select2-inspect_item_change_1-container"]').click()  ##点击检查类型
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u"超声")  #输入检查类型
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="select2-inspect_position_1-container"]').click()   #点击部位
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u"腹部")  # 点击诊所管理
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="inspect_item_name_1"]').clear()
        browser.find_element_by_xpath('//*[@id="inspect_item_name_1"]').send_keys(u"修改检验项目")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="unit_id_1"]').clear()  #
        browser.find_element_by_xpath('//*[@id="unit_id_1"]').send_keys(u"修改单位 ")
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="nowprice_id_1"]').clear()  #修改零售价
        browser.find_element_by_xpath('//*[@id="nowprice_id_1"]').send_keys(u"2000.77 ")
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="code_c"]').clear()  # 修改国际编码
        browser.find_element_by_xpath('//*[@id="code_c"]').send_keys(u"修改国际编码")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="costprice_c"]').clear()  # 修改成本价
        browser.find_element_by_xpath('//*[@id="costprice_c"]').send_keys(u"1000.99")
        time.sleep(1)
        target = browser.find_element_by_xpath('//*[@id="comment_c"]')  # 滑动到备注
        browser.execute_script("arguments[0].scrollIntoView();", target)  # 滑动到备注
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="isdiscount_c"]').click()  # 点击是否允许折扣
        time.sleep(1)
        InputType = Select(browser.find_element_by_xpath('//*[@id="isdiscount_c"]'))  # 是否允许折扣选择是
        InputType.select_by_value("1")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="comment_c"]').send_keys(u"修改备注")  # 修改备注
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="c_radio"]').click()  # 状态选择正常
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="inspect_data_btn_1"]').click()  # 点击保存
        time.sleep(2)
        browser.refresh()
        time.sleep(3)
        browser.find_element_by_xpath('//*[@id="chargingItem_leadingOut"]').click()  #导出Excel
        time.sleep(2)





#添加治疗项目
        browser.find_element_by_xpath('//*[@id="collect_fees"]/ul/li[3]/a').click()  # 点击治疗项目
        time.sleep(1)
        browser.find_element_by_id("treatmentSystermSet_btn").click()  # 点击新增治疗项目
        time.sleep(1)
        browser.find_element_by_id("examine_item_name").clear()  #
        browser.find_element_by_id("examine_item_name").send_keys(u"新增治疗项目")  # 输入治疗项目名称
        time.sleep(1)

        browser.find_element_by_id("examine_unit").clear()  #
        browser.find_element_by_id("examine_unit").send_keys(u"新增单位")  # 输入单位
        browser.find_element_by_id("prices").clear()  #
        browser.find_element_by_id("prices").send_keys("1000.9")  # 输入售价
        browser.find_element_by_id("costPrice").clear()  #
        browser.find_element_by_id("costPrice").send_keys("500.99")  # 输入成本价
        Select(browser.find_element_by_id("isdiscount")).select_by_visible_text(u"否")  # 是否允许折扣选择否
        time.sleep(1)
        Select(browser.find_element_by_id("ZL_item_1")).select_by_visible_text(u"理疗费")  # 分类选择理疗费
        time.sleep(1)
        browser.find_element_by_id("itN").click()  # 状态选择禁用
        browser.find_element_by_id("treatmentDes").clear()  #
        browser.find_element_by_id("treatmentDes").send_keys(u"新增备注")  # 输入备注信息
        browser.find_element_by_id("examine_btn_add").click()  # 点击保存
        time.sleep(5)
        browser.find_element_by_css_selector("#examine_item_body > tr:nth-child(2) > td:nth-child(7) > span.modify_btn").click()  # 点击修改
        browser.find_element_by_id("examine_item_name").clear()  # 清除输入框
        browser.find_element_by_id("examine_item_name").send_keys(u"修改治疗项")  # 修改治疗项

        browser.find_element_by_id("examine_unit").clear()  # 清除输入框
        browser.find_element_by_id("examine_unit").send_keys(u"修改单位")  # 修改单位
        browser.find_element_by_id("prices").clear()  # 清除输入框
        browser.find_element_by_id("prices").send_keys("2000.9")  # 输入售价
        browser.find_element_by_id("costPrice").clear()  # 清除输入框
        browser.find_element_by_id("costPrice").send_keys("1000.9")  # 输入成本价
        time.sleep(1)
        Select(browser.find_element_by_id("isdiscount")).select_by_visible_text(u"是")  # 是否允许折扣选择是
        Select(browser.find_element_by_id("ZL_item_1")).select_by_visible_text(u"普通治疗费")  # 类型选择检验费
        time.sleep(1)
        browser.find_element_by_id("itY").click()  # 选择正常
        browser.find_element_by_id("treatmentDes").clear()  # 清除输入框
        browser.find_element_by_id("treatmentDes").send_keys(u"修改备注")  # 修改备注
        browser.find_element_by_id("examine_btn_add1").click()  # 点击保存
        time.sleep(2)
        browser.refresh()
        time.sleep(3)
        browser.find_element_by_xpath('//*[@id="chargingItem_leadingOut"]').click()  #导出Excel
        time.sleep(2)



# 添加其他项目
        browser.find_element_by_link_text(u"其他项目").click()  # 点击其他项目
        time.sleep(2)
        browser.find_element_by_id("treatment_btn").click()  # 点击添加其他项目
        browser.find_element_by_id("item_name").clear()  #
        browser.find_element_by_id("item_name").send_keys(u"新增其他收费项目")  # 输入新增项目名称
        browser.find_element_by_id("unit_ids").clear()  #
        browser.find_element_by_id("unit_ids").send_keys(u"新增单位")  # 输入新增单位
        browser.find_element_by_id("nowprice_ids").clear()  #
        browser.find_element_by_id("nowprice_ids").send_keys("1000.99")  # 输入单价
        browser.find_element_by_xpath("(//input[@name='status'])[2]").click()  # 选择禁用
        browser.find_element_by_name("comment").clear()  #
        browser.find_element_by_name("comment").send_keys(u"新增备注")  # 输入备注信息
        browser.find_element_by_id("charging_item_btn").click()  # 点击保存
        time.sleep(5)
        browser.find_element_by_class_name("ZL-amend").click()  # 点击修改
        browser.find_element_by_id("item_name_1").clear()  #
        browser.find_element_by_id("item_name_1").send_keys(u"修改其他项目")  # 修改项目名称
        browser.find_element_by_id("unit_ids_1").clear()  #
        browser.find_element_by_id("unit_ids_1").send_keys(u"修改单位")  # 修改单位
        browser.find_element_by_id("nowprice_ids_1").clear()  #
        browser.find_element_by_id("nowprice_ids_1").send_keys("2000.99")  # 修改单价
        browser.find_element_by_id("radio_status").click()  # 点击正常
        browser.find_element_by_id("comment_l").clear()  #
        browser.find_element_by_id("comment_l").send_keys(u"修改备注")  # 修改备注
        browser.find_element_by_id("charging_item_btn_1").click()  # 点击保存
        time.sleep(2)
        browser.refresh()
        time.sleep(3)
        browser.find_element_by_xpath('//*[@id="chargingItem_leadingOut"]').click()  # 导出Excel
        time.sleep(2)


# 添加诊费
        browser.find_element_by_link_text(u"诊费管理").click()  # 点击诊费管理
        time.sleep(2)
        browser.find_element_by_id("examine_fees_btn").click()  # 点击新增诊费
        browser.find_element_by_id("itemName").clear()  #
        browser.find_element_by_id("itemName").send_keys(u"新增诊费")  # 输入诊费名称
        browser.find_element_by_id("itemUnit").clear()  #
        browser.find_element_by_id("itemUnit").send_keys(u"人次")  # 输入单位
        browser.find_element_by_id("itemPrice").clear()  #
        browser.find_element_by_id("itemPrice").send_keys("1000")  # 输入单价
        browser.find_element_by_id("isdefault_checkboxs").click()  # 点击默诊费
        browser.find_element_by_xpath("(//input[@name='status'])[2]").click()  # 点击禁用
        browser.find_element_by_id("examine_fee_btn").click()  # 点击保存
        time.sleep(5)
        browser.find_element_by_class_name("fee_alter_btn").click()  # 点击修改
        browser.find_element_by_id("itemName_1").clear()  #
        browser.find_element_by_id("itemName_1").send_keys(u"修改诊费")  # 修改名称
        browser.find_element_by_id("itemUnit_1").clear()  #
        browser.find_element_by_id("itemUnit_1").send_keys(u"修改单位")  # 修改单位
        browser.find_element_by_id("itemPrice_1").clear()  #
        browser.find_element_by_id("itemPrice_1").send_keys("555")  # 修改单价
        browser.find_element_by_id("isdefault_checkbox").click()  # 默认诊费勾选去掉
        browser.find_element_by_id("fee_radio").click()  # 状态选择正常
        browser.find_element_by_id("examine_fee_btn_1").click()  # 点击保存
        time.sleep(2)
        browser.refresh()
        time.sleep(3)
        browser.find_element_by_xpath('//*[@id="chargingItem_leadingOut"]').click()  # 导出Excel
        time.sleep(2)


# 字典、
# 添加费别字典
        time.sleep(2)
        target = browser.find_element_by_xpath('/html/body/div[3]/aside/section/ul/li[17]')  #
        browser.execute_script("arguments[0].scrollIntoView();", target)  #
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/div[3]/aside/section/ul/li[14]').click()  #点击系统管理
        time.sleep(1)
        browser.find_element_by_css_selector("body > div.wrapper > aside > section > ul > li.treeview.active > ul > li:nth-child(5) > a").click()  #点击字典
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="feibie"]/a').click()  # 点击费别字典
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="adds_diction"]/button[1]').click()  #点击添加费别
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="Medical_name"]').send_keys(u"新增费别")  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="form_3"]/ul/li[2]/input').send_keys(u"新增备注")  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="form_3"]/ul/li[3]/input[2]').click()  #点击禁用
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="_one_item_typeid"]/p[1]/select').click()
        time.sleep(1)
        InputType = Select(browser.find_element_by_xpath('//*[@id="_one_item_typeid"]/p[1]/select'))  # 选择西药
        InputType.select_by_value("1")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="_one_item_typeid"]/p[2]/input').send_keys(u"99.99")#折扣比例输入99.99%
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="add_item_one"]').click()  #点击新增
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="item_listInfos"]/div[2]/p[1]/select').click()  #点击项目类型
        time.sleep(1)
        InputType = Select(browser.find_element_by_xpath('//*[@id="item_listInfos"]/div[2]/p[1]/select'))  # 选择中草药
        InputType.select_by_value("2")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="item_listInfos"]/div[2]/p[2]/input').send_keys(u"88.88")#折扣比例输入88.88%
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="add_item_one"]').click()  #点击新增
        time.sleep(1)
        target = browser.find_element_by_xpath('//*[@id="btn_cun_one"]')  # 滑动到保存
        browser.execute_script("arguments[0].scrollIntoView();", target)  # 滑动到保存
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="item_listInfos"]/div[3]/p[1]/select').click()  #点击项目类型
        time.sleep(1)
        InputType = Select(browser.find_element_by_xpath('//*[@id="item_listInfos"]/div[3]/p[1]/select'))  # 选择中草药
        InputType.select_by_value("3")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="item_listInfos"]/div[3]/p[2]/input').send_keys(u"77.77")  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="add_item_one"]').click()  #点击新增
        time.sleep(1)
        target = browser.find_element_by_xpath('//*[@id="btn_cun_one"]')  # 滑动到保存
        browser.execute_script("arguments[0].scrollIntoView();", target)  # 滑动到保存
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="item_listInfos"]/div[4]/p[1]/select').click()  #点击项目类型
        time.sleep(1)
        InputType = Select(browser.find_element_by_xpath('//*[@id="item_listInfos"]/div[4]/p[1]/select'))  # 选择耗材
        InputType.select_by_value("999")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="item_listInfos"]/div[4]/p[2]/input').send_keys(u"66.66")  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="add_item_one"]').click()  #点击新增
        time.sleep(1)
        target = browser.find_element_by_xpath('//*[@id="btn_cun_one"]')  # 滑动到保存
        browser.execute_script("arguments[0].scrollIntoView();", target)  # 滑动到保存
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="item_listInfos"]/div[5]/p[1]/select').click()  #点击项目类型
        time.sleep(1)
        InputType = Select(browser.find_element_by_xpath('//*[@id="item_listInfos"]/div[5]/p[1]/select'))  # 选择检验
        InputType.select_by_value("4")
        browser.find_element_by_xpath('//*[@id="item_listInfos"]/div[5]/p[2]/input').send_keys(u"55.55")  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="add_item_one"]').click()  #点击新增
        time.sleep(1)
        target = browser.find_element_by_xpath('//*[@id="btn_cun_one"]')  # 滑动到保存
        browser.execute_script("arguments[0].scrollIntoView();", target)  # 滑动到保存
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="item_listInfos"]/div[6]/p[1]/select').click()  #点击项目类型
        time.sleep(1)
        InputType = Select(browser.find_element_by_xpath('//*[@id="item_listInfos"]/div[6]/p[1]/select'))  # 选择检查
        InputType.select_by_value("5")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="item_listInfos"]/div[6]/p[2]/input').send_keys(u"44.44")  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="add_item_one"]').click()  #点击新增
        time.sleep(1)
        target = browser.find_element_by_xpath('//*[@id="btn_cun_one"]')  # 滑动到保存
        browser.execute_script("arguments[0].scrollIntoView();", target)  # 滑动到保存
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="item_listInfos"]/div[7]/p[1]/select').click()  #点击项目类型
        time.sleep(1)
        InputType = Select(browser.find_element_by_xpath('//*[@id="item_listInfos"]/div[7]/p[1]/select'))  # 选择其他项目
        InputType.select_by_value("6")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="item_listInfos"]/div[7]/p[2]/input').send_keys(u"33.33")  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="add_item_one"]').click()  #点击新增
        time.sleep(1)
        target = browser.find_element_by_xpath('//*[@id="btn_cun_one"]') # 滑动到保存
        browser.execute_script("arguments[0].scrollIntoView();", target)  # 滑动到保存
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="item_listInfos"]/div[8]/p[1]/select').click()  #点击项目类型
        time.sleep(1)
        InputType = Select(browser.find_element_by_xpath('//*[@id="item_listInfos"]/div[8]/p[1]/select'))  # 选择诊费
        InputType.select_by_value("7")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="item_listInfos"]/div[8]/p[2]/input').send_keys(u"22.22")  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="add_item_one"]').click()  #点击新增
        time.sleep(1)
        target = browser.find_element_by_xpath('//*[@id="btn_cun_one"]')  # 滑动到保存
        browser.execute_script("arguments[0].scrollIntoView();", target)  # 滑动到保存
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="item_listInfos"]/div[9]/p[1]/select').click()  #点击项目类型
        time.sleep(1)
        InputType = Select(browser.find_element_by_xpath('//*[@id="item_listInfos"]/div[9]/p[1]/select'))  # 选择治疗项目
        InputType.select_by_value("10")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="item_listInfos"]/div[9]/p[2]/input').send_keys(u"11.11")  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="btn_cun_one"]').click()  #点击保存
        time.sleep(5)


#修改费别字典
        browser.refresh()
        time.sleep(2)
        browser.find_element_by_class_name('amend_FB').click()  #点击修改
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="Medical_name_1"]').clear()  #
        browser.find_element_by_xpath('//*[@id="Medical_name_1"]').send_keys(u"修改费别")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="form_4"]/ul/li[2]/input').clear()  #
        browser.find_element_by_xpath('//*[@id="form_4"]/ul/li[2]/input').send_keys(u"修改备注")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="form_4"]/ul/li[3]/input[1]').click()  #状态选择正常
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="item_listInfos_1"]/div[1]/p[1]/select').click()  #点击项目类型
        InputType = Select(browser.find_element_by_xpath('//*[@id="item_listInfos_1"]/div[1]/p[1]/select'))  # 选择治疗项目
        InputType.select_by_value("10")#选择其他项目
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="item_listInfos_1"]/div[1]/p[2]/input').clear() #
        browser.find_element_by_xpath('//*[@id="item_listInfos_1"]/div[1]/p[2]/input').send_keys(u"11.11")  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="item_listInfos_1"]/div[2]/p[1]/select').click()  #
        InputType = Select(browser.find_element_by_xpath('//*[@id="item_listInfos_1"]/div[2]/p[1]/select'))  #
        InputType.select_by_value("7")#选择诊费
        browser.find_element_by_xpath('//*[@id="item_listInfos_1"]/div[2]/p[2]/input').clear()  #
        browser.find_element_by_xpath('//*[@id="item_listInfos_1"]/div[2]/p[2]/input').send_keys(u"22.22")  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="item_listInfos_1"]/div[3]/p[1]/select').click()  #
        InputType = Select(browser.find_element_by_xpath('//*[@id="item_listInfos_1"]/div[3]/p[1]/select'))  #选择其他治疗项目
        InputType.select_by_value("6") #选择其他治疗项目
        browser.find_element_by_xpath('//*[@id="item_listInfos_1"]/div[3]/p[2]/input').clear()  #
        browser.find_element_by_xpath('//*[@id="item_listInfos_1"]/div[3]/p[2]/input').send_keys(u"33.33")
        time.sleep(1)
        target = browser.find_element_by_xpath('//*[@id="item_listInfos_1"]/div[5]/p[2]/input')  # 滑动到耗材折扣输入
        browser.execute_script("arguments[0].scrollIntoView();", target)  # 滑动到耗材折扣输入
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="item_listInfos_1"]/div[4]/p[1]/select').click()
        InputType = Select(browser.find_element_by_xpath('//*[@id="item_listInfos_1"]/div[4]/p[1]/select'))  # 选择其他治疗项目
        InputType.select_by_value("5")  # 选择检查
        browser.find_element_by_xpath('//*[@id="item_listInfos_1"]/div[4]/p[2]/input').clear()  #
        browser.find_element_by_xpath('//*[@id="item_listInfos_1"]/div[4]/p[2]/input').send_keys(u"44.44")  #
        time.sleep(1)
        target = browser.find_element_by_xpath('//*[@id="btn_cun_one_1"]')  # 滑动到保存
        browser.execute_script("arguments[0].scrollIntoView();", target)  # 滑动到保存
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="item_listInfos_1"]/div[6]/p[1]/select').click()  #
        InputType = Select(browser.find_element_by_xpath('//*[@id="item_listInfos_1"]/div[6]/p[1]/select'))  #
        InputType.select_by_value("4")#选择检验
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="item_listInfos_1"]/div[5]/p[2]/input').clear()  #
        browser.find_element_by_xpath('//*[@id="item_listInfos_1"]/div[5]/p[2]/input').send_keys(u"55.55")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="item_listInfos_1"]/div[6]/p[1]/select').click()  #
        InputType = Select(browser.find_element_by_xpath('//*[@id="item_listInfos_1"]/div[6]/p[1]/select'))  #
        InputType.select_by_value("999")  # 选择耗材
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="item_listInfos_1"]/div[6]/p[2]/input').clear()  #
        browser.find_element_by_xpath('//*[@id="item_listInfos_1"]/div[6]/p[2]/input').send_keys(u"66.66")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="item_listInfos_1"]/div[7]/p[1]/select').click()  #
        InputType = Select(browser.find_element_by_xpath('//*[@id="item_listInfos_1"]/div[7]/p[1]/select'))  #
        InputType.select_by_value("3")  # 选择中草药
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="item_listInfos_1"]/div[7]/p[2]/input').clear()  #
        browser.find_element_by_xpath('//*[@id="item_listInfos_1"]/div[7]/p[2]/input').send_keys(u"77.77")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="item_listInfos_1"]/div[8]/p[1]/select').click()  #
        InputType = Select(browser.find_element_by_xpath('//*[@id="item_listInfos_1"]/div[8]/p[1]/select'))  #
        InputType.select_by_value("2")  # 选择中成药
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="item_listInfos_1"]/div[8]/p[2]/input').clear()  #
        browser.find_element_by_xpath('//*[@id="item_listInfos_1"]/div[8]/p[2]/input').send_keys(u"88.88")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="item_listInfos_1"]/div[9]/p[1]/select').click()  #
        InputType = Select(browser.find_element_by_xpath('//*[@id="item_listInfos_1"]/div[9]/p[1]/select'))  #
        InputType.select_by_value("1")  # 选择西药
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="item_listInfos_1"]/div[9]/p[2]/input').clear()  #
        browser.find_element_by_xpath('//*[@id="item_listInfos_1"]/div[9]/p[2]/input').send_keys(u"99.99")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="btn_cun_one_1"]').click()  #点击保存
        time.sleep(5)
        browser.refresh()
        time.sleep(3)
        browser.find_element_by_xpath('//*[@id="tr_0"]/td[3]/span[2]').click()  #点击设置折扣
        time.sleep(10)
        browser.find_element_by_xpath('//*[@id="select2-search_select-container"]').click()  #点击搜索框
        time.sleep(3)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u"硫酸庆大霉素注射液")  #
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="dis_tbody"]/tr[1]/td[2]/input').clear()  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="dis_tbody"]/tr[1]/td[2]/input').send_keys(u"80")  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="discount_btn"]').click()  #点击保存
        time.sleep(5)
        browser.refresh()
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="tr_0"]/td[3]/span[1]').click()  #点击修改
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="item_listInfos_1"]/div[1]/p[2]/input').clear()  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="item_listInfos_1"]/div[1]/p[2]/input').send_keys(u"90")  #
        time.sleep(1)
        target = browser.find_element_by_xpath('//*[@id="btn_cun_one_1"]')  # 滑动到保存
        browser.execute_script("arguments[0].scrollIntoView();", target)  # 滑动到保存
        time.sleep(5)
        browser.find_element_by_xpath('//*[@id="btn_cun_one_1"]').click()#点击保存
        browser.current_window_handle
        time.sleep(5)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="discountDiv"]/p/button[1]')))  # 找到预约挂号的元素
        ys.click()  # 在弹窗中点击是
        time.sleep(2)




#新增、修改保险
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="baoxian"]/a').click()  #点击保险
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="adds_diction"]/button[2]').click()  #点击添加保险
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="form_2"]/ul/li[1]/input').send_keys(u"新增保险")  #
        browser.find_element_by_xpath('//*[@id="form_2"]/ul/li[2]/input').send_keys(u"yinyu")  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="begintimes"]').clear()  #
        browser.find_element_by_xpath('//*[@id="begintimes"]').send_keys(now)
        browser.find_element_by_xpath('//*[@id="overtimes"]').clear()  #
        browser.find_element_by_xpath('//*[@id="overtimes"]').send_keys(u"2023-11-23")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="s_province"]').click()  #
        InputType = Select(browser.find_element_by_xpath('//*[@id="s_province"]'))  # 选择北京市
        InputType.select_by_value("110000")
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="s_city"]').click()  #
        time.sleep(2)
        InputType = Select(browser.find_element_by_xpath('//*[@id="s_city"]'))  #
        InputType.select_by_value("110100")#选择市辖区
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="s_county"]').click()  #
        time.sleep(2)
        InputType = Select(browser.find_element_by_xpath('//*[@id="s_county"]'))  # 选择北京市
        InputType.select_by_value("110105")  # 选择朝阳区
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="form_2"]/ul/li[5]/input').send_keys(u"北辰汇宾大厦B座19层")  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="form_2"]/ul/li[6]/input[2]').click()  #点击禁用
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="form_2"]/ul/li[7]/input').send_keys(u"备注新增保险")  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="sub_btn_insurance"]').click()  #点击保存
        time.sleep(1)
        browser.find_element_by_class_name("make_over_BX").click()  #点击修改
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="form_22"]/ul/li[1]/input').clear()  #
        browser.find_element_by_xpath('//*[@id="form_22"]/ul/li[1]/input').send_keys(u"修改保险")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="form_22"]/ul/li[2]/input').clear()  #
        browser.find_element_by_xpath('//*[@id="form_22"]/ul/li[2]/input').send_keys(u"修改简称")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="begintimes1"]').clear()  #
        browser.find_element_by_xpath('//*[@id="begintimes1"]').send_keys(tom)
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="overtimes1"]').clear()  #
        browser.find_element_by_xpath('//*[@id="overtimes1"]').send_keys(u"2020-11-23")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="s_province1"]').click()  #
        time.sleep(2)
        InputType = Select(browser.find_element_by_xpath('//*[@id="s_province1"]'))  # 选择山东省
        InputType.select_by_value("370000")
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="s_city1"]').click()  #
        time.sleep(2)
        InputType = Select(browser.find_element_by_xpath('//*[@id="s_city1"]'))  # 选择济宁市
        InputType.select_by_value("370800")  # 选择济宁市
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="s_county1"]').click()  #
        time.sleep(2)
        InputType = Select(browser.find_element_by_xpath('//*[@id="s_county1"]'))  # 选择市中区
        InputType.select_by_value("370802")  # 选择朝阳区
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="form_22"]/ul/li[5]/input').clear()  #
        browser.find_element_by_xpath('//*[@id="form_22"]/ul/li[5]/input').send_keys(u"修改地址")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="form_22"]/ul/li[6]/input[1]').click()  #状态选择正常
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="form_22"]/ul/li[7]/input').clear()  #
        browser.find_element_by_xpath('//*[@id="form_22"]/ul/li[7]/input').send_keys(u"修改备注")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="sub_btn_insurance_1"]').click()  #点击保存
        time.sleep(2)



#科室的添加修改
        browser.find_element_by_xpath('//*[@id="keshi"]/a').click()  #点击科室管理
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="adds_diction"]/button[3]').click()  #点击添加科室
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="KS_form"]/div/input').send_keys(u"新增科室")  #输入科室名称
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="KS_form"]/div/div/input').click()  #点击保存
        time.sleep(5)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, "modify_btn")))  #
        ys.click()  #点击修改
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="KS_form_1"]/div/input').clear()
        browser.find_element_by_xpath('//*[@id="KS_form_1"]/div/input').send_keys(u"修改科室名称")  #
        time.sleep(5)
        browser.find_element_by_class_name("form_submit_BTN_1").click()  #点击保存
        time.sleep(2)



#耗材字典
        browser.find_element_by_link_text(u"耗材字典").click()  # 点击耗材字典
        time.sleep(1)
        browser.find_element_by_id("add_consumable_text").click()  # 点击新增耗材
        time.sleep(3)
        browser.current_window_handle  # 此行代码用来定位当前页面
        time.sleep(3)
        browser.find_element_by_css_selector("input.empty-input.consumable-name").clear()  #
        browser.find_element_by_css_selector("input.empty-input.consumable-name").send_keys(u"新增耗材")  # 弹窗中商品名输入
        browser.find_element_by_css_selector("input.empty-input.consumable-standard").clear()  #
        browser.find_element_by_css_selector("input.empty-input.consumable-standard").send_keys(u"新增规格")  # 弹窗中输入规格
        browser.find_element_by_css_selector("input.empty-input.consumable-production").clear()  #
        browser.find_element_by_css_selector("input.empty-input.consumable-production").send_keys(
            u"新增生产厂家")  # 弹窗中输入生产厂家
        browser.find_element_by_css_selector("input.empty-input.packing-unit").clear()  #
        browser.find_element_by_css_selector("input.empty-input.packing-unit").send_keys(u"包")  # 弹窗中输入零售单位
        browser.find_element_by_css_selector("input.empty-input.unit-price").clear()  #
        browser.find_element_by_css_selector("input.empty-input.unit-price").send_keys("10")  # 弹窗中输入售价
        browser.find_element_by_css_selector("input.empty-input.prove-num").clear()  #
        browser.find_element_by_css_selector("input.empty-input.prove-num").send_keys(u"注册证号：14324325")  # 弹窗中输入注册证号
        browser.find_element_by_id("change_consumable_btn").click()  # 点击保存
        time.sleep(2)
        browser.find_element_by_link_text(u"修改").click()  # 点击修改
        time.sleep(2)
        browser.current_window_handle  # 此行代码用来定位当前页面
        time.sleep(2)
        browser.find_element_by_css_selector("input.empty-input.consumable-name").clear()  #
        browser.find_element_by_css_selector("input.empty-input.consumable-name").send_keys(u"修改耗材")  # 修改商品名
        browser.find_element_by_css_selector("input.empty-input.consumable-standard").clear()  #
        browser.find_element_by_css_selector("input.empty-input.consumable-standard").send_keys(u"修改规格")  # 修改规格
        browser.find_element_by_css_selector("input.empty-input.consumable-production").clear()  #
        browser.find_element_by_css_selector("input.empty-input.consumable-production").send_keys(u"修改生产厂家")  # 修改生产厂家
        browser.find_element_by_css_selector("input.empty-input.packing-unit").clear()  #
        browser.find_element_by_css_selector("input.empty-input.packing-unit").send_keys(u"袋")  # 修改包装单位
        browser.find_element_by_css_selector("input.empty-input.unit-price").clear()  #
        browser.find_element_by_css_selector("input.empty-input.unit-price").send_keys("20")  # 修改售价
        browser.find_element_by_css_selector("input.empty-input.prove-num").clear()  #
        browser.find_element_by_css_selector("input.empty-input.prove-num").send_keys(u"修改注册证号：989789")  # 修改注册证号
        time.sleep(2)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="save_consumable_btn"]')))  #
        ys.click()  # 点击保存
        time.sleep(2)
        browser.find_element_by_css_selector("#list-table > tbody > tr:nth-child(1) > td:nth-child(10) > span").click()  # 点击禁用
        time.sleep(2)
        browser.current_window_handle  # 此行代码用来定位当前页面
        time.sleep(2)
        browser.find_element_by_link_text(u"确定").click()  # 点击确定
        browser.find_element_by_css_selector("#list-table > tbody > tr:nth-child(1) > td:nth-child(10) > span").click()  # 点击正常
        time.sleep(2)
        browser.current_window_handle  # 此行代码用来定位当前页面
        time.sleep(2)
        browser.find_element_by_link_text(u"确定").click()  # 点击确定
        browser.find_element_by_css_selector("#list-table > tbody > tr:nth-child(1) > td:nth-child(10) > span").click()  # 点击禁用
        time.sleep(2)
        browser.current_window_handle  # 此行代码用来定位当前页面
        time.sleep(2)
        browser.find_element_by_link_text(u"确定").click()  # 点击确定
        Select(browser.find_element_by_css_selector("select.search_text3")).select_by_visible_text(u"禁用")  # 状态选择禁用
        time.sleep(1)
        browser.find_element_by_id("search_button_type").click()  # 点击搜索
        time.sleep(5)
        Select(browser.find_element_by_css_selector("select.search_text3")).select_by_visible_text(u"正常")  # 状态选择正常
        time.sleep(1)
        browser.find_element_by_id("search_button_type").click()  # 点击搜索
        time.sleep(5)
        Select(browser.find_element_by_css_selector("select.search_text3")).select_by_visible_text(u"全部")  # 状态选择全部
        time.sleep(1)
        browser.find_element_by_id("search_button_type").click()  # 点击搜索
        time.sleep(5)
        browser.find_element_by_css_selector("input.search_text1").clear()  #
        browser.find_element_by_css_selector("input.search_text1").send_keys(u"耗材")  # 在搜索输入框中输入耗材
        time.sleep(1)
        browser.find_element_by_id("search_button_type").click()  # 点击搜索
        time.sleep(5)
        browser.find_element_by_link_text(u"新增").click()  # 耗材分类点击新增
        time.sleep(2)
        browser.current_window_handle  # 此行代码用来定位当前页面
        time.sleep(2)
        browser.find_element_by_css_selector("input.add-type-name").clear()  #
        browser.find_element_by_css_selector("input.add-type-name").send_keys(u"新增分类")  # 在弹窗中输入分类名称
        browser.find_element_by_css_selector("input.add-save-btn").click()  # 点击确定按钮
        browser.find_element_by_id("check_all").click()  # 选择第一页的所有耗材
        browser.find_element_by_css_selector("span.move-type").click()  # 点击移动到分类
        time.sleep(2)
        browser.current_window_handle  # 此行代码用来定位当前页面
        time.sleep(5)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layui-layer19"]/div[2]/div/div/div[2]/ul/li[2]/input')))  #
        ys.click()  #选择一个新增的分类
        time.sleep(1)
        browser.find_element_by_css_selector("input.que-ding").click()  # 点击确定



#药品字典
        time.sleep(3)
        browser.find_element_by_link_text(u"药品字典").click()  # 点击药品字典
        time.sleep(1)
        browser.find_element_by_id("add_medicine_text").click()  # 点击新增药品
        time.sleep(1)
        browser.find_element_by_name("genericname").click()  #
        browser.find_element_by_name("genericname").clear()  #
        browser.find_element_by_name("genericname").send_keys(u"新增药品")  # 输入通用名
        time.sleep(2)
        browser.find_element_by_name("nameeng").click()  #
        browser.find_element_by_name("nameeng").clear()  #
        browser.find_element_by_name("nameeng").send_keys("yinwen")  # 输入英文
        browser.find_element_by_name("product").click()  #
        browser.find_element_by_name("product").clear()  #
        browser.find_element_by_name("product").send_keys(u"新增生产厂家")  # 输入生产厂家
        browser.find_element_by_name("approval").click()  #
        browser.find_element_by_name("approval").clear()  #
        browser.find_element_by_name("approval").send_keys(u"新增批准文号：241234453")  # 输入批准文号
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="form_stock"]/div[1]/div[3]/ul/li[2]/span[2]/span[1]/span/span[2]').click()#点击药品类型
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u"西药")
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="form_stock"]/div[1]/div[1]/ul/li[3]/span[2]/span[1]/span/span[2]').click()  # 点击毒理分类
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u"精二类")
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)
        time.sleep(1)
        browser.find_element_by_name("isoct").click()  # 选择是OTC
        browser.find_element_by_name("isst").click()  # 选择是皮试
        browser.find_element_by_name("starnderdesc").click()  #
        browser.find_element_by_name("starnderdesc").clear()  #
        browser.find_element_by_name("starnderdesc").send_keys(u"新增规格12ml/瓶")  # 输入规格
        browser.find_element_by_xpath('//*[@id="form_stock"]/div[2]/div[2]/ul/li[1]/span[2]/span[1]/span/span[2]').click()  # 点击剂型
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u"丸剂")
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)
        browser.find_element_by_name("sellunit").click()  # 选择剂型
        browser.find_element_by_xpath("//form[@id='form_stock']/div[2]/div[3]/ul/li/div/ul/li[8]").click()  # 点击售价单位
        browser.find_element_by_name("dosageunit").click()  # 选择售价单位
        browser.find_element_by_xpath("//form[@id='form_stock']/div[2]/div/ul/li[2]/div/ul/li[3]").click()  # 点击计量单位
        browser.find_element_by_name("selltodosage").click()#选择计量单位
        browser.find_element_by_name("selltodosage").clear()  #
        browser.find_element_by_name("selltodosage").send_keys("12")  # 填写1盒=
        browser.find_element_by_xpath('//*[@id="form_stock"]/div[3]/div[1]/ul/li[1]/span[2]/span[1]/span/span[2]').click()  # 点击用法
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u"外用")
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)
        time.sleep(1)
        browser.find_element_by_name("dosagegrown").clear()  #
        browser.find_element_by_name("dosagegrown").send_keys("12")  # 输入成人计量
        browser.find_element_by_name("defaultnum").click()  #
        browser.find_element_by_name("defaultnum").clear()  #
        browser.find_element_by_name("defaultnum").send_keys("3")  # 输入默认开药量
        browser.find_element_by_xpath('//*[@id="form_stock"]/div[3]/div[1]/ul/li[2]/span[2]/span[1]/span/span[2]').click()  # 点击用药频次
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u"每天三次")
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)
        browser.find_element_by_name("dosagechild").clear()  #
        browser.find_element_by_name("dosagechild").send_keys("12")  # 输入儿童计量
        browser.find_element_by_name("advice").click()  # 点击医嘱
        browser.find_element_by_xpath("//form[@id='form_stock']/div[3]/div[3]/ul/li[2]/div/ul/li[5]").click()  # 选择医嘱
        browser.find_element_by_name("sellprice").click()  #
        browser.find_element_by_name("sellprice").clear()  #
        browser.find_element_by_name("sellprice").send_keys("20")  # 输入零售价
        browser.find_element_by_id("save_btn").click()  # 点击保存
        time.sleep(3)
        browser.find_element_by_xpath('//*[@id="goBack"]').click()  #点击返回
        time.sleep(2)
        browser.find_element_by_link_text(u"修改").click()  # 点击修改
        time.sleep(1)
        browser.find_element_by_name("genericname").click()  #
        browser.find_element_by_name("genericname").click()  #
        browser.find_element_by_name("genericname").clear()  #
        browser.find_element_by_name("genericname").send_keys(u"修改药品")  # 修改通用名
        time.sleep(2)
        browser.find_element_by_name("nameeng").click()  #
        browser.find_element_by_name("nameeng").clear()  #
        browser.find_element_by_name("nameeng").send_keys(u"修改")  # 修改英文名
        time.sleep(2)
        browser.find_element_by_name("product").click()  #
        browser.find_element_by_name("product").click()  #
        browser.find_element_by_name("product").clear()  #
        browser.find_element_by_name("product").send_keys(u"修改")  # 修改生产厂家
        browser.find_element_by_name("approval").click()  #
        browser.find_element_by_name("approval").clear()  #
        browser.find_element_by_name("approval").send_keys(u"修改批准文号")  # 修改批准文号
        browser.find_element_by_xpath('//*[@id="form_stock"]/div[1]/div[3]/ul/li[2]/span[2]/span[1]/span/span[2]').click()  # 点击药品类型
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u"中草药")
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)
        browser.find_element_by_xpath('//*[@id="form_stock"]/div[1]/div[1]/ul/li[3]/span[2]/span[1]/span/span[2]').click()  # 点击毒理分类
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u"麻醉药")
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)
        browser.find_element_by_name("starnderdesc").click()  # 否OTC
        browser.find_element_by_name("starnderdesc").clear()  # 否皮试
        browser.find_element_by_name("starnderdesc").send_keys(u"修改规格12ml/瓶")  # 修改规格
        browser.find_element_by_xpath('//*[@id="form_stock"]/div[2]/div[2]/ul/li[1]/span[2]/span[1]/span/span[2]').click()  # 点击剂型
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u"滴剂")
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="form_stock"]/div[2]/div[3]/ul/li/div').click()#点击售价单位
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="form_stock"]/div[2]/div[3]/ul/li/div/ul/li[5]').click()#选择袋
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="form_stock"]/div[2]/div[1]/ul/li[2]/div').click()#点击计量单位
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="form_stock"]/div[2]/div[1]/ul/li[2]/div/ul/li[6]').click()#选择计量单位
        time.sleep(2)
        browser.find_element_by_name("selltodosage").clear()  #
        browser.find_element_by_name("selltodosage").send_keys("10")  # 1袋=
        browser.find_element_by_xpath('//*[@id="form_stock"]/div[3]/div[1]/ul/li[1]/span[2]/span[1]/span/span[2]').click()  # 点击用法
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u"吸入")
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)
        browser.find_element_by_name("dosagegrown").clear()  #
        browser.find_element_by_name("dosagegrown").send_keys("10")  # 修改成人计量
        browser.find_element_by_name("defaultnum").click()  #
        browser.find_element_by_name("defaultnum").clear()  #
        browser.find_element_by_name("defaultnum").send_keys("5")  # 修改默认开药量
        browser.find_element_by_xpath('//*[@id="form_stock"]/div[3]/div[1]/ul/li[2]/span[2]/span[1]/span/span[2]').click()  # 点击用药频次
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u"每小时五次")
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)
        browser.find_element_by_name("dosagechild").clear()  #
        browser.find_element_by_name("dosagechild").send_keys("5")  # 修改儿童计量
        browser.find_element_by_name("advice").click()  # 点击医嘱
        browser.find_element_by_xpath("//form[@id='form_stock']/div[3]/div[3]/ul/li[2]/div/ul/li[2]").click()  # 选择医嘱
        browser.find_element_by_name("sellprice").click()  #
        browser.find_element_by_name("sellprice").clear()  #
        browser.find_element_by_name("sellprice").send_keys("30")  # 修改售价
        browser.find_element_by_id("save_btn").click()  # 点击保存
        time.sleep(2)
        browser.find_element_by_css_selector("span.state-medicine").click()  # 点击禁用
        time.sleep(1)
        browser.current_window_handle  # 此行代码用来定位当前页面
        time.sleep(1)
        browser.find_element_by_link_text(u"确定").click()  # 弹窗中browser
        time.sleep(2)
        browser.find_element_by_css_selector("span.state-medicine").click()  # 点击启用
        time.sleep(1)
        browser.current_window_handle  # 此行代码用来定位当前页面
        time.sleep(1)
        browser.find_element_by_link_text(u"确定").click()  # 弹窗中browser
        Select(browser.find_element_by_css_selector("select.search_text3")).select_by_visible_text(u"正常")  # 筛选状态为正常的
        time.sleep(1)
        browser.find_element_by_id("search_button_type").click()  #
        time.sleep(1)
        Select(browser.find_element_by_css_selector("select.search_text3")).select_by_visible_text(u"禁用")  # 筛选状态为禁用的
        browser.find_element_by_id("search_button_type").click()  #
        time.sleep(1)
        Select(browser.find_element_by_css_selector("select.search_text3")).select_by_visible_text(u"全部")  # 筛选状态为全部
        browser.find_element_by_id("search_button_type").click()  #
        time.sleep(1)
        browser.find_element_by_css_selector("input.search_text1").clear()  #
        browser.find_element_by_css_selector("input.search_text1").send_keys(u"药品")  # 筛选通用名或者商品名包含“药品”的药
        browser.find_element_by_id("search_button_type").click()  # 点击搜索
        time.sleep(2)
        browser.find_element_by_css_selector("input.search_text2").clear()  #
        browser.find_element_by_css_selector("input.search_text2").send_keys(u"修改")  # 筛选生产厂家含’修改的‘
        browser.find_element_by_id("search_button_type").click()  # 点击搜索
        time.sleep(2)
        browser.find_element_by_css_selector("input.search_text2").clear()  #
        browser.find_element_by_css_selector("input.search_text2").send_keys("")  # 清空通用名、商品名输入框
        browser.find_element_by_css_selector("input.search_text1").clear()  #
        browser.find_element_by_css_selector("input.search_text1").send_keys("")  # 清空生产厂家输入框
        browser.find_element_by_id("search_button_type").click()  # 点击搜索
        time.sleep(2)
        browser.find_element_by_link_text(u"新增").click()  # 点击新增分类
        time.sleep(1)
        browser.current_window_handle  # 此行代码用来定位当前页面
        time.sleep(1)
        browser.find_element_by_css_selector("input.add-type-name").clear()  #
        browser.find_element_by_css_selector("input.add-type-name").send_keys(u"新增分类")  # 弹窗中输入新增分类名称
        browser.find_element_by_css_selector("input.add-save-btn").click()  #
        time.sleep(2)
        browser.find_element_by_id("check_all").click()  # 选择第一页的药品
        browser.find_element_by_css_selector("span.move-type").click()  # 点击移动到分类
        time.sleep(2)
        browser.current_window_handle  # 此行代码用来定位当前页面
        time.sleep(2)
        browser.find_element_by_name("type").click()  # 在弹窗中选择分类
        time.sleep(2)
        browser.find_element_by_css_selector("input.que-ding").click()  # 点击确定
        time.sleep(2)





#医用字典
        time.sleep(2)
        browser.find_element_by_link_text(u"医用字典").click()  # 点击医用字典
        browser.find_element_by_css_selector("li.check").click()  # 点击处方用法
        time.sleep(2)
        browser.find_element_by_css_selector("#add_yiyong_text > span").click()  # 点击新增用法
        browser.find_element_by_css_selector("input.xiyao_name").clear()  #
        browser.find_element_by_css_selector("input.xiyao_name").send_keys(u"新增处方用法")  # 输入用法名称
        browser.find_element_by_id("forbidden").click()  # 状态点击禁用
        browser.find_element_by_css_selector("span.btn.keepinfo1").click()  # 点击保存
        time.sleep(5)
        browser.find_element_by_css_selector("span.alter_1").click()  # 点击修改
        browser.find_element_by_css_selector("input.xiyao_name").clear()  #
        browser.find_element_by_css_selector("input.xiyao_name").send_keys(u"修改处方用法")  # 修改用法名称
        browser.find_element_by_id("male1").click()  # 状态选择正常
        browser.find_element_by_css_selector("span.btn.keepinfo2").click()  # 选择保存
        time.sleep(5)
        browser.find_element_by_xpath("//ul[@id='useList']/li[2]").click()  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="add_yiyong_text"]').click()  # 点击新增频次
        time.sleep(1)
        browser.find_element_by_css_selector("input.times_data").clear()  #
        browser.find_element_by_css_selector("input.times_data").send_keys("6")  # 输入6天
        browser.find_element_by_css_selector("input.interval_data").clear()  #
        browser.find_element_by_css_selector("input.interval_data").send_keys("8")  # 输入8次
        browser.find_element_by_css_selector("div.add_frequency_div.layui-layer-wrap > div > p > span.jin2 > #forbidden").click()  # 状态选择禁用
        time.sleep(1)
        browser.find_element_by_css_selector("span.btn.rateinfo1").click()  # 点击保存
        time.sleep(5)
        browser.find_element_by_css_selector("span.alter_2").click()  # 点击修改
        time.sleep(2)
        browser.current_window_handle  # 此行代码用来定位当前页面
        time.sleep(5)
        browser.find_element_by_css_selector("input.times_data").clear()  #
        browser.find_element_by_css_selector("input.times_data").send_keys("8")  # 输入天数
        browser.find_element_by_css_selector("input.interval_data").clear()  #
        browser.find_element_by_css_selector("input.interval_data").send_keys("10")  # 输入次数
        browser.find_element_by_name("status1").click()  # 状态选择正常
        time.sleep(1)
        browser.find_element_by_css_selector("span.btn.rateinfo2").click()  # 点击保存
        time.sleep(5)
        browser.find_element_by_xpath('//*[@id="useList"]/li[3]').click()  # 点击草药处方用法
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="add_yiyong_text"]/span[3]').click()  # 点击新增用法
        time.sleep(2)
        browser.find_element_by_css_selector("input.xiyao_name").clear()  #
        browser.find_element_by_css_selector("input.xiyao_name").send_keys(u"新增草药处方用法")  # 输入用法名称
        browser.find_element_by_id("forbidden").click()  # 状态选择禁用
        browser.find_element_by_css_selector("span.btn.keepinfo3").click()  # 点击保存
        time.sleep(5)
        browser.find_element_by_css_selector("span.alter_3").click()  # 点击修改
        time.sleep(1)
        browser.find_element_by_css_selector("input.xiyao_name").clear()  #
        browser.find_element_by_css_selector("input.xiyao_name").send_keys(u"修改草药处方用法")  # 修改用法名称
        browser.find_element_by_id("male1").click()  # 状态选择正常
        browser.find_element_by_css_selector("span.btn.keepinfo4").click()  # 点击保存
        time.sleep(5)


#供应商维护
        browser.find_element_by_xpath('//*[@id="gonghuo"]/a').click()  #点击供应商维护
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="adds_diction"]/button[7]').click()  #点击添加供应商
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="form_2"]/ul/li[1]/input').send_keys(u"新增供应商")  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="form_2"]/ul/li[2]/input[2]').click()  #点击禁用
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="sub_btn_insurance"]').click()  #点击保存
        time.sleep(3)
        browser.refresh()
        time.sleep(3)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, "make_over_BX")))  #
        ys.click()  # 点击修改
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="form_22"]/ul/li[1]/input').clear()  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="form_22"]/ul/li[1]/input').send_keys(u"修改供应商")  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="form_22"]/ul/li[2]/input[1]').click()  #点击正常
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="sub_btn_insurance_1"]').click()  #点击保存
        time.sleep(1)

if __name__ == '__main__':
    unittest.main()