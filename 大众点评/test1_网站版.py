#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2018-03-17 09:57:13
# Project: 20180317095711

from pyspider.libs.base_handler import *


class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('https://m.dianping.com/shoplist/3602/search?from=m_search&keyword=%E5%8D%83%E5%B2%9B%E6%B9%96', fetch_type='js', callback=self.index_page, js_script='''
                   window.scrollTo(0,document.body.scrollHeight);
               ''')

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('#app > div > div.J_searchList > ul > li > a').items():
            self.crawl(each.attr.href, callback=self.detail_page)
            # print each.attr.href

    @config(priority=2)
    def detail_page(self, response):
        return {
            "url": response.url,
            "title": response.doc('title').text(),
        }
