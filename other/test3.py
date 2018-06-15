#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-12-29 20:30:17
# Project: 20171229203015

from pyspider.libs.base_handler import *


class Handler(BaseHandler):
    crawl_config = {
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
        'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('http://mp.weixin.qq.com/s?timestamp=1514599465&src=3&ver=1&signature=lnI*JA95chL8RkecUITurw6sb*n3hmTupWkOPu7eNgNuGhO-TIQ8JV1bthslEA1UAT6PDFQmcgjuNVzx68UB5D6m2nHwtfol6S*GTMM5eLawXwAoN6QEj7JjJ5dhw5IjyixM4Oe6ykYawvRwsjpWKLLEP9crH4GG*5C7lACM-uk=', fetch_type='js', callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        content = response.doc('#js_content').html().strip()
        with open('/home/mininet/content.html','w+') as f:
            f.write(content)
            f.close()
        print(content)

    @config(priority=2)
    def detail_page(self, response):
        return {
            "url": response.url,
            "title": response.doc('title').text(),
        }