
'''
装饰器(decorator):
	修饰函数
闭包:函数内有一个内嵌函数，内嵌函数可以使用外部函数的局部变量
'''

'''
import datetime

d = datetime.date()
print(d)
'''
# 函数作为返回只
def test():
	return str

f = test()
print(f(1234))

import functools

def decorator(f):
	@functools.wraps(f) # 此装饰器作用是将f的函数名赋值给wrapper
	def wrapper(*args, **kw):
		'''装饰器的内部函数'''
		# print(args, kw)
		print('hello python')
		# print(f.__name__)
		return f(*args, **kw)
	return wrapper

@decorator 
def show(name1, name2):
	'''验证装饰器功能的小函数'''
	print('hello %s and %s' % (name1, name2))
	return 100

print(show.__name__)
print(show.__doc__)
res = show('王涛', '任海') # show = decorator(show)
print(res)



