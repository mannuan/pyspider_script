# -*- coding:utf-8 -*-

from pyquery import PyQuery as py
import sys,os
from lxml import etree

with open('/home/mininet/content.html') as f:
    content = f.read().decode('utf-8')
    f.close()

p = py(content)
def Download_Pic(url,img_name):
    os.system('wget {} -T 10 -t 6 -O {}/{}'.format(url,os.environ['HOME'],img_name))
def GetPicname(url):
    return '/picture_hzz/'+url.replace('https://','').replace('http://','').replace('/','_').replace('.','-').split('?')[0]
def CreateEtree(next,root):
    if len(next.getchildren()) is not 0:
        for child in next.getchildren():
            p = etree.SubElement(root, 'p')
            CreateEtree(child,p)
    else:
        if next.tag == 'img':
            if next.attrib.get('src') is None:
                p = etree.SubElement(root, 'p')
                p.text = ' '
            elif next.attrib.get('src').find('http') == 0:#http在字符串的最前面
                img = etree.SubElement(root, 'img')
                img_url = next.attrib.get('src')
                img_name = GetPicname(img_url)
                img.attrib['src'] = img_name
                Download_Pic(img_url,img_name)
        else:
            p = etree.SubElement(root, 'p')
            p.text = (lambda x:' ' if x is None else x)(next.text)
text = ''
for each in p.contents():
    root = etree.Element('p')
    for child in each.getchildren():
        p = etree.Element('p')
        CreateEtree(child,p)
        root.append(p)
    text += etree.tostring(root,encoding='utf-8')
print(text)