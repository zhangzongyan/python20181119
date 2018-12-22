# -*- coding: utf-8 -*-
#   File Name：     08thread
#   Description :
#   Author :       zongyanzhang
#   date：          2018/12/22

from threading import Thread, Lock
import time


lock = Lock() # 保护互斥量
n = 100 # 多线程发成竞争的那段代码就是互斥量

def thr_job():
    print('the new thread is running....')
    global n
    lock.acquire()
    n = 200
    lock.release()
    time.sleep(3)


if __name__ == '__main__':
    # 创建线程
    thr = Thread(target=thr_job, name='不一样', daemon=True)
    thr.start()
    print(thr.name, thr.ident)
    # 加锁
    lock.acquire()
    print(n)
    time.sleep(2)
    print(n + 10)
    # 解锁
    lock.release()
    thr.join()

