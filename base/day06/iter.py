'''
生成器(generator):
迭代器(Iterator):
	next()得到成员的:generator
可迭代(Iterable):
	能用for遍历的:str, list, tuple, dict, set, generator, range

collections模块中定义的Iterator和Iterable类型
'''

# 从1开始的fib
def fib(n):
	a, b = 0, 1
	while n > 0:
		# print(b)
		yield b # 随着生成器调用next方法，得到yield的值
		a, b = b, a+b
		n -= 1
	return 'done'

g = fib(10)
print(g)


