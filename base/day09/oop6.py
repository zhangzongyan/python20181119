'''
多继承:
	python支持，但不建议使用	
'''

class A(object):
	def run(self):
		print('run A run')

class B(A):
	def run(self):
		super().run()
		print('run B run')

class C(A):
	def run(self):
		super().run()
		print('run C run')

class D(B, C):
	pass


c = C()
c.run()
# 获取类或者对象的方法和属性
print(dir(C))
# 获取类的继承顺序
print(C.__mro__)

d = D()
d.run()
print(D.__mro__)



