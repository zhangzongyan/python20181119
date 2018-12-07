
'''
生成器
'''
l = [i for i in range(100)]
print(l)

# 生成器：节省空间
g = (i for i in range(100))
print(g)

print(next(g))
print(next(g))

for x in g:
	print(x, end=' ')
print()

