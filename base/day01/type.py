# python中的类型
"""
内置类型:
	布尔类型：True False
	数字类型：int float
	文本类型：str	
	序列类型：list tuple range
	集合类型：set
	映射类型：dict
"""
# 定义一个整型变量
a = 1
b = int(100)
s = '100'
s = int(s) # 强转
print(type(s))


print(type(a))
print(type(b))

a = 10.2
print(type(a))

# 运算符
a = 10
b = 3.0
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

# 函数
print(abs(-100))
print(pow(2, 8))
print(divmod(8, 3))

# 关系运算符(> >= < <= == !=) 逻辑运算符(not and or)
print(10 > 100)
print(10 > 3 and 10 < 5)
print(-8 and 5)
print(0 and 5)
print(5 and 100)
print(5 and 100 < 5)
print(0 and 100 < 5)
print(10 > 5 and 2)

print('**********************')

print(-8 or 5)
print(0 or 5)
print(5 or 100)
print(5 or 100 < 5)
print(0 or 100 < 5)
print(10 > 5 or 2)

print('**********************')

print(10 and 5 or 0)
print(10 or 5 and 0)

print(not 5 and 10 > 5 or 100)

a = 100
b = a
print(a is b)
print(a, b)
a = 200
b = 200
print(a is b)
print(a, b)

# 赋值运算
# a = a + 2
a += 2 # -= *= /= //= %=
print(a)

print(1+True)

# 位运算(& | ^ ~ << >>)
a = '100'
print(int(a, 2))
b = 100
print(bin(b))
c = 66
print(bin(c))
print(b & c)
print(b | c)
print(b ^ c)

# 两个数的交换
b = b ^ c
c = b ^ c
b = b ^ c
print(b, c)

a = 4
print(a << 2)
print(a >> 2)





