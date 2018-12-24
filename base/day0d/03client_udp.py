# -*- coding: utf-8 -*-
#   File Name：     03client_udp
#   Description :
#   Author :       zongyanzhang
#   date：          2018/12/24

import socket

if __name__ == '__main__':
    sd = socket.socket(type=socket.SOCK_DGRAM)

    sd.sendto(b'hello world', ('192.168.5.129', 9988))
    sd.close()
