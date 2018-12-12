
'''
局部变量
全局变量
'''

def test():
	# 声明使用全局变量x
	global x
	x = 100
	y = 300	 # 局部变量:作用域和生存周期仅在从定义开始到函数结束


x = 200 # 全局变量:作用域从定义开始到进程结束
test()
print(x)

