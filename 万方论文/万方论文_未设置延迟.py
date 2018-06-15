#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-11-21 16:41:40
# Project: wanfang

key_words = ["河长制", "智慧治水", "水利厅", "污水治理", "一河一策", "一河一档", "水政执法", "水资源保护", "河湖水域岸线保护", "水污染防治", "污染源类型", "污染企业",
             "水利工程管理", "环保督查", "环境改善", "河道治理", "河流治理", "水功能区", "污染源分布", "水生态修复", "水利工程管理", "环境改善", "水质监测", "涉河水利工程",
             "岸线规划", "污水治理", "水环境治理"]
type_id = ["TV*", "TP*", "F*", "P*", "D*"]

from pyspider.libs.base_handler import *
import time,pymysql,re,sys,random


class Handler(BaseHandler):
    crawl_config = {
    }

    context_css = "<style type=\"text/css\">.fixed-width{width:1170px;margin:0 auto}.clear{zoom:1}div{display:block}body{font:12px/1.5 helvetica,arial,'Hiragino Sans GB',sans-serif;font-size:14px;background-color:#fff}.clear:after{display:block;clear:both;content:\"\";visibility:hidden;height:0}.section-baseinfo{font-size:12px;width:1170px;padding:18px 0 8px 0;color:#65686f;float:left}.section-baseinfo .abstract{margin-top:12px;line-height:28px}.abstract .zh .pre{float:left;width:40px;cursor:text}.abstract .zh .text{float:left;width:1130px;display:block}.fixed-width-wrap-feild .baseinfo-feild .row{zoom:1}.fixed-width-wrap-feild .baseinfo-feild{font-size:12px;line-height:28px;margin-top:12px;color:#65686f}.fixed-width-wrap-feild .baseinfo-feild .row .pre{width:92px;display:inline-block;font-weight:700;float:left}.fixed-width-wrap-feild .baseinfo-feild .row:after{display:block;clear:both;content:\"\";visibility:hidden;height:0}.fixed-width-wrap-feild .baseinfo-feild .row .text{float:left;display:inline-block;width:1068px}</style>"

    context_html_tmp = "<div class=\"fixed-width baseinfo clear\"><div class=\"section-baseinfo\"><h1>{}</h1><div class=\"baseinfo-feild abstract\"><div class=\"row clear zh\"><div class=\"pre \"><span>摘要：</span></div><div class=\"text\">{}</div></div></div></div></div>{}"

    @every(minutes=24 * 60)
    def on_start(self):
        for key in key_words:
            for typeId in type_id:
                for i in range(1, 50):
                    url = 'http://s.wanfangdata.com.cn/Paper.aspx?q=' + key + '+分类号%3a%22' + typeId + '%22&p=' + str(i)
                    self.crawl(url, fetch_type='js', callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc("body > div.content.content-search.clear > div.right > div.record-item-list > div.record-item > div.left-record > div.record-title > a.title").items():
            self.crawl(each.attr.href, fetch_type='js', callback=self.detail_page)

    @config(priority=6)
    def detail_page(self, response):
        result = {}
        title_tmp = response.doc('body > div.fixed-width.baseinfo.clear > div > h1').text()
        abstract_tmp = response.doc('body > div.fixed-width.baseinfo.clear > div > div.baseinfo-feild.abstract > div > div.text').text()
        tail_tmp = response.doc('body > div.fixed-width-wrap.fixed-width-wrap-feild').html()
        tail_tmp = re.sub('[\f\n\r\t\v]+','',tail_tmp)
        tail_tmp = re.sub('[ ]*&#13;[ ]*','',tail_tmp)
        context = self.context_css+self.context_html_tmp.format(title_tmp,abstract_tmp,tail_tmp)
        result["context"] = context
        result["url"] = response.url
        result["title"] = response.doc('HTML>BODY>DIV.fixed-width.baseinfo.clear>DIV.section-baseinfo>h1').text()
        result["abstract"] = response.doc(
            'HTML>BODY>DIV.fixed-width.baseinfo.clear>DIV.section-baseinfo>DIV.baseinfo-feild.abstract>DIV.row.clear.zh>DIV.text').text()
        result["author"] = response.doc(
            'HTML>BODY>DIV.fixed-width-wrap.fixed-width-wrap-feild>DIV.fixed-width.baseinfo-feild>DIV.row.row-author>SPAN.text').text()
        result["magezine"] = response.doc(
            'HTML>BODY>DIV.fixed-width-wrap.fixed-width-wrap-feild>DIV.fixed-width.baseinfo-feild>DIV.row.row-magazineName>SPAN.text').text()
        result["file_url"] = ''.join(x.attr.href for x in response.doc(
            'HTML>BODY>DIV.fixed-width.baseinfo.clear>DIV.section-baseinfo>DIV.record-action-link.clear>A.download').items())
        result["keyword"] = response.doc(
            'HTML>BODY>DIV.fixed-width-wrap.fixed-width-wrap-feild>DIV.fixed-width.baseinfo-feild>DIV.row.row-keyword>SPAN.text').text()
        result["spider_time"] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))#爬虫的时间
        result["unit"] = ""
        result["time"] = ""
        for i in range(0, 12):
            title = response.doc(
                'HTML>BODY>DIV.fixed-width-wrap.fixed-width-wrap-feild>DIV.fixed-width.baseinfo-feild>DIV:nth-child(' + str(
                    i) + ')>SPAN.pre').text()
            if title == "作者单位：":
                result["unit"] = response.doc(
                    'HTML>BODY>DIV.fixed-width-wrap.fixed-width-wrap-feild>DIV.fixed-width.baseinfo-feild>DIV:nth-child(' + str(
                        i) + ')>SPAN.text').text()
            if title == "在线出版日期：":
                result["time"] = response.doc(
                    'HTML>BODY>DIV.fixed-width-wrap.fixed-width-wrap-feild>DIV.fixed-width.baseinfo-feild>DIV:nth-child(' + str(
                        i) + ')>SPAN.text').text()
        return result

    def on_result(self, result):
        if not result or not result['title']:
            return
        conn = pymysql.connect(host="127.0.0.1", port=3306, user="repository", passwd="repository", db="repository", charset='utf8')
        cur = conn.cursor()

        # 先查找是否存在
        cur.execute("select * from wanfangnew where url = %s", result["url"])
        rows = cur.fetchall()
        if len(rows) == 0:
            cur.execute(
                "insert into wanfang(title,abstract,author,unit,magezine,file_url,time,keyword,url,spider_time,context) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (result["title"], result["abstract"], result["author"], result["unit"], result["magezine"],
                 result["file_url"], result["time"], result["keyword"], result["url"], result["spider_time"],result["context"]))
        else:
            cur.execute(
                "update wanfang set title=%s,abstract=%s,author=%s,unit=%s,magezine=%s,file_url=%s,time=%s,keyword=%s,spider_time=%s,context=%s where url=%s",
                (result["title"], result["abstract"], result["author"], result["unit"], result["magezine"],result["file_url"], result["time"], result["keyword"], result["spider_time"],result["context"],result["url"]))
        conn.commit()
        cur.close()
        conn.close()