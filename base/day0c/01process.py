# -*- coding: utf-8 -*-
#   File Name：     01process
#   Description :
#   Author :       zongyanzhang
#   date：          2018/12/22

import os, time

if __name__ == '__main__':
    print('the calling process id:%d' % os.getpid())
    # 创建进程
    pid = os.fork()
    if pid == 0:
        # 子进程
        print('the child pid is %d' % os.getpid())
        time.sleep(3)
    elif pid > 0:
        # 父进程
        os.wait() # 等待子进程终止
        print('[%d]bye-bye' % os.getpid())

