# 读入
s = input('请说的什么:')
print(type(s))
print(s)

n = int(s)
print(type(n), n)

s = input('请输入两个整型数:')
print(s)

a, b = eval(s) # 将字符串'num1, num2'转换为整型数num1, num2
print(a, b)
