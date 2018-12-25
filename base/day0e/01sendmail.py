# -*- coding: utf-8 -*-
#   File Name：     01sendmail
#   Description :
#   Author :       zongyanzhang
#   date：          2018/12/25

from email.mime.text import MIMEText
from smtplib import SMTP
from email.header import Header
from email.utils import formataddr

if __name__ == '__main__':
    # 构建邮件
    msg = MIMEText('我不是垃圾邮件，就是一个测试', 'plain', 'utf-8')
    # 发件人
    msg['From'] = formataddr((Header('尚观','utf-8').encode(), '1312191341@qq.com'))
    # 收件人
    msg['To'] = formataddr((Header('朋友','utf-8').encode(), 'python_1989@163.com'))
    # 邮件主题
    msg['Subject'] = Header('圣诞快乐', 'utf-8')

    # 发邮件
    smtp = SMTP()
    smtp.connect('smtp.qq.com', 25)
    # 打开调试
    smtp.set_debuglevel(1)
    # 登录邮箱
    smtp.login('1312191341@qq.com', 'vemaluredgrlgede')
    # 发送
    smtp.sendmail('1312191341@qq.com', ['python_1989@163.com'], msg.as_string())
    # 断开
    smtp.quit()
