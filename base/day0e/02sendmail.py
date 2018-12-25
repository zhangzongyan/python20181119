# -*- coding: utf-8 -*-
#   File Name：     02sendmail
#   Description :
#   Author :       zongyanzhang
#   date：          2018/12/25

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
from email.header import Header
from smtplib import SMTP
from email.mime.base import MIMEBase
from email.encoders import encode_base64

if __name__ == '__main__':
    msg = MIMEMultipart()
    text = MIMEText('你好！\n不好意思有打扰您！涨工资的事您考虑的怎么样了....', 'plain', 'utf-8')
    msg.attach(text)
    msg['From'] = formataddr((Header('陈云亮', 'utf-8').encode(), '1312191341@qq.com'))
    msg['To'] = formataddr((Header('领导', 'utf-8').encode(), 'python_1989@163.com'))
    msg['Subject'] = Header('您在考虑一下', 'utf-8')

    # 添加附件图片
    with open('cool.gif', 'rb') as f:
        mime = MIMEBase('image', 'gif')
        mime.add_header('Content-Disposition', 'attachment', filename='cool.gif')
        # 加载图片
        mime.set_payload(f.read())
        # 指定编码格式
        encode_base64(mime)
        msg.attach(mime)


    # 发邮件
    smtp = SMTP('smtp.qq.com', 25)
    # 打开调试
    smtp.set_debuglevel(1)
    # 登录邮箱
    smtp.login('1312191341@qq.com', 'vemaluredgrlgede')
    # 发送
    smtp.sendmail('1312191341@qq.com', ['python_1989@163.com'], msg.as_string())
    # 断开
    smtp.quit()