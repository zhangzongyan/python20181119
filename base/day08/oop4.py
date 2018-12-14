'''
多态
'''

class Animal(object):
	def run(self):
		print('animal is running')


class Dog(Animal):
	def run(self):
		print('Dog run fast')


class Rabbit(Animal):
	def run(self):
		print('Rabbit jump...')

class Cat(Animal):
	pass

class Timer(object):
	def run(self):
		print('the time is running')


# 多态：同一种类型，不同的表现形式
def runTwice(animal):
	animal.run()
	animal.run()

a = Animal()
rabbit = Rabbit()

runTwice(a)
runTwice(rabbit)

# 鸭子类型
tm = Timer()
runTwice(tm)

