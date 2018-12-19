# -*- coding: utf-8 -*-
#   File Name：     error3
#   Description :
#   Author :       zongyanzhang
#   date：          2018/12/19

class FooError(ValueError):
    pass


def foo(m, n):
    if n == 0:
        # 抛出异常
        raise FooError('n is zero error...')
    res = m // n
    return res

try:
    foo(10, 0)
except FooError as e:
    raise ZeroDivisionError('test error')

