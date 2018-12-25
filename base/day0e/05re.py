# -*- coding: utf-8 -*-
#   File Name：     05re
#   Description :
#   Author :       zongyanzhang
#   date：          2018/12/25

import re

s = 'a href"=https://Book.douban\.com" booktarget="_blank"\\ \ndata-moreurl-dict=">读书</a>'
# 编译规则
cmp = re.compile(r'.{3,8}?')
# 得到与规则匹配的结果对象
res = cmp.match(s)
print(res.group(), res.start(), res.end(), res.span())

# 从头
res = re.match(r'[a-z]*', s)
print(res)

# 匹配整个字符串 re.S 使得.包括'\n', re.M多行模式
res = re.findall(r'^[a-z](.+)>$', s, re.S)
print(res)

res = re.finditer(r'[a-z]{2}', s)
print(res)

res = re.findall(r'Book|book', s)
print(res)

p = re.compile(r'\W+')
res = p.split('This is a test, short       and    sweet, of split().')
print(res)


