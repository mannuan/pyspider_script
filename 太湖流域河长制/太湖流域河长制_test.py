#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-12-25 15:24:21
# Project: test8

from pyspider.libs.base_handler import *
import os


class Handler(BaseHandler):
    crawl_config = {
        "headers":{
        "Proxy-Connection": "keep-alive",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13C75 Safari/601.1',
        "Accept": "*/*",
        "DNT": "1",
        "Accept-Encoding": "gzip, deflate, sdch",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4",
    }
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('http://www.tba.gov.cn//tba/content/TBA/xwzx/jczt/hcz/mtbg/0000000000013024.html', fetch_type='js', callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        text = ''
        for each in response.doc('#print > tbody > tr:nth-child(5) > td > table > tbody > tr > td').items('p'):
            img_url = each('img').attr.src
            if img_url is not None:
                img_name = img_url.replace('http://','').replace('https://','').replace('/','_')
                img_tail = '.'+img_name.split('.')[-1]
                img_head = img_name.replace(img_tail,'').replace('.','-')
                img_name = img_head+img_tail
                server_path = '/picture_hzz/'+img_name
                local_path = os.environ['HOME']+'/.picture_hzz/'+img_name
                print local_path
                os.system('wget {} -O {}'.format(img_url,local_path))
                part = "<p><img src={}></p>".format(server_path)#为了显示图片更加清楚把img标签加入p标签里面
            else:
                part = '<p>{}</p>'.format(each.text())
                part = part.replace('\'','\\\'').replace('\"','\\\"')
            text+=part
        print text

    @config(priority=2)
    def detail_page(self, response):
        return {
            "url": response.url,
            "title": response.doc('title').text(),
        }