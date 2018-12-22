# -*- coding: utf-8 -*-
#   File Name：     06pool
#   Description :
#   Author :       zongyanzhang
#   date：          2018/12/22

from multiprocessing import Pool
import time

def pro_job(s):
    print('the %d process is running' % s)
    time.sleep(2)


if __name__ == '__main__':
    # 创建进程池
    pool = Pool(2)

    for i in range(5):
        # 异步添加进程
        pool.apply_async(func=pro_job, args=(i, ))

    # 不允许向进程池中添加新的进程
    pool.close()
    # 收尸
    pool.join()

