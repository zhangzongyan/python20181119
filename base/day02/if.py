# 控制语句
'''
n = int(input('请输入一个偶数:'))

if n % 2 == 0:
	print('成功输入了一个偶数')
else:
	print('你傻吗？这不是一个偶数吧')
	print('你再想想吧')
'''
'''
判断用户输入的年份是否为闰年，闰年能被4整除并且不能被100整除，或者能被400整除的
'''
'''
year = int(input('年份:'))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
	print('{}是闰年'.format(year))
else:
	print('{}是平年'.format(year))
'''

'''
多个条件:输入一个月份，判断其所属季节
'''
'''
month = int(input('月份:'))

if month < 1 or month > 12:
	print('无效月份')
elif 3 <= month <= 5:
	print('春天')  
elif 6 <= month <= 8:
	print('夏天')
elif month >= 9 and month <= 11:
	print('秋天')
else:
	print('冬天')
'''
'''
读入一个成绩，判断其所属等级
	90~100 	A
	80～89	B
	70～79	C
	60～69	D
	0～59	E
'''
score = int(input('请输入一个成绩:'))

'''
if 90 <= score <= 100:
	print('A')
elif 80 <= score < 90:
	print('B')
elif 70 <= score <= 79:
	print('C')
elif 60 <= score <= 69:
	print('D')
else:
	print('E')
'''
if score > 100 or score < 0:
	pass
else:
	score //= 10
	if score == 9 or score == 10:
		print('A')
	elif score == 8:
		print('B')
	elif score == 7:
		print('C')
	elif score == 6:
		print('D')
	else:
		print('E')
	
	
	
	
	




