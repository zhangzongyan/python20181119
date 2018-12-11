'''
递归调用:
	在函数内调用函数本身

	1. 找到终止条件
	2. 找到递归条件
'''

def sumn(n):
	'''
		n的前n项和
	'''
	if n == 0:
		return 0
	return n + sumn(n-1)


'''
Fibnacci数列的第n项
'''
def fibnacci(n):
	if n <= 0:
		return False 
	if n == 1:
		return 0 
	elif n == 2:
		return 1 
	return fibnacci(n-1) + fibnacci(n-2)



print(sumn(10))
for i in range(1, 21):
	print(fibnacci(i), end = ' ')
print()


