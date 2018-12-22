# -*- coding: utf-8 -*-
#   File Name：     05queue
#   Description :
#   Author :       zongyanzhang
#   date：          2018/12/22

from multiprocessing import Process, Queue
import time

# 发送
def pro1(que):
    for i in range(10):
        # 向队列中写入
        que.put(i)
        time.sleep(2)


def pro2(que):
    while True:
        print('from que get:{}'.format(que.get()))


if __name__ == '__main__':
    # 创建队列
    q = Queue()

    obj1 = Process(target=pro1, args=(q,))
    obj2 = Process(target=pro2, args=(q,))

    obj1.start()
    obj2.start()

    obj1.join()
    obj2.join()

