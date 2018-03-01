# coding:utf-8
from selenium import webdriver
import unittest
import time
from locale import *
import datetime
browser = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")  # chromedriver.exe文件的路径
global browser
class Browser():
    setlocale(LC_NUMERIC, 'English_US')
