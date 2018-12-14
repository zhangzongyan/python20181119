
'''
限制实例属性
'''
class Person(object):
	__slots__ = ('name', 'age') # 只允许由'name' 'age'属性
'''
per1 = Person()
per1.name = '小明'
print(per1.name)
per1.height = 167 # 不允许
'''

class Student(object):
	def __init__(self, age):
		self.__age = age
	'''
	def setScore(self, score):
		if 0 <= score <= 100:
			self.__score = score
			return 'ok'
		else:
			return 'error'
			
	def getScore(self):
		return self.__score
	'''

	@property # 访问器 可以单独存在
	def score(self):
		print('getter is called')
		return self.__score

	@score.setter # 设置器 不单独存在，一定要有property
	def score(self, score):
		print('setter is called')
		if 0 <= score <= 100:
			self.__score = score
			return 'ok'
		else:
			return 'error'

	@ property
	def age(self):
		return self.__age


s1 = Student(20)
'''
if s1.setScore(10) == 'ok': # s1.score= 100
	print(s1.getScore())
'''
s1.score = 100
print(s1.score)
print(s1.age)



