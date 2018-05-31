#coding:utf-8
import requests
import json
#不带参数的接口
# r = requests.get('http://www.cnblogs.com/yoyoketang/')
# print r.status_code
# print r.text


#带参数的接口
# par = {"Keywords":"yoyoketang"}
# r = requests.get('http://zzk.cnblogs.com/s/blogpost',params=par)
# print r.status_code
# print r.text


# r = requests.get('https://www.baidu.com/',verify=False)  #verify=False最简单的就是关闭校验,关闭检验https请求就OK了
# print r.url
# print r.encoding  #编码
# print r.content #获取返回内容
# print r.headers
# print r.cookies
#
# #post请求
# payload = {"yoyo":"hello world",
#            "pythonQQ群":"226296743"}
# #转化为json格式
# data_json = json.dumps(payload)
# r = requests.post('http://httpbin.org/post',json=data_json)
# print (r.text)

# #登录
# url = "http://yun.oasisapp.cn:9080/uc/authentication/loginForWeb"
#
# headers = {"Host": "yun.oasisapp.cn:9080",
# "Connection": "keep-alive",
# "Content-Length": "109",
# "Cache-Control": "max-age=0",
# "Origin": "http://yun.oasisapp.cn:9080",
# "Upgrade-Insecure-Requests": "1",
# "Content-Type": "application/x-www-form-urlencoded",
# "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36",
# "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
# "Referer": "http://yun.oasisapp.cn:9080/uc/authentication/check?login=true&phone=&redirectUrl=http://yun.oasisapp.cn:8080/yunhis/security_check.action",
# "Accept-Encoding": "gzip, deflate",
# "Accept-Language": "zh-CN,zh;q=0.9",
# "Cookie": "JSESSIONID=CA100CE1E2B24B8A686D51385902A8DF"
# }
# payload = "redirectUrl=http%3A%2F%2Fyun.oasisapp.cn%3A8080%2Fyunhis%2Fsecurity_check.action&uname=17444444444&pwd=444444"
# r = requests.post(url,json=payload,headers=headers,verify=False)
# print r.json()

#
# payload = {"yoyo":"hello world",
#            "pythonQQ群": "226296743"}
# #转化为json格式
# data_json = json.dumps(payload)
# r = requests.post('http://httpbin.org/post',json=data_json)
# print (r.text)


# #博客园登录
# url = "https://passport.cnblogs.com/user/signin"
# headers = {"Connection": "keep-alive",
# "Content-Length": "557",
# "Accept": "application/json, text/javascript, */*; q=0.01",
# "Origin": "https://passport.cnblogs.com",
# "X-Requested-With": "XMLHttpRequest",
# "VerificationToken": "@TokenHeaderValue()",
# "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36",
# "Content-Type": "application/json; charset=UTF-8",
# "Referer": "https://passport.cnblogs.com/user/signin",
# "Accept-Encoding": "gzip, deflate, br",
# "Accept-Language": "zh-CN,zh;q=0.9",
# "Cookie": "_ga=GA1.2.581740237.1522115039; UM_distinctid=162fc05a7a550-08daf7b9e734bb-4542072c-144000-162fc05a7a65ec; __gads=ID=6e71a00683a09505:T=1524905313:S=ALNI_MYy-DCWxnPj-IYvIy6a_-m6NbMIog; ASP.NET_SessionId=3y0dfvj5jhunj4mrqapwodwo; _gid=GA1.2.1429512175.1525232617; SERVERID=34e1ee01aa40e94e2474dffd938824db|1525241578|1525241449"
# }
#
# payload = {"input1":"NxVkd0Ytd6jGVzN5R3Ettzi2dEv8K+J+Tz0LP9KcQOVQ2FlL1ISy0kGgG6zFFi+lAzCMj5Ue39Oj2lokgRWZNha5/Mou/flsHgIQGAgTFjo+8L5qskrEVoYUewxq7xDIuQTK/K46eYTFvP37B/L5z4jHjUPBanj+ZspS3QBiIg0=","input2":"AtSmmz9Wfb+ENHTVeaHvrVgHd6B3adWuoXqPssFTmvHr0tUuyhu+/LNpwmgdOMUPnFdJMQ/FVAcPIdiJrhj3rEhj3qL//scNrVvzmhTzK3MhzF1S01Bepx+XX3OVH8dEeAAp/dzhZSPEjrO53sDFJk9HWa+qcjBoSaIElCW3DEc=","remember":"false","geetest_challenge":"13b946e826273e43e2f4f9829e7371e3jx","geetest_validate":"d3b56c8eae402dcca90d03f93d4f99a7","geetest_seccode":"d3b56c8eae402dcca90d03f93d4f99a7|jordan"}
# r = requests.post(url, json=payload, headers=headers,verify=False)
# print r.json()

#his登录
# 先打开登录首页，获取部分cookie
url = "http://yun.oasisapp.cn:9080/uc/authentication/loginForWeb"
headers = {"Connection": "keep-alive",
"Content-Length": "109",
"Cache-Control": "max-age=0",
"Origin": "http://yun.oasisapp.cn:9080",
"Upgrade-Insecure-Requests": "1",
"Content-Type": "application/x-www-form-urlencoded",
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"Referer": "http://yun.oasisapp.cn:9080/uc/authentication/check?login=true&phone=&redirectUrl=http://yun.oasisapp.cn:8080/yunhis/security_check.action",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "zh-CN,zh;q=0.9",
"Cookie": "JSESSIONID=1651F4D49753298DB32E357B69435FED"
} # get方法其它加个ser-Agent就可以了
d = {"redirectUrl": "http://yun.oasisapp.cn:8080/yunhis/security_check.action", "uname": "15555555555", "pwd": "555555" }
s = requests.session()
r = s.post(url, headers=headers, data=d)
print r.content
# 正则表达式提取账号和登录按钮
import re
# t = re.findall(r'<a>(.+?)</a>', r.content)
# t = re.findall(r.content)
# print t[0]
