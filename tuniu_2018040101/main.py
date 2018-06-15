# -*- coding:utf-8 -*-

import time,random,re,sys,json
from util import *
from driver import *
import requests,json,sys
reload(sys)
sys.setdefaultencoding('utf8')
from pyquery import PyQuery as pq
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.command import Command

driver = getChromeMobileDriver()
print '进入途牛移动版主页...'
driver.get('https://m.tuniu.com/')
# print driver.switch_to_alert().text
# time.sleep(1)
# driver.find_element_by_css_selector('#index-kw').send_keys(u'飞猪')
# driver.find_element_by_css_selector('#index-bn').click()
# time.sleep(1)
# driver.find_elements_by_partial_link_text(u'飞猪')[0].click()
driver.find_element_by_css_selector('#J_header > div.m_header_bar.J_header-bar > div.mhb_center > div').click()
# time.sleep(1)
# driver.find_element_by_css_selector('#app > div > div > div.searchsuggestion-container > div.searchinput-theme-yellow.searchinput-container > form > div > div > input').send_keys(u'千岛湖')
# print '输入千岛湖...'
# driver.find_element_by_css_selector('#app > div > div > div.searchsuggestion-container > div.searchinput-theme-yellow.searchinput-container > form > div > div > input').send_keys(Keys.ENTER)
# print '搜索千岛湖...'
# driver.find_element_by_css_selector('#app > div > div.search-result-ctn > div > div > div > div:nth-child(2) > div > div.h-bar-tabview > div > div.h-tabview-list > div > div > div > ul > li:nth-child(6)').click()
# print '点击门票...'
#
# time.sleep(1)
# getShopInfo(driver)
# driver.quit()