# -*- coding:utf-8 -*-

import re,sys

def regex(str):
    result = ''
    if re.sub(r'^::/128$|^([0]{4}:){7}[0]{4}$',r'Unspecified',str) == 'Unspecified':
        result = 'Unspecified'
    elif re.sub(r'^::1/128$|^([0]{4}:){7}[0]{3}1$',r'Loopback',str) == 'Loopback':
        result = 'Loopback'
    elif re.sub(r'^FE80::/10$|^FE[89AB]{1}[0-9A-F]{1}(:[0-9A-F]{4}){6}:[0-9A-F]{4}$',r'LinkLocal',str) == 'LinkLocal':
        result = 'LinkLocal'
    elif re.sub(r'^FEC0::/10$|^FE[CDEF]{1}[0-9A-F]{1}(:[0-9A-F]{4}){6}:[0-9A-F]{4}$',r'SiteLocal',str) == 'SiteLocal':
        result = 'SiteLocal'
    elif re.sub(r'^FF00::/10$|^FF[0-9A-F]{2}(:[0-9A-F]{4}){6}:[0-9A-F]{4}$',r'Multicast',str) == 'Multicast':
        result = 'Multicast'
    elif re.sub(r'^([0-9A-F]{4}:){7}[0-9A-F]{4}$',r'Globalcast',str) == 'Globalcast':
        result = 'Globalcast'
    else:
        result = 'Error'
    return result
str = sys.stdin.readline().strip()
print regex(str)