#coding:utf-8

from lib import HTMLTestRunner
import unittest
from lianxi.lianxi_a import TestHis


if __name__=='__main__':
    suite=unittest.makeSuite(TestHis)
    filename='D:\\myreport.html'
    fp=file(filename,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(fp,title=u'my unit test',description=u'This is a report test')
    runner.run(suite)