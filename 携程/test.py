#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2018-03-07 17:10:26
# Project: test

from pyspider.libs.base_handler import *


class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('http://m.ctrip.com/webapp/hotel/city1332/?ulocation=29.6045894622803_119.034812927246_千岛湖',fetch_type='js', callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        # for each in response.doc('a[href^="http"]').items():
        #     self.crawl(each.attr.href, callback=self.detail_page)
        # print response.doc('#useCasKey').val()
        with open('temp.txt','w+') as f:
            f.write(response.text)

    @config(priority=2)
    def detail_page(self, response):
        return {
            "url": response.url,
            "title": response.doc('title').text(),
        }