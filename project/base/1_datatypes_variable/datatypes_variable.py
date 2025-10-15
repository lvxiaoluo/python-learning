print(30*1500*12)
print('I\'m \"OK\"!')
print('I\'m learning\nPython.')
# 如果字符串里面有很多字符都需要转义，需要加很多 \
print('\\\t\\')
#  为了简化，Python允许用 r'' 表示 '' 内部的字符串默认不转义
print(r'\\\t\\')
# 如果字符串内部很多换行,Python允许用三引号'''...'''的格式表示多行内容
print('''line1
line2
line3''')
print('line1 \
line2 \
line3')

print(r'''hello,\n
world''')

# 布尔类型
print(True)
print(False)
print(3>2)
print(3>5)

age = 20
if age >= 18:
    print('adult')
else:
    print('teenager')


# 变量
a = 'ABC'
b = a
a = 'XYZ'
print(b)

print(10/3)
print(9/3)

# // 地板除 ,两个整数的除法仍然是整数,整数的地板除 // 永远是整数,即使除不尽.要做精度的除法使用/
print(10//3)
# 余数运算
print(10%3)


s4 = r'''Hello,
Bob!'''
print(s4)

print(ord('A'))
print(ord('中'))
print(chr(66))
print(chr(25991))

print('\u4e2d\u6587')


print('ABC'.encode('ascii'))

print('中文'.encode('utf-8'))

# 因为中文编码的范围超过了ASCII编码的范围,Python会报错
# print('中文'.encode('ascii'))

print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

# 如果bytes 中只有一小部分无效的字节,可以传入 errors='ignore'忽略错误的字节
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))

# 计算str包含多少个字符,可以用len()函数
print(len('ABC'))
print(len('中文'))

# 格式化输出
print('Hello, %s' % 'world')
print('Hi,%s,you have $%d.' % ('Michael', 1000000))

print('Hi,%s,you have $%d.' %('Bob', 999999))