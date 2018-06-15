# -*- coding:utf-8 -*-

import time,random,re,sys,json
from util import *
from driver import *


driver = getChromeWebDriver()
try:
    driver.get("http://piao.qunar.com/ticket/list.htm?keyword=千岛湖&region=杭州&from=qunarindex&in_track=index_tab_search")
except Exception:
    for i in range(3):
        PageTimeout('driver.refresh()')
while(True):
    # getShopInfo(driver)
    try:
        driver.find_element_by_link_text(u'下一页').click()
    except Exception as e:
        print e
        break
driver.quit()