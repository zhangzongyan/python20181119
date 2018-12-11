
'''
1990.1.1 星期1
2018.11.1
'''

def isleap(y):
	'''
		function:判断是否为闰年
		y:判断的年份
		return:True / False
	'''
	return True if (y % 4 == 0 and y % 100 != 0 or y % 400 == 0) else False


def dayofmonth(m, y):
	'''
		function:m月有多少天
	'''
	if m in (1,3,5,7,8,10,12):
		days = 31 
	elif m in (4,6,9,11):
		days = 30
	else:
		if isleap(y):
			days = 29
		else:
			days = 28
	return days	


def main():
	year, month = eval(input('请输入年份和月份(year,month):'))
	
	sumdays = 0
	# 1990~year
	for y in range(1990, year):
		sumdays += (365+isleap(y))
	
	# year.1.1 ~ year.month.1
	for m in range(1, month):
		sumdays += dayofmonth(m, year)
	
	sumdays += 1
	
	weekday = sumdays % 7
	
	# 计算month月有多少天
	monthdays = dayofmonth(month, year)	
	
	# 打印日历
	m = '一二三四五六七八九十'
	if month == 11:
		monthstr = '十一'
	elif month == 12:
		monthstr = '十二'
	else:
		monthstr = m[month-1]
	print('\33[34m{:>7}月 {}'.format(monthstr, year))
	print('\33[0m', end='') # 关闭属性
	print('\33[47m日 一 二 三 四 五 六')
	print('\33[0m', end='') # 关闭属性
	print('   '*weekday, end='')
	for d in range(1, monthdays+1):
		print('{:>2}'.format(d), end=' ' if (weekday+d)%7 else '\n')	
	print()
	

# 调用函数
main()







