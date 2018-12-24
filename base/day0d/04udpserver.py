# -*- coding: utf-8 -*-
#   File Name：     04udpserver
#   Description :
#   Author :       zongyanzhang
#   date：          2018/12/24

# ForkingUDPServer只能应用于unix操作系统

from socketserver import ForkingUDPServer, BaseRequestHandler
import time


class MyUdpRequest(BaseRequestHandler):
    def handle(self):
        # self.request是一个元祖，包含两个成员，分别是数据，以及套接字对象
        data = self.request[0]
        sd = self.request[1] # socket
        print('from ip:{}, port:{},recv:{}'.format(*self.client_address, data.decode()))
        time.sleep(10)


if __name__ == '__main__':
    with ForkingUDPServer(('192.168.5.68', 9988), MyUdpRequest) as server:
        server.serve_forever()





