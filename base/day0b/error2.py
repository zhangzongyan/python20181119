# -*- coding: utf-8 -*-
#   File Name：     error2
#   Description :
#   Author :       zongyanzhang
#   date：          2018/12/19

def foo(m, n):
    try:
        res = m / n
    except Exception as e:
        return e
    else:
        return res


print(foo(100, 0))

