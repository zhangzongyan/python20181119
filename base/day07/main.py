'''验证模块的使用'''
__author__='zhangzongyan'

# import pag.moduler as pm
# from pag.moduler import _test
from pag.moduler import * # 私有函数(_或__开头的函数)没导入
import hw
import sys

if __name__ == '__main__':
	print(__name__)
	print(__doc__)
	print(__author__)

	# 得到模块的搜索路径
	print(sys.path)

	# pm._test()
	test()

