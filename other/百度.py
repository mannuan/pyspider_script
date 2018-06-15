host = "127.0.0.1"
port = 3306
user = "repository"
passwd = "repository"
db = 'repository'
filter_words = ["广告", "咨询", "百度图片", "公司", "ppt"]
key_words = ["环境", "污水", "河长", "水利", "政策"]

from pyspider.libs.base_handler import *
import datetime
import time
import json
import pymysql
import sys


class Handler(BaseHandler):
    crawl_config = {
        "headers": {
            "Proxy-Connection": "keep-alive",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36",
            "Accept": "*/*",
            "DNT": "1",
            "Accept-Encoding": "gzip, deflate, sdch",
            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4",
        }
    }

    @every(minutes=24 * 60 * 10)
    def on_start(self):
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='repository', passwd='repository', db='repository',
                               charset='utf8')
        cur = conn.cursor()
        cur.execute("select * from key_word")
        rows = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        for each in rows:
            url = "https://www.baidu.com/s?wd=" + each[1]
            self.crawl(url, callback=self.baidu_page, save={"page": 1})

    @config(age=5 * 24 * 60 * 60)
    def baidu_page(self, response):
        # 先获取到所有的链接
        time.sleep(2)
        for each_div in response.doc("DIV#content_left>DIV").items():
            text_base_info = each_div.text()
            if filter(text_base_info) == 1:
                self.crawl(each_div('h3>a').attr.href, callback=self.index_page,
                           save={"title": each_div('h3>a').text()})

        for each_a in response.doc("DIV#page>a").items():
            if each_a.text().find("下一页") != -1:
                page_num = response.save['page']
                if int(page_num) < 5:
                    page_num = page_num + 1
                    self.crawl(each_a.attr.href, callback=self.baidu_page, save={"page": page_num})

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        self.crawl(response.url, callback=self.detail_page, save={"title": response.save["title"]})

        for each_a in response.doc("a").items():
            if filter(each_a.text()) == 1 and keyFilter(each_a.text()) == 1:
                self.crawl(each_a.attr.href, callback=self.index_page, save={"title": each_a.text()})

    @config(age=10 * 24 * 60 * 60)
    def detail_page(self, response):
        result = {
            "url": response.url,
            "title": response.save['title'],
            "text_info": response.doc("body").text()
        }
        html = "<html><head><meta http-equiv='Content-Type' content='text/html;charset=utf-8'><base href='" + response.url + "'></head><body><div style='position:relative'>"
        html += response.doc("HEAD").html()
        html += response.doc("BODY").html()
        html += "</div></body></html>"
        result["html"] = html
        return result

    def on_result(self, result):
        if not result or not result["title"]:
            return

        conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset='utf8')
        cur = conn.cursor()
        cur.execute("select * from baidu where url = %s", result["url"])
        rows = cur.fetchall()
        if len(rows) == 0:
            cur.execute("select count(*) from baidu");
            row = cur.fetchone()
            num = int(row[0]) + 1
            file_path = "/home/quick_picture/" + str(num) + ".html"
            file = open(file_path, "wt")
            file.write(result["html"])
            file.close()

            cur.execute("insert into baidu(url,title,text_info,quick_picture_file) values(%s,%s,%s,%s)",
                        (result["url"], result["title"], result["text_info"], file_path))
        conn.commit()
        cur.close()
        conn.close()


def filter(text):
    for word in filter_words:
        x = text.find(word)
        if x != -1:
            return 0
    return 1


def keyFilter(text):
    for word in key_words:
        x = text.find(word)
        if x != -1:
            return 1
    return 0