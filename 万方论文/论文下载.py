host = "122.224.129.35"
port = 23306
user = "repository"
passwd = "repository"
db = 'repository'

from pyspider.libs.base_handler import *
import requests
import pymysql
import sys
import os


class Handler(BaseHandler):
    crawl_config = {
    }

    id = ""

    @every(minutes=24 * 60)
    def on_start(self):
        conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset='utf8')
        cur = conn.cursor()

        cur.execute("select * from wanfang where file_path is null limit 300");
        rows = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()

        for row in rows:
            self.crawl(row[6], callback=self.index_page,
                       save={'id': row[0], 'fileName': row[9][row[9].rindex('/') + 1:len(row[9])]})

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('a#doDownload').items():
            fileUrl = each.attr.href
            fileName = "/var/wanfang/" + response.save['fileName'] + ".pdf"
            rowId = response.save['id']
            # with request.urlopen(fileUrl) as web:
            #    with open(fileName , 'wb') as outfile:
            #        outfile.write(web.read())
            res = requests.get(fileUrl)
            res.raise_for_status()
            playFile = open(fileName, 'wb')
            for chunk in res.iter_content(100000):
                playFile.write(chunk)
            playFile.close()
            conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset='utf8')
            cur = conn.cursor()
            cur.execute("update wanfang set file_path = '%s' where id = %s" % (fileName, int(rowId)))
            conn.commit()
            cur.close()
            conn.close()

    @config(priority=2)
    def detail_page(self, response):
        return {
            "result": "ok"
        }