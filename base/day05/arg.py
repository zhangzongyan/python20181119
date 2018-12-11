
'''
参数类型:
	位置参数
	默认参数
	可变参数
	关键字参数
'''

# 位置参数
def max2num(x, y):
	print(x, y)
	return x if x > y else y


# 默认参数
def power(x, y=2):
	s = 1
	while y:
		s *= x
		y -= 1
	return s

# 默认参数的默认值最好不是可变类型
'''
def add_end(l=[]):
	l.append('python')
	return l
'''

def add_end(l=None):
	if l == None:
		l = []
	l.append('python')
	return l

# 可变参数
def sumall(*numbers):
	# print(type(numbers))
	s = 0

	for i in numbers:
		s += i

	return s

# 位置参数在可变参数后
def test(*args, n=100):
	print(n, args)


# 关键字参数
def stuinfo(name, age, city='北京', **kw):
	print(name, age, city, kw)


# 命名关键字参数
def stuinfo2(name, age, city='北京', *, height, gender):
	print(name, age, city, height, gender)	


# 多种参数类型混合使用 位置参数在第一位，关键字参数一定在最后
def test2(locate, *args, name, age, default=100, **kw):
	print(locate, args, default, name, age, kw)


res = max2num(10, 20)
print(res)

res = max2num(y=100, x=200)
print(res)

print(power(10, 4))
print(power(10))

ls = [1,2,3]
add_end(ls)
print(ls)

print(add_end())
print(add_end())
print(add_end())

res = sumall(1,2,3,4,5)
print(res)

test(1,2,4,5)

stuinfo('米佳齐', 20, height=178, gender='M', school='河北农大')
stuinfo2('米佳齐', 20, height=178, gender='M')
stuinfo2('米佳齐', 20, gender='M', height=175)

test2(1, 'hello', 'world',  name='uplooking', age=14, python='guido', height=180)

