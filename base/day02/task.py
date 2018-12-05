
'''
练习1:读入两个整型数，求得两个数中较大的一个
'''
'''
num1, num2 = eval(input('读入两个整型数:'))
if num1 > num2:
	print(num1)
else:
	print(num2)
'''

'''
练习2:读入一个字符串，不使用len函数，求得字符串的长度
'''
'''
s = input('请输入一个字符串:')
n = 0
for i in s:
	n += 1
print('字符串{}的长度是{}'.format(s, n))
'''

'''
练习3:打印99乘法表
'''
'''
for i in range(1, 10): # row
	for j in range(1, i+1): # col
		print('{}*{}={:<2}'.format(j, i, j*i), end=' ')
	print()
'''

'''
练习4:读入一个整型数，判断其是否为质数(除了1和本身不能被其它数整除的数)
'''
n = int(input('整数:'))
prime = True

i = 2
while i < n:
	if n % i == 0:
		prime = False	
		break
	i += 1
if prime:
	print('yes')
else:
	print('no')


