# -*- coding: utf-8 -*-
#   File Name：     myio2
#   Description :
#   Author :       zongyanzhang
#   date：          2018/12/19

import io

with open('text', mode='r+b') as f:
    line = f.readlines(1)
    print(line)
    print(f.tell())
    '''
    # seek设置文件偏移量的时候:如果文件的打开方式是t，则只允许在SEEK_SET位置设置偏移量
    # 如果是b的方式打开则，SEEK_SET/SEEK_CUR/SEEK_END都允许
    f.seek(14, io.SEEK_SET)
    f.seek(1, io.SEEK_CUR)
    '''
    f.seek(-4, io.SEEK_END)
    l = [b'python', b'guido']
    f.writelines(l)

