
'''
time模块
'''
import time

# 时间戳
tm = time.time()
# 时间结构
ltime = time.localtime()
print(ltime.tm_year)
# 时间字符串
str_time = time.strftime("%Y-%m-%d %H:%M:%S", ltime)
print(str_time)


