# -*- coding: utf-8 -*-
#   File Name：     error3
#   Description :
#   Author :       zongyanzhang
#   date：          2018/12/19


def foo(m, n):
    # 断言 如果断言为False 则抛出AssertionError
    assert n != 0, 'n is zero'
    res = m // n
    return res


print(foo(10, 0))
