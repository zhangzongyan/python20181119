
'''
枚举类
'''

'''
INSERT=1 # 缺点就是本质是变量，可以改变

if choose == INSERT:
	pass
'''

from enum import Enum, unique

@ unique # 防止枚举成员的重复
class Menu(Enum):
	INSERT=1
	DELETE=2
	UPDATE=3
	SHOW=4
	# CHOOSE=4

print(Menu.INSERT.value)
# Menu.INSERT.value = 2
print(Menu['INSERT'])


