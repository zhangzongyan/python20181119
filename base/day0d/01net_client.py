# -*- coding: utf-8 -*-
#   File Name：     01net_client
#   Description :
#   Author :       zongyanzhang
#   date：          2018/12/24

import socket

if __name__ == '__main__':
    s = socket.socket()

    # bind()
    s.connect(('192.168.5.68', 8888))
    '''
    while True:
        rcvdata = s.recv(1024)
        if rcvdata == b'':
            break
        print(rcvdata.decode('utf-8'))
    s.close()
    '''

    s.send(b'hello')
