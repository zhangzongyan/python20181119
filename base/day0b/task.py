# -*- coding: utf-8 -*-
#   File Name：     task
#   Description :
#   Author :       zongyanzhang
#   date：          2018/12/19

'''
1. 实现一个cp功能
    python xxx.py error.py hello 每一次读不超过10个字节
'''

import sys, time


def mycp(src, dest):
    with open(src, encoding='utf-8') as rf:
        with open(dest, mode='w', encoding='utf-8') as wf:
            while True:
                data = rf.read(10)
                # print(data)
                # time.sleep(1)
                if data == '':
                    # 读到文件终止标志
                    break
                wf.write(data)


# print(sys.argv)
if len(sys.argv) >= 3:
    mycp(sys.argv[1], sys.argv[2])

