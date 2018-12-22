# -*- coding: utf-8 -*-
#   File Name：     09local
#   Description :
#   Author :       zongyanzhang
#   date：          2018/12/22

from threading import Thread, local

# 是的多线程在使用全局的local绑定变量的时候局部化
lc = local()

def fun(s):
    lc.name = s

if __name__ == '__main__':
    lc.name = 'main'
    thr = Thread(target=fun, args=('python',))
    thr.start()
    thr.join()
    print(lc.name)

