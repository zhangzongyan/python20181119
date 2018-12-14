
'''
实现发牌器(牌中不包含大小鬼),共4个玩家,每人13张牌
黑桃 方片 红桃 梅花
A 2 3 4 5 6 7 8 9 10 j q k

Card()--->单张扑克类
	属性:
		花色(color)
		值(number)
		状态(face)
	行为:
		展示(show)

Hand() -----> 玩家类
	属性:
		名字(name)
		一手牌(rands)	
	行为:
		增加牌(add)
		减少牌(play)
		显示(show)

Puke(Hand) ------> 一副扑克
	属性:
	行为:
		生成一幅牌(getall)
		洗牌(randPuke)
		发牌(deal)	

'''
from random import shuffle

class Card(object):
	colors = ['梅花', '红桃', '黑桃', '方片']
	numbers = ['A'] + [str(i) for i in range(2, 11)]+['J', 'Q', 'K']
	def __init__(self, color, number, face = True):
		self._color = color	
		self._number = number
		self._face = face

	def show(self):	
		'''展示当前牌'''
		if self._face:
			return self._color+self._number
		else:
			return 'X'

	def flip(self):
		'''翻牌'''
		self._face = not self._face


class Hand(object):
	def __init__(self, name='神秘玩家'):
		self._name = name
		self._cards = [] # 一手牌

	def add(self, card):
		'''增加一张牌'''
		self._cards.append(card)

	def show(self):
		res = [] 
		for c in self._cards:
			res.append(c.show())
		return ','.join(res)


class Poke(Hand):
	def getall(self):
		'''生成由52张牌组成的一手牌'''
		for c in Card.colors:
			for n in Card.numbers:
				self._cards.append(Card(c, n))

	def randomPuke(self):
		'''洗牌'''
		shuffle(self._cards)		

	def dealPuke(self, hands, count=13):
		'''发牌'''		
		for c in range(count):
			for h in hands:
				poppuke = self._cards.pop()
				h.add(poppuke)
	
if __name__ == '__main__':
	poke = Poke()
	
	# 生成一幅扑克
	poke.getall()
	# print(poke.show())

	poke.randomPuke()
	hands = [Hand('陈云亮'), Hand('王涛'), Hand('王志勇'), Hand('米佳琪')]
	poke.dealPuke(hands)

	for h in hands:
		print(h._name, h.show())	


