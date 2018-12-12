
'''
匿名函数
	适合函数功能简洁的
'''

f = lambda x : True if x % 2 == 0 else False
print(type(f))

print(f(101))

f = lambda : print('hello world')
f()

f = lambda x, y : x * y
print(f(10, 14))

f = lambda x, y=2 : x ** y
print(f(5, 5))

f = lambda x, *arg : print(x, arg) 
print(f(1, 2,3,4,5,6))


