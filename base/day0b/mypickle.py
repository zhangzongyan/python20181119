# -*- coding: utf-8 -*-
#   File Name：     mydmp
#   Description :
#   Author :       zongyanzhang
#   date：          2018/12/19
'''
文件序列化
'''
import pickle as pk

with open('text', 'w+b') as f:
    d = dict(name='python', age=20)
    # 序列化
    '''
    data = pk.dumps(d)
    f.write(data)
    '''
    pk.dump(d, f)

    # 读出写入的字典
    f.seek(0, 0)
    '''
    d = f.read()
    # 反序列化
    dt = pk.loads(d)
    '''
    dt = pk.load(f)
    print(dt)


class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


s1 = Student('uplooking', 13)
with open('text', 'r+b') as f:
    pk.dump(s1, f)
    f.seek(0, 0)
    s = pk.load(f)
    print(s.name, s.age)


