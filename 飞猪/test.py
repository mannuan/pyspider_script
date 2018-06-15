# -*- coding:utf-8 -*-

from pyquery import PyQuery as pq
import sys
reload(sys)
sys.setdefaultencoding('utf8')

with open('/home/mininet/桌面/飞猪_千岛湖.html','r') as f:
    html_content = f.read()
p = pq(html_content)
p('script').remove()
p('style').remove()
p('link').remove()
p('img').remove()
with open('/home/mininet/桌面/飞猪_千岛湖_clean.html','w+') as f:
    f.write(p.html(method='html'))