#-*- coding:utf-8 -*-
import time,random,re,sys,json
from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import DesiredCapabilities
reload(sys)
sys.setdefaultencoding('utf8')

def getPhantomJsWebDriver():
    service_args=[]
    service_args.append('--load-images=no')
    service_args.append('--disk-cache=yes')
    service_args.append('--ignore-ssl-errors=true')
    driver = webdriver.PhantomJS()
    driver.set_page_load_timeout(15)
    driver.set_script_timeout(15)#这两种设置都进行才有效
    driver.implicitly_wait(15)#隐性等待
    return driver

def getPhantomJsMobileDriver():
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.userAgent"] = (
        "Mozilla/5.0 (iPhone; CPU iPhone OS 9_2 like Mac OS X) AppleWebKit/601.1 (KHTML, like Gecko) CriOS/47.0.2526.107 Mobile/13C75 Safari/601.1.46")
    service_args=[]
    service_args.append('--load-images=no')
    service_args.append('--disk-cache=yes')
    service_args.append('--ignore-ssl-errors=true')
    driver = webdriver.PhantomJS(desired_capabilities=dcap,service_args=service_args)
    driver.set_page_load_timeout(15)
    driver.set_script_timeout(15)#这两种设置都进行才有效
    driver.implicitly_wait(15)#隐性等待
    return driver

def getChromeWebDriver():
    service_args=[]
    service_args.append('--load-images=no')
    service_args.append('--disk-cache=yes')
    service_args.append('--ignore-ssl-errors=true')
    driver = webdriver.Chrome(service_args=service_args)
    driver.set_page_load_timeout(15)
    driver.set_script_timeout(15)#这两种设置都进行才有效
    driver.implicitly_wait(15)#隐性等待
    return driver

def getChromeMobileDriver():
    # 进入浏览器设置
    options = webdriver.ChromeOptions()
    # 设置中文
    options.add_argument('lang=zh_CN.UTF-8')
    # 更换头部
    options.add_argument('user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')
    service_args=[]
    service_args.append('--load-images=no')
    service_args.append('--disk-cache=yes')
    service_args.append('--ignore-ssl-errors=true')
    driver = webdriver.Chrome(chrome_options=options,service_args=service_args)
    driver.set_page_load_timeout(15)
    driver.set_script_timeout(15)#这两种设置都进行才有效
    driver.implicitly_wait(15)#隐性等待
    return driver

def getChromeHeaderlessWebDriver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    service_args=[]
    service_args.append('--load-images=no')
    service_args.append('--disk-cache=yes')
    service_args.append('--ignore-ssl-errors=true')
    driver = webdriver.Chrome(chrome_options=chrome_options,service_args=service_args)
    driver.set_page_load_timeout(15)
    driver.set_script_timeout(15)#这两种设置都进行才有效
    driver.implicitly_wait(15)#隐性等待
    return driver

def getChromeHeaderlessMobileDriver():
    # 进入浏览器设置
    options = webdriver.ChromeOptions()
    # 设置中文
    options.add_argument('lang=zh_CN.UTF-8')
    options.add_argument('--headless')
    # 更换头部
    options.add_argument('user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')
    service_args=[]
    service_args.append('--load-images=no')
    service_args.append('--disk-cache=yes')
    service_args.append('--ignore-ssl-errors=true')
    driver = webdriver.Chrome(chrome_options=options,service_args=service_args)
    driver.set_page_load_timeout(15)
    driver.set_script_timeout(15)#这两种设置都进行才有效
    driver.implicitly_wait(15)#隐性等待
    return driver