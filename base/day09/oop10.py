
'''
元类(metaclass)
'''
'''
class Test(object):
	def show(self, name='python'):
		print('hello %s', name)
'''

# type()构建一个类

def f(self, name='python'):
	print('hello %s'% name)

Test = type('Test', (object,), dict(show=f, name='python'))

t = Test()
t.show()
print(t.name)

# 另一种构建类的方法，是先构建元类，以元类为模板构建类
class ListMetaclass(type):
	def __new__(cls, name, bases, attrs):
		'''类方法'''
		attrs['add'] = lambda self, value : self.append(value)
		return type.__new__(cls, name, bases, attrs)

class Mylist(list, metaclass=ListMetaclass):
	pass

l = Mylist()
print(type(l))
l.add(1)
l.add('hello')
print(l)







