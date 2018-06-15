# -*- coding:utf-8 -*-

#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# options = webdriver.ChromeOptions()
# options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
#
# driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver',chrome_options=options)
# driver.maximize_window()
# driver.set_page_load_timeout(5)
# driver.get("http://h5.m.taobao.com/trip/hotel/searchlist/index.html?ttid=12bai0000004&e=kjRQGs7HnSlIGYWvs5y5E4AAksovHygfUR6Co5abHEPcEesopIDDZC_IAR7ok-np8sviUM61dt3AyMgUdz-fmZ4wgOgUxP9jBWqoyfzEffi-NCCc-lX3QU6j1QJSoFwkiiVicoq_k5dqE55nENphhtG5T7v9i6W7Wq_pVe8GRwxbWjXjFLUzDm3CCSTosozIBHHV38ohJK6uVjKj9BvATzhpiYA3a5n9&_preProjVer=1.0.11&_projVer=1.0.11&guid=1521010635587395982&cityName=%E5%8D%83%E5%B2%9B%E6%B9%96&cityCode=100017&adultNum=2&keyWords=%E5%8D%83%E5%B2%9B%E6%B9%96&recKeyword=undefined&checkIn=2018-03-14&checkOut=2018-03-15&isLBS=false&spm=181.7437877.1998398706.9")
# time.sleep(5)
# for i in range(50):
#     js = 'document.body.scrollTop = 10000'
#     # 就是这么简单，修改这个元素的scrollTop就可以
#     driver.execute_script(js)
#     time.sleep(1)

# "rpi-scroll-view.scroller-list"
print (lambda s:'可订今日票' if '可订今日票' in s else '')('可订今日票')