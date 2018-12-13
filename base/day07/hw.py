
'''
现有以下函数，利用装饰器为此函数加上认证功能，也就是只有用户名为'python', 密码为'123'才能调用此函数，否则不允许

def my_log(name):

　　print('%s欢迎登陆'%(name))
'''
import functools

def decorator(f):
	@ functools.wraps(f)
	def wrapper(*args, **kw):
		name = input('用户名:')		
		pwd = input('密码:')
		if name == 'python' and pwd == '123':
			return f(*args, **kw)
	return wrapper

@ decorator
def my_log(name):
	print('%s欢迎登陆'%(name))


'''
利用装饰器为函数加上统计执行时间的功能。
　　提示 time模块中的time()函数可以获取当前时间
'''
import time
def decorator2(f):
	@ functools.wraps(f)
	def wrapper(*args, **kw):
		bef = time.time()
		ret = f()
		aft = time.time()
		print('执行时间是{}'.format(aft-bef))
		return ret

	return wrapper

@ decorator2
def test():
	print('running....')	
	time.sleep(1)

if __name__ == '__main__':
	test()
	my_log('amazing')
