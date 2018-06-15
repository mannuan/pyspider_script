host = "127.0.0.1"
port = 3306
user = "repository"
passwd = "repository"
db = 'repository'

from pyspider.libs.base_handler import *
import datetime
import time
import json
import pymysql


class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60 * 10)
    def on_start(self):
        conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset='utf8')
        cur = conn.cursor()
        cur.execute("select * from weixin_public")
        rows = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        for row in rows:
            url = "http://weixin.sogou.com/weixin?type=1&s_from=input&query=" + row[1] + "&ie=utf8&_sug_=n&_sug_type_="
            self.crawl(url, callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('UL.news-list2>LI:nth-child(1)>DIV.gzh-box2>DIV.txt-box>P.tit>a').items():
            self.crawl(each.attr.href, callback=self.list_page)

    @config(priority=3)
    def list_page(self, response):
        time.sleep(10)
        scriptStr = response.doc('body').text()
        if scriptStr.find("msgList", 1) != -1:
            start = scriptStr.find("msgList", 1) + 10
            end = len(scriptStr) - 42
            msg = json.loads(scriptStr[start:end])
            for each in msg["list"]:
                url = each["app_msg_ext_info"]["content_url"]
                url = url.replace("amp;", "")
                self.crawl("https://mp.weixin.qq.com" + url, callback=self.detail_page)

    @config(priority=2)
    def detail_page(self, response):
        result = {
            "title": response.doc('#activity-name').text(),
            "time": response.doc('#post-date').text(),
            "public_signal": response.doc('span.rich_media_meta.rich_media_meta_text.rich_media_meta_nickname').text(),
            "main_body": response.doc('div#js_content').text(),
            "spider_time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            "url": response.url,
        }
        return result

    def on_result(self, result):
        if not result or not result['title']:
            return
        conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset='utf8')
        cur = conn.cursor()

        # 先查找是否存在
        cur.execute("select * from weixin_info where title = %s", result["title"])
        rows = cur.fetchall()
        if len(rows) == 0:
            cur.execute(
                "insert into weixin_info(title,time,public_name,main_body,spider_time,url) values(%s,%s,%s,%s,%s,%s)", (
                result["title"], result["time"], result["public_signal"], result["main_body"], result["spider_time"],
                result["url"]))
        conn.commit()
        cur.close()
        conn.close()