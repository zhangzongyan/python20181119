'''
公鸡5文钱1只，母鸡3文钱1只，小鸡3只1文钱，用100文钱买100只鸡，可以怎么买？
'''
for cock in range(21):
	for hen in range(34):
		for chick in range(101):
			if cock + hen + chick == 100 and cock*5 + hen*3 + chick/3 == 100:
				print("100文钱可以买公鸡:{}只，母鸡:{}只,小鸡:{}只".format(cock, hen, chick))

'''
像121 11 111等对称的整型数称为回文整型数,随机产生1000以内的10个整型数，打印其中的回文整型数
'''
for i in range(10):
	n = int(input('输入一个整型数:'))
	'''
	s = str(n) 
	s_reverse = s[::-1]
	if s == s_reverse:
		print('{}是回文整型'.format(s))
	'''
	save = n		
	res = 0

	while n:
		res = res*10 + n % 10
		n //= 10
	if res == save:
		print('{}是回文整型'.format(save))
		





