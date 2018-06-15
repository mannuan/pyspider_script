#-*- coding:utf-8 -*-
import time,random,re,sys,json
from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
reload(sys)
sys.setdefaultencoding('utf8')
from pyvirtualdisplay import Display

def getPhantomJsWebDriver():
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.userAgent"] = (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11) AppleWebKit/601.1.27 (KHTML, like Gecko) Version/8.1 Safari/601.1.27")
    service_args=[]
    # service_args.append('--load-images=no')
    # service_args.append('--disk-cache=yes')
    # service_args.append('--ignore-ssl-errors=true')
    driver = webdriver.PhantomJS(desired_capabilities=dcap,service_args=service_args)
    driver.set_page_load_timeout(15)
    driver.set_script_timeout(15)#这两种设置都进行才有效
    driver.implicitly_wait(15)#隐性等待
    return driver

def getPhantomJsMobileDriver():
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.userAgent"] = (
        "Mozilla/5.0 (iPhone; CPU iPhone OS 9_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13C75 Safari/601.1")
    service_args=[]
    # service_args.append('--load-images=no')
    # service_args.append('--disk-cache=yes')
    # service_args.append('--ignore-ssl-errors=true')
    driver = webdriver.PhantomJS(desired_capabilities=dcap,service_args=service_args)
    driver.set_page_load_timeout(15)
    driver.set_script_timeout(15)#这两种设置都进行才有效
    driver.implicitly_wait(15)#隐性等待
    return driver

def getChromeWebDriver():
    options = webdriver.ChromeOptions()
    options.add_argument(
        'user-agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/11.10 Chromium/27.0.1453.93 Chrome/27.0.1453.93 Safari/537.36"')
    service_args=[]
    # service_args.append('--load-images=no')
    # service_args.append('--disk-cache=yes')
    # service_args.append('--ignore-ssl-errors=true')
    driver = webdriver.Chrome(chrome_options=options,service_args=service_args)
    driver.set_page_load_timeout(15)
    driver.set_script_timeout(15)#这两种设置都进行才有效
    driver.implicitly_wait(15)#隐性等待
    return driver

def getChromeMobileDriver():
    options = webdriver.ChromeOptions()
    options.add_argument('lang=zh_CN.UTF-8')
    options.add_argument('user-agent="Mozilla/5.0 (iPhone; CPU iPhone OS 9_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13C75 Safari/601.1"')
    service_args=[]
    # service_args.append('--load-images=no')
    # service_args.append('--disk-cache=yes')
    # service_args.append('--ignore-ssl-errors=true')
    driver = webdriver.Chrome(chrome_options=options,service_args=service_args)
    driver.set_page_load_timeout(15)
    driver.set_script_timeout(15)#这两种设置都进行才有效
    driver.implicitly_wait(15)#隐性等待
    return driver

def getChromeHeaderlessWebDriver():
    display = Display(visible=0, size=(800, 600))
    display.start()
    options = webdriver.ChromeOptions()
    options.add_argument(
        'user-agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/11.10 Chromium/27.0.1453.93 Chrome/27.0.1453.93 Safari/537.36"')
    # chrome_options.add_argument('lang=zh_CN.UTF-8')
    # chrome_options.add_argument('--headless')
    service_args=[]
    # service_args.append('--load-images=no')
    # service_args.append('--disk-cache=yes')
    # service_args.append('--ignore-ssl-errors=true')
    driver = webdriver.Chrome(chrome_options=options,service_args=service_args)
    driver.set_page_load_timeout(15)
    driver.set_script_timeout(15)#这两种设置都进行才有效
    driver.implicitly_wait(15)#隐性等待
    return driver

def getChromeHeaderlessMobileDriver():
    # display = Display(visible=0, size=(800, 600))
    # display.start()
    options = webdriver.ChromeOptions()
    options.add_argument('lang=zh_CN.UTF-8')
    options.add_argument('--headless')
    options.add_argument('user-agent="Mozilla/5.0 (iPhone; CPU iPhone OS 9_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13C75 Safari/601.1"')
    service_args=[]
    # service_args.append('--load-images=no')
    # service_args.append('--disk-cache=yes')
    # service_args.append('--ignore-ssl-errors=true')
    driver = webdriver.Chrome(chrome_options=options,service_args=service_args)
    driver.set_page_load_timeout(15)
    driver.set_script_timeout(15)#这两种设置都进行才有效
    driver.implicitly_wait(15)#隐性等待
    return driver