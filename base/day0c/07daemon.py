# -*- coding: utf-8 -*-
#   File Name：     07daemon
#   Description :
#   Author :       zongyanzhang
#   date：          2018/12/22

from multiprocessing import Process
import time


def job():
    while True:
        print('hello')
        time.sleep(1)


if __name__ == '__main__':
    pro = Process(target=job)
    pro.start()
