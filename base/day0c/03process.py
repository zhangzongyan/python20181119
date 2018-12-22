# -*- coding: utf-8 -*-
#   File Name：     03process
#   Description :
#   Author :       zongyanzhang
#   date：          2018/12/22

from multiprocessing import Process
import time

n = 100


def pro_test(arg):
    print('running argument is %s' % arg)
    global n
    n += 1
    print('n的地址:{}, n:{}'.format(id(n), n))
    time.sleep(1)


def pro2_test():
    global n
    print('n的地址:{}, n:{}'.format(id(n), n))
    print('n:%d' % n)
    print('''process 2......''')

# 进程的构建方式二
class Myprocess(Process):
    def __init__(self, args):
        super().__init__()
        self.args = args

    def run(self):
        print('hello world with %s' % self.args)


if __name__ == '__main__':
    pro = Process(target=pro_test, args=('python',))
    # 运行
    pro.start()
    # 收尸
    pro.join()
    print(pro.name, pro.pid)

    pro2 = Process()
    pro2.run = pro2_test
    pro2.start() # 启动进程， 并调用run方法
    pro2.join()
    print(pro2.name, pro2.pid)

    pro3 = Myprocess('the argument of the process')
    pro3.start()
    pro3.join()