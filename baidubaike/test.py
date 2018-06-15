# -*- coding:utf-8 -*-
import re
bold = re.compile(r'\*{2}(.*?)\*{2}')
text = 'Make this **cai**. This **junsheng**.'
print('Text:', text)
print('Bold:', bold.sub(r'<b>\1</b>', text))
