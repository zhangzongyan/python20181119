# -*- coding: utf-8 -*-
#   File Name：     03recvmail
#   Description :
#   Author :       zongyanzhang
#   date：          2018/12/25

from poplib import POP3

if __name__ == '__main__':
    pop = POP3('pop.163.com', 110)

    pop.set_debuglevel(1)

    # 连接成功欢迎字符串
    print(pop.getwelcome().decode())

    # 登录
    pop.user('python_1989@163.com')
    pop.pass_('python123456')

    # 邮件状态(总件数,总大小)
    print(pop.stat())

    # 获取每一封邮件索引和大小
    response, res, oct = pop.list()
    print(res)

    # 获取最后一封邮件
    response, context, oct = pop.retr(25)
    print(context)

    res = b'\r\n'.join(context)
    print(res.decode('utf-8'))
