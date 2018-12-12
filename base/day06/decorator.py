
'''
装饰器(decorator):
	修饰函数
'''

'''
import datetime

d = datetime.date()
print(d)
'''

def decorator(f):
	def wrapper(*arg, **kw):
		print(arg, kw)
		print('hello python')
		return f(*arg, **kw)
	return wrapper

@decorator 
def show(name1, name2):
	print('hello %s and %s' % (name1, name2))
	return 100

res = show('王涛', '任海') # show = decorator(show)
print(res)



