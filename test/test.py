# -*- coding:utf-8 -*-

import re
import json
import time
from pyquery import PyQuery as pq
import binascii
import os
with open('/home/mininet/题目.txt','r') as f:
    content = f.read()
content = "<div class=\"rich_media_content\">%s</div>" % content
content = re.sub(r' id=\".*?\"|id=\".*?\" |&#13;|[\f\n\r\t\v]*', '', content)  # 去除id
content = re.sub('[ ]{2,}', '', content)
img_list = re.findall(
    r'<(?=img)[^ </>\"]+[^<>]*[ ]+(?=src|data-src)[^ </>\"]+[ ]*=[ ]*?\"((?=https://|http://)[^ \"<>]+)?\"[^<>]*[/]{0,1}?>',
    content)
img_name_list = [re.sub(r'https:\/\/mmbiz.qpic.cn\/mmbiz_[\w]+\/', '', i) for i in
                 img_list]
img_name_list = [re.sub(r'\/640\?wx_fmt=', '_', i) for i in img_name_list]
for i in range(len(img_list)):
    content = content.replace(img_list[i], 'http://122.224.129.35:28080/picture_hzz/%s' % img_name_list[i])
    wget_img = 'wget %s -O %s/.picture_hzz/%s' % (img_list[i], os.environ['HOME'], img_name_list[i])
    os.system(wget_img)
print content