'''
高阶函数：
	函数为参
'''

def test(n):
	return n ** 3

# g = map(test, (1,2,3,4))
g = map(lambda x : x**3, (1,2,3,4))
print(type(g))

'''
print(next(g))
print(next(g))
print(next(g))
'''
'''
for res in g:
	print(res)
'''
l = list(g)
print(l)

'''
练习1:
	生成一个由5个10以内随机整型数组成的列表，使用高阶函数map实现将5个整型数分别转换为字符串
'''

'''
练习2:
	将列表中每一个元素都转换为一个标准的标题，首字符大写其它小写
		l = ['hello world', 'Good AFTERNOON', 'morning']
'''


