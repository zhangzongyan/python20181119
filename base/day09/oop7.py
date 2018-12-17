
'''
python魔法方法
'''

class Student(object):
	def __init__(self, name = 'python'):
		self.__name = name

	def __str__(self):
		'''打印本类对象时，自动调用'''
		return 'hello, %s' % self.__name

	def __repr__(self):
		'''在解释器环境下直接输出本对象，自动调用的方法'''
		return self.__str__()

	def __len__(self):
		'''调用len函数的时候自动调用的方法'''
		return 100

	def __call__(self):
		'''调用本类对象的时候自动调用的方法'''
		print('Student object name:%s' % self.__name)

print(dir(Student))

s = Student()
print(s)

print(len(s))

s()




