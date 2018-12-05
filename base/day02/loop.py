# 循环语句 while  for
'''
i = 0

while i < 10:
	score = int(input('请输入一个成绩:'))
	
	if score > 100 or score < 0:
		break
		# continue
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
	i += 1
else:
	print("10个成绩判断完成")		
'''
'''
练习1:读入一个整型数，将其每一位倒序输出,不允许转换为字符串 1998
'''
'''
n = int(input('整型数:'))

while n > 0:
	print(n % 10)
	n = n // 10
'''
'''
练习2：将读入字符串的每一个成员倒序输出
'''
s = input('请输入一个字符串:')
i = len(s)-1
while i >= 0:
	print(s[i])
	i -= 1

i = -1
while i >= -len(s):
	print(s[i])	
	i -= 1




