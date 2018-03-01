#coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


import unittest
import os
import HTMLTestRunner


#执行所有测试用例

# python2.7要是报编码问题，就加这三行，python3不用加

import sys
reload(sys)
sys.setdefaultencoding('utf8')

# 用例路径
case_path = os.path.join(os.getcwd(), "case")
# 报告存放路径
report_path = os.path.join(os.getcwd(), "report")
def all_case():
    discover = unittest.defaultTestLoader.discover(case_path,
                                                    pattern="test*.py",
                                                    top_level_dir=None)
    print(discover)
    return discover

if __name__ == "__main__":
    # runner = unittest.TextTestRunner()
    # runner.run(all_case())

    # html报告文件路径
    report_abspath = os.path.join(report_path, "result.html")
    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'自动化测试报告,测试结果如下：',
                                           description=u'用例执行情况：')

    # 调用add_case函数返回值
    runner.run(all_case())
    fp.close()



#发送邮件
#————1、根发邮件相关的参数————
smtpserver = "smtp.163.com"      #发件服务器
port = 0                         #端口
sender = "18611059298@163.com"   #账号
psw = "yangaihuan13"             #密码
receiver = "1280480542@qq.com"   #接收人

#————2、编辑邮件内容————
#读文件
file_path = "E:\\test\\untitled_his\\report\\result.html"#测试报告所存放的路径：即result.html的路径
with open(file_path,"rb") as fp:
    mail_body = fp.read()
msg = MIMEMultipart()
msg["from"] = sender   #发件人
msg["to"] = receiver   #收件人
msg["subject"] = "云his自动化测试报告"  #主题

#正文
body = MIMEText(mail_body,"html","utf-8")
msg.attach(body)

#附件
att = MIMEText(mail_body,"base64","utf-8")
att["Content-Type"] = "application/octet-stream"
att["Content-Disposition"] = 'attachment;filename="test_report.html" '
msg.attach(att)

#发送邮件
try:
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)  #链接服务器
    smtp.login(sender,psw)
except:
    smtp = smtplib.SMTP_SSL(smtpserver,port)
    smtp.login(sender,psw)            #登录
smtp.sendmail(sender,receiver,msg.as_string())  #发送
smtp.quit()