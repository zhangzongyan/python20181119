
# 字符串类型

# 定义
s1 = 'hi'
s2 = "hello"
s3 = """moring"""
s4 = '''moring
good'''

print(s1, s2, s3, s4)

s = str(100)
print(type(s))

# 字符串中应用的运算符
print(s1 + s2)

print(s1 * 5)

s1 += s2
print(s1, s2)

# 成员运算符
print('hi' in s1)
print('hg' not in s1)

# 索引和切片 正向递增(0~len(s)-1) 反向递减(-1~-len(s))
s = 'python'
print(s[0])
print(s[-1])

print(s[1:3]) # s[a:b] a<=<b s[start=0:end=len(s):step=1]
print(s[-3:-1])
print(s[-1:-3:-1])

print(s[:3])
print(s[:])
print(s[::2])

# 函数
print(s[len(s)-1])
print(max(s))
print(min(s))
print(s.index('h'))
print(s.count('n'))

# 格式化字符串
n = 5
s = '我今天瘦了%d两'% n
print(s)
print('我今天%s高兴' % '很')

height=169
weight=80.5
print('我的身高是{}cm,体重是{}kg'.format(height, weight))
print('我的身高是{1}cm,体重是{0}kg'.format(weight, height))

name = 'python'
age = 29
print('我的名字{nameid}, 年龄是{ageid}'.format(ageid=age, nameid=name))

s = '我太帅了'
print('{:*>20}'.format(s))
print('{:*<20}'.format(s))
print('{:*^20}'.format(s))

f = 10.8998765
print('{:.2f}'.format(f))








