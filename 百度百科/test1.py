#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 22:49:57 2018

@author: mannuan
"""
import os
from pyquery import PyQuery
p=os.popen('curl https://wapbaike.baidu.com/item/%E4%BA%AC%E6%9D%AD%E5%A4%A7%E8%BF%90%E6%B2%B3?wpf=3\&ldr=1\&page=8')
print p.read()
p.close()
import sys
sys.argv[1]

