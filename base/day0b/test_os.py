# -*- coding: utf-8 -*-
#   File Name：     test_os
#   Description :
#   Author :       zongyanzhang
#   date：          2018/12/19

import os.path
import os

# 分离文件的后缀
res = os.path.splitext(r'E:\python1119\day0b\error')
print(res)

# 获取给定路径下所有.py文件
l = [x for x in os.listdir(r'E:\python1119\day0b') \
 if os.path.exists(x) and os.path.splitext(x)[1]=='.py']

print(l)

# 获取给定路径下所有文件类型为目录的文件
l = [x for x in os.listdir(r'E:\python1119\day0b') \
  if os.path.isdir(x)]
print(l)

# 绝对路径
print(os.path.abspath('.'))






