import random

words = ('hello', 'python', 'boys', 'apple', 'world', 'eat')

# 'apple'
word = random.choice(words)

# 'palep'
save = word
'''
rand_str = ''
while word: # 不是空串
	rand_ind = random.randrange(len(word)) # random.choice(range(len(word)))
	rand_str += word[rand_ind]	
	word = word[:rand_ind]+word[rand_ind+1:] # 切除抽取的成员
'''
listword = list(word)
random.shuffle(listword)
rand_str = ''.join(listword)


print('请猜测%s是什么单词, 你有三次机会:' % rand_str)

for i in range(3):
	input_str = input('第%d次:' % (i+1))
	if input_str == save:
		print('恭喜你！答对了')
		break
	else:
		if i < 2:
			print('很遗憾！再试一次')
		else:
			print('游戏结束！已经没有机会了')



