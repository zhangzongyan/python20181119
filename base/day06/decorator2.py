
'''
带参数的装饰器
'''
import functools

def log(text, text2):
	def decorator(f):
		@functools.wraps(f)
		def wrapper(*args, **kw):
			print('log', text, text2)	
			print('这个装饰器好吧?')
			return f(*args, **kw)
		return wrapper
	return decorator


@log('argument', 'haha')
def now():
	print('2018-12-12')

now() # now = log('argument')(now)

