
'''
1990.1.1 星期1
2018.11.1
'''

year, month = eval(input('请输入年份和月份(year,month):'))

sumdays = 0
# 1990~year
for y in range(1990, year):
	sumdays += (365+(1 if (y % 4 == 0 and y % 100 != 0 or y % 400 == 0) else 0))

# year.1.1 ~ year.month.1
for m in range(1, month):
	if m == 1 or m == 3 or m == 5 or m == 7 or \
		m == 8 or m == 10 or m == 12:
		sumdays += 31 
	elif m == 4 or m == 6 or m == 9 or m == 11:
		sumdays += 30
	else:
		if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
			sumdays += 29
		else:
			sumdays += 28

sumdays += 1

weekday = sumdays % 7

# 计算month月有多少天
if month == 1 or month == 3 or month == 5 or month == 7 or \
	month == 8 or month == 10 or month == 12:
	monthdays = 31 
elif month == 4 or month == 6 or month == 9 or month == 11:
	monthdays = 30
else:
	if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
		monthdays = 29
	else:
		monthdays = 28

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

