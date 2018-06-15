# -*- coding:utf-8 -*-

import time,random,re,sys,json
from util import *
from driver import *


driver = getChromeHeaderlessWebDriver()
try:
    driver.get("http://www.mafengwo.cn/search/s.php?q=千岛湖&t=poi&seid=8091BF5D-D163-4C69-80B9-083323DA4DE9&mxid=&mid=&mname=&kt=1")
except Exception:
    for i in range(3):
        PageTimeout('driver.refresh()')
while(True):
    getShopInfo(driver)
    try:
        driver.find_element_by_link_text(u'下一页').click()
    except Exception as e:
        print e
        break
driver.quit()