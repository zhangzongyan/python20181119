import random

'''
练习1：定义一个函数common_divisori()，求得两个整型数的最大公约数
'''
def common_divisori(m, n):
	if m < n:
		m, n = n, m
	# 辗转相除
	while True:
		mod = m % n
		if mod == 0:
			return n
		m = n
		n = mod
	

'''
练习2：定义一个函数maxoflist(),不使用max内置函数，实现求得整型列表的最大值
'''
def maxoflist(l):
	m = l[0]
	for i in range(1, len(l)):
		if l[i] > m:
			m = l[i]
	return m


'''
练习3：定义一个函数sortoflist()，不使用sorted()和sort()的基础上为一个整型列表排序(从小到大)
'''
# 冒泡排序
def sortoflist(l):
	n = len(l)
	for i in range(n-1): 
		for j in range(n-i-1):
			if l[j] > l[j+1]:
				l[j], l[j+1] = l[j+1], l[j]
			
	return l

def main():
	'''
	m,n = eval(input("请输入两个整型数:"))
	res = common_divisori(m, n)
	print("{}和{}的最大公约数是:{}".format(m, n, res))
	'''
	l = [random.randint(1, 100) for i in range(10)]
	'''
	print(l)
	res = maxoflist(l)
	print("最大的元素是%d" % res)
	'''
	l = sortoflist(l)
	print(l)

main()


