'''
继承
'''

class Animal(object):
	def __init__(self, name, age=1, color='white'): # 重写
		self.name = name
		self.age = age
		self.__color = color  # _Animal__color

	def show(self):
		print(self.name, self.age, self.__color)


class Dog(Animal):
	def __init__(self, name, age, breed):
		# 调用父类方法
		# Animal.__init__(self, name, age)
		# super(Dog, self).__init__(name, age)
		super().__init__(name, age)
		self.breed = breed
	
	def show(self):
		Animal.show(self)
		print('品种是%s' % self.breed)


class Cat(Animal):
	'''
	def getColor(self):
		return self.__color # 子类中不能直接访问继承的私有属性
		# return self._Animal__color
	'''
	pass

animal1 = Animal('花花')
animal1.show()

d1 = Dog('旺财', 1, '哈士奇')
d1.show()

cat1 = Cat('来福', 2, '花色')
cat1.show()

print(cat1.getColor())

