'''
python3的字符串:
	文本字符串(str)---->unicode
		''
		""
		''' '''
		str()
	二进制字符串(bytes)
		b''
		b""
		b''' '''
		bytes()
	编码:
		str--->bytes
		string.encode(encoding = 'utf-8')
	解码:
		bytes--->str
		bytestring.decode(encodeing = 'utf-8')

'''
s = 'python是最好的语言'
bs = s.encode()
print(type(bs))
print(bs)

bs2 = bytes(s, encoding='utf-8')
print(type(bs2))
print(bs2)

s1 = bs2.decode()
print(type(s1))
print(s1)

s2 = str(bs2, encoding='utf-8')
print(type(s2))
print(s2)









