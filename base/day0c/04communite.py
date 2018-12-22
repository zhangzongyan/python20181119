# -*- coding: utf-8 -*-
#   File Name：     04communite
#   Description :
#   Author :       zongyanzhang
#   date：          2018/12/22

from multiprocessing import Process, Pipe
import time

# 发送
def pro1(args):
    for i in range(10):
        # 向管道发送数据
        args.send(i)
        time.sleep(1)
    args.close()


def pro2(args):
    while True:
        # 从管道接收数据
        r = args.recv()
        print('from pro1:%d' % r)


if __name__ == '__main__':
    # 管道的创建，得到管道的两端
    conn1, conn2 = Pipe()

    obj1 = Process(target=pro1, args=(conn1,))
    obj2 = Process(target=pro2, args=(conn2,))

    obj1.start()
    obj2.start()

    obj1.join()
    obj2.join()

