'''
深复制和浅复制
'''
import copy

# 对于非复合类型 深复制和浅复制无差别
a = 10
b = copy.copy(a)
print(id(a))
print(id(b))
a = 20
print(a, b)

# 对于可变复合类型 浅复制不会复制子对象,而深复制会
a = [1,2,[100, 200]]
b = copy.copy(a)
print(id(a))
print(id(b))
a[0] = 110
print(a)
print(b)
a[2][1] = 222
print(a)
print(b)

b = copy.deepcopy(a)
print(id(a))
print(id(b))
a[0] = 1
print(b)
a[2][1] = 333
print(a)
print(b)

print(id(a[2]))
print(id(b[2]))

