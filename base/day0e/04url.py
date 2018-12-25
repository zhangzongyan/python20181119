# -*- coding: utf-8 -*-
#   File Name：     04url
#   Description :
#   Author :       zongyanzhang
#   date：          2018/12/25

import urllib.request
import re


# 打开并读取url
url = urllib.request.urlopen('https://movie.douban.com/')
print(url)

# 读取数据
data = url.read().decode()
# print(data)

res = re.findall(r'<img src="(.*?)" alt="神探狗笨吉"', data)
print(res)
