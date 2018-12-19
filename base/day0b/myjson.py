# -*- coding: utf-8 -*-
#   File Name：     myjson
#   Description :
#   Author :       zongyanzhang
#   date：          2018/12/19

'''
json数据格式

json        python
{}          dict
[]          list
""          str
123         int
true/false  True / False
null        None
'''

import json

d = dict(name='hello', age=3)
# 转换为json
jd = json.dumps(d)
print(type(jd))
print(jd)

# 将json数据类型转换为python
ld = json.loads(jd)
print(type(ld))
print(ld)

class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

def student2dict(s):
    return {'name':s.name, 'age':s.age}

s = Student('world', 4)
# 将student2dict函数的返回值作为dumps参数
js = json.dumps(s, default=student2dict)
print(js)

def dict2student(d):
    return Student(d['name'], d['age'])

# 将loads转换回的字典作为dict2student的参数
print(json.loads(js, object_hook=dict2student))
