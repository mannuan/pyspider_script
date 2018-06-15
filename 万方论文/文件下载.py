#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-11-21 16:41:40
# Project: 文件下载

from pyspider.libs.base_handler import *
import requests


class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('http://f.wanfangdata.com.cn/download/Periodical_zhonggsl201702007.aspx',callback=self.index_page,save={'filename': 'zhonggsl201702007.pdf'})

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        fileurl = response.doc('#doDownload').attr.href
        print fileurl
        filename = "/home/mininet/" + response.save['filename']
        res = requests.get(fileurl)
        # res.raise_for_status()
        with open(filename, 'wb+') as f:
            for chunk in res.iter_content(100000):
                f.write(chunk)
            f.close()

    @config(priority=2)
    def detail_page(self, response):
        return {
            "result": "ok"
        }