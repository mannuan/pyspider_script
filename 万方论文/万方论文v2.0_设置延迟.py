#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-11-21 16:41:40
# Project: wanfangv2.0

from pyspider.libs.base_handler import *
import time,pymysql,re,sys,random,requests,os
reload(sys)
sys.setdefaultencoding('utf-8')
from pyquery import PyQuery as pq


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

    search_key_list = ["河长制", "智慧治水", "水利厅", "污水治理", "一河一策", "一河一档", "水政执法", "水资源保护", "河湖水域岸线保护", "水污染防治", "污染源类型", "污染企业","水利工程管理", "环保督查", "环境改善", "河道治理", "河流治理", "水功能区", "污染源分布", "水生态修复", "水利工程管理", "环境改善", "水质监测","涉河水利工程","岸线规划", "污水治理", "水环境治理"]
    search_type_dict = {"TV":"水利工程", "TP":"自动化技术、计算机技术", "F":"经济", "P":"天文学、地球科学", "D":"政治、法律"}

    context_css = "<link rel=\"stylesheet\" type=\"text/css\" href=\"css/articleDetail.css\"><link rel=\"stylesheet\" type=\"text/css\" href=\"css/bootstrap.css\"><link rel=\"stylesheet\" type=\"text/css\" href=\"css/font-awesome.min.css\">"
    context_html_tmp = "<article class=\"entry\"><div class=\"entry__article\">{}</div></article>"

    @every(minutes=24 * 60)
    def on_start(self):
        for key in self.search_key_list:
            for type in self.search_type_dict.keys():
                for p in range(1, 50):
                    url = 'http://www.wanfangdata.com.cn/search/searchList.do?searchType=perio&pageSize=50&page={}&searchWord={}&facetField=$subject_classcode_level:∷/{}&facetName={}:$subject_classcode_level&showType=detail&firstAuthor=false&rangeParame=all'.format(p,key,type,self.search_type_dict.get(type))
                    self.crawl(url, fetch_type='js', callback=self.index_page, exetime=time.time() + random.randint(60 * 60, 12 * 60 * 60))

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc("#here > div.right_con > div.ResultBlock > div > div.ResultCont > div.title > a:nth-child(3)").items():
            self.crawl(each.attr.href, fetch_type='js', callback=self.detail_page, exetime=time.time() + random.randint(60 * 60, 12 * 60 * 60))

    def download_file(self, url, filename):
        p = pq(url)
        url_tail = p('#doDownload').attr.href
        if url_tail is None:
            return ''
        fileurl = 'http://f.wanfangdata.com.cn/' + url_tail
        filename = "/var/wanfang/{}.pdf".format(filename)
        res = requests.get(fileurl)
        with open(filename, 'wb+') as f:
            for chunk in res.iter_content(100000):
                f.write(chunk)
            f.close()
        return filename

    @config(priority=2)
    def detail_page(self, response):
        result = {}
        context = self.context_css
        text = ''
        for each in response.doc('#div_a > div > div.left_con > div.left_con_top > ul > li').items():
            if '作者：' in each('div.info_left').text():
                pass
            elif '关键词：' in each('div.info_left').text():
                pass
            elif '在线出版日期：' in each('div.info_left').text():
                pass
            else:
                text += "<p>{}</p>".format(each('div.info_left').text()+each('div.info_right').text())
        context+=self.context_html_tmp.format(text)
        result["context"] = re.sub('[\f\n\r]+','',context)
        #####################################
        result["url"] = response.url
        result["title"] = response.doc('#div_a > div > div.left_con > div.left_con_top > div.title').text().split(' ')[0]+' '+response.doc('#div_a > div > div.left_con > div.left_con_top > div.English').text()
        result["abstract"] = response.doc('#see_alldiv').text().replace('摘要 ： ','')
        result["spider_time"] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 爬虫的时间
        ######################################
        result["author"] = ''
        result["unit"] = ''
        result["magezine"] = ''
        result["time"] = ''
        for each in response.doc('#div_a > div > div.left_con > div.left_con_top > ul > li').items():
            if '作者：' in each('div.info_left').text():
                result["author"] = each('div.info_right').text()
            elif '作者单位：' in each('div.info_left').text():
                result["unit"] = each('div.info_right').text()
            elif '刊名：' in each('div.info_left').text():
                result["magezine"] = each('div.info_right').text()
            elif '关键词：' in each('div.info_left').text():
                result["keyword"] = each('div.info_right').text()
            elif '在线出版日期：' in each('div.info_left').text():
                result["time"] = each('div.info_right').text()
        result["file_url"] = ''
        result["file_path"] = ''
        ######################################
        if response.doc('#ddownb').text() is not None:
            result["file_url"] = 'http://f.wanfangdata.com.cn/download/Periodical_{}.aspx'.format(response.url.split('=')[-1])
            result["file_path"] = ''
            #文件下载,放在公司服务器只需要注释下面一行
            result["file_path"] = self.download_file(result["file_url"],response.url.split('=')[-1])
        ###################################
        return result

    def on_result(self, result):
        if not result or not result['title']:
            return
        conn = pymysql.connect(host="127.0.0.1", port=3306, user="repository", passwd="repository", db="repository", charset='utf8')
        cur = conn.cursor()

        # 先查找是否存在
        cur.execute("select * from wanfang where title = %s", result["title"])
        rows = cur.fetchall()
        if len(rows) == 0:
            cur.execute(
                "insert into wanfang(title,abstract,author,unit,magezine,file_url,file_path,time,keyword,url,spider_time,context) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (result["title"], result["abstract"], result["author"], result["unit"], result["magezine"],
                 result["file_url"],result["file_path"], result["time"], result["keyword"], result["url"], result["spider_time"],result["context"]))
        else:
            cur.execute(
                "update wanfang set title=%s,abstract=%s,author=%s,unit=%s,magezine=%s,file_url=%s,file_path=%s,time=%s,keyword=%s,spider_time=%s,context=%s where url=%s",
                (result["title"], result["abstract"], result["author"], result["unit"], result["magezine"],result["file_url"],result["file_path"], result["time"], result["keyword"], result["spider_time"],result["context"],result["url"]))
        conn.commit()
        cur.close()
        conn.close()