# for...in循环

for i in range(10):
	print(i)

i = 0
while i < 10:
	print(i)
	i += 1

print('*******************************')
for i in range(5, 10):
	print(i)
i = 5
while i < 10:
	print(i)
	i += 1

print('*******************************')
for i in range(10, 5, -1):
	print(i)
i = 10
while i > 5:
	print(i)
	i -= 1

print('*******************************')
# 遍历字符串
for i in 'python':
	print(i)

print('*******************************')
for i in range(100):
	if i % 2:
		continue	
	if i > 90:
		break
	print(i)


