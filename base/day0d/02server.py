# -*- coding: utf-8 -*-
#   File Name：     02server
#   Description :
#   Author :       zongyanzhang
#   date：          2018/12/24

import socketserver as ss
import time


class MyRequest(ss.BaseRequestHandler):
    def handle(self):
        '''服务端的工作'''
        # self.request是已连接套接字 self.socket监听套接字
        data = self.request.recv(1024)
        print('客户端地址ip:{}, port:{}'.format(*self.client_address))
        print(data)
        time.sleep(3)


if __name__ == '__main__':
    with ss.ThreadingTCPServer(('192.168.5.68', 8888), MyRequest) as server:
        server.serve_forever()



