
'''
有序的不可变的序列类型:
	元组tuple
'''
t = () 
print(type(t))

t1 = (1,)
print(type(t1))

t2 = tuple([1,2,3,4, 'hello'])
print(t2)

# 索引 切片
print(t2[0])
print(t2[::-1])
print(t2)

# 成员运算符
for t in t2:
	print(t)

print('*****************************')
t3 = (5,6,2,12,7,8,7,1,100)
print(max(t3))
print(min(t3))
print(len(t3))
print(t3.index(7))
print(t3.count(7))




