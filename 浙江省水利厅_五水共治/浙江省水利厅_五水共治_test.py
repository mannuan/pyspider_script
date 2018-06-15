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
        self.crawl('http://www.zjwater.com/pages/document/123/document_942.htm', fetch_type='js', callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        selectors = [('#NewsContent','p','img'),('#NewsContent > p:nth-child(2) > table > tbody > tr:nth-child(4) > td','p','img'),('#NewsContent > table > tbody > tr:nth-child(3) > td','p','img')]
        text = ''
        for (selector1, selector2, selector3) in selectors:
            for each in response.doc(selector1).items(selector2):
                img_url = each(selector3).attr.src
                if img_url is not None:
                    img_url_tmp = img_url.split('?')[0]  # 去除url后面的参数部分
                    img_name = img_url_tmp.replace('http://', '').replace('https://', '').replace('/', '_')
                    img_tail = '.' + img_name.split('.')[-1]
                    img_head = img_name.replace(img_tail, '').replace('.', '-')
                    img_name = img_head + img_tail
                    server_path = '/picture_hzz/' + img_name
                    local_path = os.environ['HOME'] + '/.picture_hzz/' + img_name
                    os.system('wget {} -O {}'.format(img_url, local_path))
                    part = "<p><img src={}></p>".format(server_path)  # 为了显示图片更加清楚把img标签加入p标签里面
                else:
                    part = '<p>{}</p>'.format(each.text())
                    part = part.replace('\'', '\\\'').replace('\"', '\\\"')
                text += part
            if text.replace(' ', '').replace('　', '').replace('\n', '').replace('\r', '') != '':
                break
        print text
        file_url = None
        file_name = None
        for selector in selectors:
            for each in response.doc(selector[0]).items(selector[1]):
                file_url = each('a').attr.href
                if file_url is not None:
                    file_url_tmp = file_url.split('?')[0]  # 去除url后面的参数部分
                    file = file_url_tmp.replace('http://', '').replace('https://', '').replace('/', '_')
                    file_tail = '.' + file.split('.')[-1]
                    file_head = file.replace(file_tail, '').replace('.', '-')
                    file = file_head + file_tail
                    server_path = '/document_hzz/' + file
                    local_path = os.environ['HOME'] + '/.document_hzz/' + file
                    os.system('wget {} -O {}'.format(file_url, local_path))
                    file_name = server_path
                else:
                    file_name = ''
        print file_url,file_name

    @config(priority=2)
    def detail_page(self, response):
        return {
            "url": response.url,
            "title": response.doc('title').text(),
        }