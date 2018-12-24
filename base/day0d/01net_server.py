# -*- coding: utf-8 -*-
#   File Name：     01net
#   Description :
#   Author :       zongyanzhang
#   date：          2018/12/24
'''
tcp套接字

被动端(服务器)        主动端(客户端)
s = socket()        s = socket()
s.bind()            s.bind()---->可省略
s.listen()          s.connect()
s.accept()
s.recv() / s.send() s.recv() / s.send()
s.close()           s.close()
'''

import socket, time
from multiprocessing import Process

def fun(sd):
    for i in range(3):
        sd.send(b'ok!!!')
        time.sleep(1)
    sd.close()

if __name__ == '__main__':
    s = socket.socket()
    s.bind(('192.168.5.68', 6688))
    s.listen(20)
    while True:
        newsd, raddr = s.accept()
        print('recv client ip:{}, port:{}'.format(*raddr))
        pro = Process(target=fun, args=(newsd, ))
        pro.start()












