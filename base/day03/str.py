# 字符串 将用户输入字符串中的大写成员转小写，小写成员转大写
# ord()  chr()

s = input('str:')

new_str = ''
for i in s:
	if 'a' <= i <= 'z':
		# new_str += chr(ord(i) - (ord('a')-ord('A')))
		new_str += i.upper()
	elif 'A' <= i <= 'Z':
		# new_str += chr(ord(i) + (ord('a')-ord('A')))
		new_str += i.lower()
	else:
		new_str += i
print(new_str)

