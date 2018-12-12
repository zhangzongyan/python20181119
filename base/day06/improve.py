'''
高阶函数：
	函数为参
'''

def test(n):
	return n ** 3

# g = map(test, (1,2,3,4))
g = map(lambda x : x**3, (1,2,3,4))
print(type(g))

'''
print(next(g))
print(next(g))
print(next(g))
'''
'''
for res in g:
	print(res)
'''
l = list(g)
print(l)

'''
练习1:
	生成一个由5个10以内随机整型数组成的列表，使用高阶函数map实现将5个整型数分别转换为字符串
'''
import random

l = [random.randrange(10) for i in range(5)]
print(l)
l = list(map(str, l))
print(l)

'''
练习2:
	将列表中每一个元素都转换为一个标准的标题，首字符大写其它小写
		l = ['hello world', 'Good AFTERNOON', 'morning']
'''
l = ['hello world', 'Good AFTERNOON', 'morning']
l = list(map(lambda x : x.title(), l))
print(l)

# reduce()
from functools import reduce

def f(x, y):
	return x * 10 + y

n = reduce(f, (1,5,6,7))
print(type(n), n)

n = reduce(lambda x,y : x*y, (1,2,3,4,5,6))
print(n)

'''
实现一个将字符串转换为整型数的函数str2int()
	'1432' ----> 1432 不允许调用int函数
'''
def str2int(s):
	g = map(lambda x:ord(x)-ord('0'), s)
	return reduce(lambda x, y:x*10+y, g)

print(str2int('1423'))

# filter()
res = filter(lambda x : x % 2 == 0, [random.randrange(100) for i in range(10)])
print(list(res))

# sorted()
l = ['hello', 'Yes', 'PYTHON', 'world', 'Go']
res = sorted(l, key=str.lower, reverse=True) # 按小写排序
print(res)











