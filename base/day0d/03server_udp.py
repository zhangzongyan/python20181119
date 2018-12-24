# -*- coding: utf-8 -*-
#   File Name：     03server_udp
#   Description :
#   Author :       zongyanzhang
#   date：          2018/12/24
'''
server                          client
s=socket.socket()               s = socket.socket()
s.bind()                        # s.bind()
                                s.sendto()
s.recvfrom()
s.close()                       s.close()
'''
import socket

if __name__ == '__main__':
    sd = socket.socket(type=socket.SOCK_DGRAM)
    sd.bind(('192.168.5.68', 9999))

    while True:
        data, clientaddr = sd.recvfrom(1024)
        print('from ip:{}, port:{}'.format(*clientaddr))
        print(data.decode('utf-8'))


