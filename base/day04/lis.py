
'''
列表生成式
'''

l = []

for i in range(100):
	if i % 2 == 0:
		l.append(i)
print(l)

l = [i*i for i in range(100) if i % 2 == 0]
print(l)

'''
练习1:有字符串s1 = 'ABC' s2 = 'xyz' 生成一个列表，列表中的元素是['Ax', 'By', 'Cz']
'''
l = [x+y for x in 'ABC' for y in 'xyz']
print(l)

s1 = 'ABC'
s2 = 'xyz'
l = [s1[i]+s2[i] for i in range(len(s1))]
print(l)

'''
练习2:有列表l = ['Hello', 'EVERYone', 'goOd', 'AFTErNooN']
	使用一条语句将列表中变成由所有小写字母组成
'''
l = ['Hello', 'EVERYone', 'goOd', 'AFTErNooN']
l = [x.lower() for x in l]
print(l)



