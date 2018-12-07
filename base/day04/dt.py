
'''
字典(dict):
	无序的可变的, 有key=value组成的
'''

# 定义
d1 = {'name':'python', 'age':20}
print(type(d1))
print(d1)

d2 = dict(name='python', age=20)
print(type(d2))
print(d2)

d3 = dict([('name', 'python'), ('age', 20)])
print(type(d3))
print(d3)

d4 = dict(zip(['name', 'age'], ['python', 20]))
print(type(d4))
print(d4)

# 通过key得到成员: key唯一的,不可变的
print(d4['name'])

d4['name'] = 'guido'
print(d4)

# 获得所有的key, values, item
print(d4.keys())

print(d4.values())

print(d4.items())

# 遍历
for k in d4.keys():
	print(d4[k])

for k, v in d4.items():
	print(k, v)

for k in d4: # key
	print(k)

# 增加
d4['height'] = 180
print(d4)

d4.update(id=5, score=100)
print(d4)

# 删除
d4.pop('id')
print(d4)











