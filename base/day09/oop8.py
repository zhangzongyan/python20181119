
'''
魔法方法
'''

class Fib(object):
	cnt = 0
	def __init__(self):
		self.a = 0
		self.b = 1

	def __iter__(self):
		'''返回可迭代对象'''
		return self

	def __next__(self):
		'''随着循环自动调用的'''
		self.a, self.b = self.b, self.a+self.b
		
		if self.a >= 100:
			'''循环遍历终止'''		
			raise StopIteration()
		Fib.cnt += 1
		
		return self.a

	def __len__(self):
		return Fib.cnt

	def __getitem__(self, n):
		'''索引时自动调用的方法'''
		if isinstance(n, int):
			a, b = 0, 1
			while n >= 0:
				a, b = b, a+b
				n -= 1
			return a	

		if isinstance(n, slice):
			'''切片类型 start:end'''
			if n.start == None:
				start = 0
			else:
				start = n.start	
			if n.stop == None:
				return 'error'
			stop = n.stop
			l = []
			for i in range(start, stop):
				l.append(self[i])
			return l

f = Fib()

print(dir(f))

for i in f:
	print(i, end=' ')
print()

print(len(f))

for i in range(20):
	print(f[i], end=' ')
print()

print(f[0:3])
print(f[1:10])



