# -*- coding: utf-8 -*-
#   File Name：     02process
#   Description :
#   Author :       zongyanzhang
#   date：          2018/12/22

import os, sys

if __name__ == '__main__':
    while True:
        cmd = input('[root@localhost xxxx]# ')
        if cmd == 'quit' or cmd == 'exit':
            # 终止进程
            sys.exit(0) # os._exit()
        # 'ls -l'
        cmdls = cmd.split()
        pid = os.fork()
        if pid == 0:
            # child  替换调用进程
            os.execlp(cmdls[0], *cmdls)
        # parent
        os.wait()
