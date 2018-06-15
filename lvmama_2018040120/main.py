# -*- coding:utf-8 -*-

import time,random,re,sys,json
from util import *
from driver import *
import requests,json,sys
from pyquery import PyQuery as pq
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.command import Command

driver = getChromeHeaderlessMobileDriver()
print('进入驴妈妈移动版主页...')
driver.get('https://m.lvmama.com')
time.sleep(3)
driver.find_element_by_css_selector('#content > div.index-header > a.search.cmAddClick > p').click()
time.sleep(1)
driver.find_element_by_css_selector('#keyword').send_keys(u'千岛湖')
print('输入千岛湖...')
driver.find_element_by_css_selector('#keyword').send_keys(Keys.ENTER)
print('搜索千岛湖...')
time.sleep(1)
driver.find_element_by_css_selector('#tab_ticket > a').click()
print('点击景点门票...')
time.sleep(3)
# while(True):
for i in range(200):
    ActionChains(driver).move_to_element(
        driver.find_element_by_css_selector('body > div.headBlank > div.headFixed > div > nav > div')).send_keys(Keys.ARROW_DOWN).perform()
    # try:
    #     driver.find_element_by_css_selector('#ticket_nomore')
    #     break
    # except Exception:
    #     pass
getShopInfo(driver)
driver.quit()