# -*- coding: utf-8 -*-
#   File Name：     error
#   Description :
#   Author :       zongyanzhang
#   date：          2018/12/19

try:
    a, b = eval(input('请输入两个整型数:'))
    res = a / b
except NameError as e: # 捕获异常
    print('让你输入整型你不听:%s' % e)
except ZeroDivisionError:
    print('0不能做除数，你不知道吗')
else:
    # 如果没有异常
    print(res)
finally:
    # 不管是否有异常都会执行
    print('谢谢!!!!')
print('哈哈哈')

