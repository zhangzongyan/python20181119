# -*- coding: utf-8 -*-
#   File Name：     hw
#   Description :
#   Author :       zongyanzhang
#   date：          2018/12/24

from threading import Thread, Lock
import threading

lock = Lock()
num = 0


def isprimer(n):
    flag = True
    for i in range(2, n):
        if n % i == 0:
            flag = False
            break
    return flag


def job():
    global num
    while True:
        lock.acquire()
        while num == 0:
            lock.release()
            lock.acquire()
        if num == -1:
            lock.release()
            break
        n = num
        num = 0
        lock.release()
        if isprimer(n):
            print('[{}]:{} is a primer'.format(threading.current_thread().name, n))


if __name__ == '__main__':
    thrlist = []

    for i in range(4):
        thrlist.append(Thread(target=job))
        thrlist[i].start()

    # 发放任务
    for i in range(200, 301):
        lock.acquire()
        while num != 0:
            lock.release()
            lock.acquire()
        num = i
        lock.release()

    lock.acquire()
    while num != 0:
        lock.release()
        lock.acquire()
    num = -1
    lock.release()

    for i in range(4):
        thrlist[i].join()





