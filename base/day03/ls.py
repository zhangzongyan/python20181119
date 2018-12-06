
'''
可变的序列类型：
	列表list
'''
l = []
l = [1,2,3,'hello', [11,22]]
ls = list('hello')
ls2 = list(range(100))

print(ls)
print(ls2)

# 索引
print(l[0])
print(l[4])
print(l[4][0])

# 切片
print(l[:4])
print(l[1:])
print(l[1::2])

# 增
l[1:1] = [100]
print(l)
l.append(110)
print(l)
l.insert(2, 119)
print(l)

# 删
l[1:3] = []
print(l)
l.pop(3)
print(l)
l.remove([11,22])
print(l)

# 修改
l[0] = 120
l[1:3] = [9,8,7,6]
print(l)
l += ['a', 'b', 'c']
print(l)
l.extend([607, 478])
print(l)

# 查
for i in l:
	print(i)

for i in range(len(l)):
	print(l[i])

l.reverse()
print(l)
l = [10, 12, 5, 2, 1, 7, 8]
l.sort(reverse=True)
print(l)








