# coding:utf-8
from selenium import webdriver
import unittest
import time
from commonshare.His import Browser
p = Browser()
class TestHis(unittest.TestCase):
    def setUp(self):
        p.Browserinit("http://yun.oasisapp.cn:9080/uc/authentication/check?login=true&phone=&redirectUrl=http://yun.oasisapp.cn:8080/yunhis/security_check.action")
        p.TestLogin("17111111111","111111")#登录并选择金融街诊所
        p.BookingRegister(u"董焕焕","18611069298")#预约挂号
        p.DoctorBench()# 点击医生工作台
        p.ClickJz()
        p.Case(u"感冒、发烧、咳嗽、嗓子疼",u"感冒")#填写病例信息
        p.SaveButton('//*[@id="history_save"]')#点击保存
        p.ClickCheckout()#点击检验项目
        p.WriteCheckout(u"过敏原检测(食物组)")#输入检验项目"过敏原检测(食物组)"
        p.WriteCheckout(u"ABO血型")#输入检验项目"u"ABO血型""
        p.SaveButton('//*[@id="inspect_save"]')#点击保存
        p.Click('//*[@id="seeDoctoring_nav"]/ul/li[3]/a')# 点击检查项目
        p.Click('//*[@id="select2-checkoutSearchLis-container"]')
        p.WriteInspect(u"多普勒听胎心")
        p.Click('//*[@id="select2-checkoutSearchLis-container"]')
        p.WriteInspect(u"泌尿系超声")
        p.SaveButton('//*[@id="saveCheckoutItems"]')
        p.ClickTherapy()
        p.ClickTherapy()#点击治疗
        p.WriteTherapy(u"隔物灸法")#填写治疗项
        p.ClearImport('//*[@id="selectedInspectListBox"]/form/div/div[3]/input',10)
        p.WriteTherapy(u"颈椎正骨治疗")
        p.SaveButton('//*[@id="inspect_save"]')
        p.Click('//*[@id="seeDoctoring_nav"]/ul/li[5]/a')#点击处方
        p.Prescription(u"阿司匹林肠溶片")
        p.Prescription(u"硫酸庆大霉素注射液")
        p.Click('//*[@id="prescriptionContentBox"]/div[4]/div/div/select')#点击诊费输入框
        p.Select("#prescriptionContentBox > div.consultation_fee > div > div > select > option:nth-child(2)")#选择常规诊费
        p.Import("#addOtherFee",u"护士出诊(平日)")#在其他费用处输入护士出诊(平日)
        p.Select("#addOtherRelateList > p > span.name.name-text")#选择护士出诊(平日)
        p.Click('//*[@id="prescription_save"]')#点击保存
        p.Click('//*[@id="seeDoctoring_nav"]/ul/li[6]/a')#点击草药处方
        p.ChinesePrescription(u"荆芥",30)
        p.ChinesePrescription(u"防风", 30)
        p.ChinesePrescription(u"羌活", 30)
        p.ChinesePrescription(u"独活", 30)
        p.ChinesePrescription(u"川芎", 30)
        p.ChinesePrescription(u"醋北柴胡", 30)
        p.ChinesePrescription(u"前胡", 30)
        p.ChinesePrescription(u"桔梗", 30)
        p.ChinesePrescription(u"麸炒枳壳", 30)
        p.ChinesePrescription(u"土茯苓", 30)
        p.ChinesePrescription(u"炙甘草", 15)
        p.Import("#herbalsPresBox > div > div.consultation_fee > div > div > input",6)
        p.Down('//*[@id="herbalsPresBox"]/div/div[4]/div/div[2]/textarea')
        p.Import("#herbalsPresBox > div > div.other-prescription-tiems > div > div.herbal-pres-nose > textarea",u"饭后服用一天两次")
        p.SaveButton('//*[@id="herbalPres_save"]')
        p.Click('//*[@id="contaleBtn"]/button[4]/a')#点击结束就诊
        p.Click('//*[@id="offMadicalMess"]/div/a/button')#是否结束就诊点击是
        p.Click('/html/body/div[2]/aside/section/ul/li[8]/a/span[1]')#点击收费发药
        p.Click('//*[@id="content"]/div[1]/div/div/ul/li[2]/a')#点击收费
        p.Click('//*[@id="ajax-content"]/div/div[1]/div[2]/ul/li[1]/div/div[2]')#点击待收费
        p.Down('//*[@id="ajax-content"]/div/div[2]/form/div/div[2]/div[10]')#滑动到收费按钮
        p.ClickLong('//*[@id="ajax-content"]/div/div[2]/form/div/div[2]/div[9]/p[1]/i')#点击收费
        p.ClickLong('//*[@id="layui-layer50"]/div[2]/div/ul/li[2]/div[2]/input')#点击刷卡
        p.ClickLong('//*[@id="print_buying"]')#点击确定
        time.sleep(3)
        p.Back()#点击返回
        p.Click('//*[@id="content"]/div[1]/div/div/ul/li[4]/a')#点击结算管理
        p.Click('//*[@id="table_excel"]/tbody/tr[1]/td[13]/a')#点击详情
        p.Down('//*[@id="ajax-content"]/div/div[1]/div[3]/div[7]')#详情页滑动到最下方
        p.Click('//*[@id="ajax-content"]/div/div[1]/div[3]/div[7]/a/span')#点击退费
        p.Click('//*[@id="ajax-content"]/div/div[1]/div[3]/div[3]/table/thead/tr/th[1]/label/input')#点击全选框
        p.Down('//*[@id="ajax-content"]/div/div[1]/div[3]/div[7]')#滑动到退费页的最下方
        p.Click('//*[@id="ajax-content"]/div/div[1]/div[3]/div[7]/span')#点击提交
        p.Click('//*[@id="layui-layer2"]/div[3]/a[1]')#点击确认
        time.sleep(3)
        p.Back()
if __name__ == '__main__':
    unittest.main()