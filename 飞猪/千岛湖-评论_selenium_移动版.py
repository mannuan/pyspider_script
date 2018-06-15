# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,random,re,sys,json
reload(sys)
sys.setdefaultencoding('utf8')
from pymongo import MongoClient

conn = MongoClient('localhost', 27017)
db = conn.feizhu_qiandaohu  # 连接feizhu_qiandaohu数据库，没有则自动创建
comments = db.comments  # 使用comments集合,没有则自动创建

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
driver.implicitly_wait(15)#隐性等待
driver.get("https://www.baidu.com")

driver.find_element_by_id("index-kw").clear()
driver.find_element_by_id("index-kw").send_keys(u"飞猪")
driver.find_element_by_id("index-bn").click()
time.sleep(1)
driver.find_elements_by_partial_link_text(u'飞猪')[0].click()
driver.find_element_by_css_selector('#J_Page > article > header > div > div.searchbar__search___3oyby').click()
driver.find_element_by_css_selector("input.searchinput-input").clear()
driver.find_element_by_css_selector("input.searchinput-input").send_keys(u"千岛湖")
driver.find_element_by_css_selector("input.searchinput-input").send_keys(Keys.ENTER)
driver.find_element_by_css_selector('#app > div > div.search-result-ctn > div > div > div > div:nth-child(2) > div > div.h-bar-tabview > div > div.h-tabview-list > div > div > div > ul > li:nth-child(6) > span').click()
time.sleep(3)

driver.find_elements_by_css_selector('.product-list > div')[0].find_element_by_css_selector('a:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1)').click()