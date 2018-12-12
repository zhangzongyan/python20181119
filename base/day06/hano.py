
'''
汉诺塔
'''

# 定义三个全局的列表
la = []
lb = []
lc = []

stepn = 0

def create_hano(n):
	'''构建由n个圆盘组成的汉诺塔'''
	global la
	la = [i for i in range(n, 0, -1)]	


def move(src, dest):
	'''从src柱子上最上面的圆盘移动到dest柱子上'''
	dest.append(src.pop())
	global stepn	
	stepn += 1

	input()

	print('柱子A:',la)
	print('柱子B:',lb)
	print('柱子C:',lc)


def start_game(src, tmp, dest, n):
	if n == 1:
		move(src, dest)
		return None
	if n < 1:
		return -1
	start_game(src, dest, tmp, n-1)	
	start_game(src, tmp, dest, 1)
	start_game(tmp, src, dest, n-1)


create_hano(4)
print('柱子A:',la)
print('柱子B:',lb)
print('柱子C:',lc)
start_game(la, lb, lc, 4)
print(stepn)


