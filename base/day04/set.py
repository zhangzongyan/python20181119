
'''
集合(set):无序的不重叠的可变的
	去除重复
'''
# 定义
st = {1,2,3,4}
print(type(st))
print(st)

# 去重
l = [1,2,3,3,2,34,1,23]
l = list(set(l))
print(l)

for i in st:
	print(i)

st.add(100)
print(st)

st.pop()
print(st)

st.remove(100)
print(st)

st2 = {2,1,8,9,4}
print(st & st2) # 交集
print(st | st2) # 并集
print(st - st2) # 差集
print(st ^ st2) # 交叉差集





