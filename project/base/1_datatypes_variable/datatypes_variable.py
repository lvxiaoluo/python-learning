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

print('%3d-%02d' % (3,1))
print('%.2f' % 3.1415926)

# 字符串里面有%时,需要转义,用%%来表示一个%
print('growth rate: %d %%' % 7)

# format() 
print('Hello,{0},成绩提升了{1:.1f}%'.format('小明',17.125))

# f-string
r = 2.5
s= 3.14 * r ** 2
print(f'The area of a circle with radius {r} is {s:.2f}')

# 列表 list
classmates = ['Michael','Bob','Tracy']
print(classmates)
# len() 列表元素个数
print(len(classmates))

print(classmates[0])
print(classmates[1])
print(classmates[2])
# 索引超出了范围是,会报IndexError错误
# print(classmates[3])
# 获取最后一个元素，可以用 -1 做索引，直接获取最后一个元素
print(classmates[-1])
print(classmates[-2])
print(classmates[-3])
# 倒数第4个就会越界 IndexError: list index out of range
# print(classmates[-4])
# list中追加元素到末尾
classmates.append('Adam')
print(classmates)
# 把元素插入到指定位置
classmates.insert(0,'Jack')
print(classmates)
# 删除list末尾的元素，用pop()方法
print(classmates.pop())
print(classmates)
# 删除指定位置元素，使用pop(i)方法，其中i是索引位置
print(classmates.pop(1))
print(classmates)
# 把某个元素替换成别的元素，直接赋值对应的索引位置
classmates[1] = 'Sarah'
print(classmates)
# list里面的元素数据类型也可以不同
L = ['Apple',123,True]
print(L)
# list元素也可以是另一个list
s = ['Python','Java',['asp','php'],'scheme']
print(s)
print(len(s))
p = ['asp','php']
s = ['Python','Java',p,'scheme']
print(p)
print(s)
print(p[1])
print(s[2][1])

# tuple 有序列表元组.tuple一旦初始化就不能修改
classmates = ('Michael','Bob','Tracy')
print(classmates)
# 括号()既可以表示tuple,又可以表示数学公式中的小括号,因此Python规定这种情况下,按小括号进行计算,计算结果自然是1
# 所以只有1个元素的tuple定义时必须加一个逗号, 来消除歧义
t = (1,)
print(t)
# tuple所谓的不变是说,tuple的每个元素,指向永远不变.
t = ('a','b',['A','B'])
print(t)
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)