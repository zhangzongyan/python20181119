
'''
面向对象(oop):	
	类:抽象概念，类型
	对象:实际物体,类实例化对象
	属性:
		描述类---》类属性
		描述对象---》实例属性
'''

# 面向过程描述学生的成绩
d = {'miguitian':80, 'yangzhichao':88, 'zhangxue':100, 'liuhongsheng':12}

# 抽象类型
class Student(object):
	count = 0 # 类属性：类名.属性名
	def __init__(self, score): # --->构造函数:实例化对象时自动调用的
		# print('__init__ is called')
		# self : 当前对象
		self.score = score
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

	def __del__(self): # 析构方法:对象销毁的时候自动调用调用
		print('delete.....')

# 实例化对象
s1 = Student(100)
# 访问对象的属性
print(s1.score)
s1.name = 'chenyunliang'
print(s1.name)

del s1

s2 = Student(98)
print(s2.score)

# 调用方法
s2.setName('python')
print(s2.name)

s2.run()

print('学生对象有%d个'%Student.count)



