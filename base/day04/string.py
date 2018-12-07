
'''
字符串方法补充
'''

# 居中填充
s = 'python'
s = s.center(20, '-')
print(s)

# 统计出现个数
print(s.count('th', 0, 3))

# 找到子串 '-------python-------'
ind = s.find('th')
print(ind)

# 按进制输出
s = '{:b}'.format(10)
print(s)

s = '{:o}'.format(10)
print(s)

s = '{:x}'.format(10)
print(s)

import random
# 字符串拼接 
s = 'beautiful'
l = list(s)
random.shuffle(l)
s = ''.join(l)
print(s)

s = ''.join(('haha', 'hehe', 'hihi'))
print(s)

s = ','.join('hello')
print(s)

# 替换
s = s.replace(',', '.')
print(s)

# 切割
res = s.split('.')
print(res)




