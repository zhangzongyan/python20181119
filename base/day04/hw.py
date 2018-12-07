
'''
抓了a,b,c,d四名犯罪嫌疑人，其中有一人是小偷，审讯中：

•a说我不是小偷；
•b说c是小偷；
•c说小偷肯定是d；
•d说c胡说！

其中有三个人说的是实话，一个人说的是假话，请编程推断谁是小偷。
''' 

for thief in ('a', 'b', 'c', 'd'):
	if ((thief != 'a') + (thief == 'c') + \
		(thief == 'd') + (thief != 'd')) == 3:
		print('小偷是{}'.format(thief))
		break

'''
斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。

求斐波那契数列的前20项
'''
a = 0
b = 1

print(a, b, end=' ')
for i in range(18):
	c = a+b
	print(c, end=' ')
	a = b
	b = c
print()





