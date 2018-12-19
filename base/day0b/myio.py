# -*- coding: utf-8 -*-
#   File Name：     myio
#   Description :
#   Author :       zongyanzhang
#   date：          2018/12/19

'''
文件io
'''
import sys, time

# 打开
fd = open(r'E:\python1119\day0b\text', mode='w+', encoding='utf-8')

fd.write('hello\n')
fd.flush()
time.sleep(100)
# 改变文件的偏移量
fd.seek(0, 0)
read_data = fd.read(10)

fd.close()

print(read_data)

'''
文件的缓存三种方式
    行缓存: stdout stdin
    全缓存: 文件
    无缓存: stderr
'''

print('hungry', end='')
sys.stdout.flush() # 强制刷新文件的缓存区
while True:
    pass

