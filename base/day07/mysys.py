'''
sys模块
'''
import sys

def _add(a, b):
	return a + b

def _sub(a, b):
	return a - b

def _mul(a, b):
	return a * b

def _div(a, b):
	return a / b

def caculate(num1, num2, op):
	'''四则运算'''
	'''
	op_ls = ['+', '-', 'x', '/']
	fun_ls = [_add, _sub, _mul, _div]	
	for i in range(len(op_ls)):
		if op_ls[i] == op:
			return (fun_ls[i])(num1, num2)
	'''
	op_fun = {'+':_add, '-':_sub, 'x':_mul, '/':_div}
	for k in op_fun:
		if k == op:
			return (op_fun[k])(num1, num2)
	

# print(sys.argv)
if __name__ == '__main__':
	'''
	argv = sys.argv
	if len(argv) >= 4:
		res = caculate(int(argv[1]), int(argv[3]), argv[2])
		print('{} {} {} = {}'.format(argv[1], argv[2], argv[3], res))
	'''
	sys.exit(0) # 终止

	print(sys.builtin_module_names)




