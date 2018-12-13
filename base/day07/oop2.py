
'''
面向对象(oop):	
	类:抽象概念，类型
	对象:实际物体,类实例化对象
	属性:
		描述类---》类属性
		描述对象---》实例属性
'''

# 抽象类型
class Student(object):
	count = 0 # 类属性：类名.属性名
	def __init__(self, score): # --->构造函数:实例化对象时自动调用的
		self.__score = score # 私有属性,只允许在本类中访问
		Student.count += 1

	# 实例方法
	def setName(self, name):
		if 1 < len(name) < 32:
			self.name = name
			return True
		else:
			return False

	def run(self):
		print('%s is running' % self.name)

	def getScore(self):
		self.__privateFun()
		return self.__score

	# 私有方法
	def __privateFun(self):
		print('private....')

	def __del__(self): # 析构方法:对象销毁的时候自动调用调用
		print('delete.....')

# 实例化对象
s1 = Student(100)
# 访问对象的属性
print(s1.getScore())

# 私有属性---》解释器做了名字的修改
print(s1._Student__score)

# 私有方法
# s1.__privateFun()
s1._Student__privateFun()


