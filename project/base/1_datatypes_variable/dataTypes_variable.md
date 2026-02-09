### 1.语法
1. 开头是注释 
2. :冒号结尾时，缩进的语句视为代码块  应该始终坚持使用 4 个空格缩进
3. Python程序时大小写敏感的

### 2.数据类型和变量
#### 2.1 整数
1.python允许在数字中间以 _  分割
#### 2.2 浮点数
1.浮点数也是就是小数
> 很大或者很小的浮点数，必须用科学计数法标识 ，把10用e替代，1.23x10 就是 1.23e9；0.000012可以写成 1.2e-5
Python的浮点数没有大小限制,但是超出一定范围就直接表示为 inf （无限大）

#### 2.3 字符串

1. 字符串时以单引号 ' 或 双引号 " 括起来的任意文本；如果 ' 本身也是一个字符，那就可以用 "" 括起来；如果字符串内部既包含 ' 又包含 "，可以用转义字符\来标识，例如：'I\'m \"OK\"!'
2.转义符 \n 表示换行，\t 表示制表符，字符\本身也要转义，所以\\表示的字符就是\

#### 2.4 布尔值
1. 布尔值只有 True、False 两种值，要么是 True，要么是 False，在 Python 中，可以直接用 True、False 表示布尔值（请注意大小写）
2. 布尔值可以用 and、or 和 not 运算。
and - 与运算 ,所有都为True时，结果才为True
or - 或运算,只要其中有一个为True,结果就为True
not - 逻辑非运算,如果为True,结果为False,如果为False,结果为True

#### 2.5 空值
1. 空值是Python里一个特殊的值，用 None 表示。None 不能理解为 0，因为 0 是有意义的，而 None 是一个特殊的空值。
2. 变量中没有被赋值时，默认值为 None

### 3.变量
变量名必须是大小写英文、数字和下划线 _ 的组合，且不能用数字开头

在Python中,等号 = 是赋值语句,可以把任意数据类型赋值给变量,同一个变量可以反复赋值,而且可以是不同类型的变量

变量本身类型不固定的语言称之为 动态语言,与之对应的是静态语言

### 4.常量
常量是不能变的变量,Python中通常用全部大写的变量名表示常量


### 5.Python字符串
1. ord() 函数获取字符的整数表示
2. chr() 函数把编码转换为对应的字符
3. len() 函数获取字符串的长度

### 6.格式化输出
6.1 在Python中,格式化输出时,可以用 % 操作符,也可以用 format() 方法
% 运算符就是用来格式化字符串的,在字符串内部,%s表示用字符串替换,%d表示用整数替换,有几个%?占位符,后面就跟几个变量或值.如果只有一个%?,括号可以忽略
常见的占位符有：
%d - 整数
%f - 浮点数
%s - 字符串
%x - 十六进制整数

格式化整数和浮点数还可以指定是否补0 和 整数与小数的位数

如果字符串里面%是一个普通字符需要转义,用%%来表示一个%

6.2 format() 格式化字符串,依次替换字符串内的占位符 {0} {1} ......

6.3 f-string,格式化字符串以f开头的字符串,称之为f-string,字符串如果包含{xxx},会以对应的变量替换

### 7.列表
#### 7.1 list列表
1.list是一种有序集合,可随时添加和删除其中的元素
2.索引超出范围,Python会报IndexError错误,最后一个元素索引是len(list)-1
3.list获取最后一个元素除了计算索引位置外,可以用-1做索引
4.pop()方法删除list末尾的元素,pop(i)删除指定位置的元素
5.替换元素,直接赋值给对应索引位置即可
#### 7.2 tuple元组
tuple是一种有序集合,tuple一旦创建,就无法被修改
> classmates = ('Michael','Bob','Tracy')

### 8.条件判断
8.1 两个分支判断
if 条件:
    执行语句1
else:
    执行语句2

if判断是True 执行  ，False则执行 else 语句

8.2 多个分支判断
if 语句执行从上往下判断，如果在某个判断上是Ture，把该判断对应得语句执行后，就会忽略剩下得elif 和 else 语句。


if 条件1:
    执行语句1
elif 条件2:
    执行语句2
else:
    执行语句3


if 判断条件还可以简写，比如写：
if x:
    print('True')

只要 x 是非零数值、非空字符串、非空list等，就判断为True,否则为False


input() 返回的数据类型时str ,str 不能直接和整数比较，需要转成整数

### 9.模式匹配
当我们用 if ... elif ... elif ... else ... 判断时，会写很长一串代码，可读性差
针对某个变量匹配若干种情况，可以使用match语句
```python
score = 'B'
match score:
    case 'A':
        print('score is A.')
    case 'B':
        print('score is B.')
    case 'C':
        print('score is C.')
    case _:
        print('Invalid score.')
```

#### 9.1 复杂匹配
match 语句除了可以匹配简单的单个值外，还可以匹配多个值、匹配一定范围。并且把匹配后的值绑定到变量
```python
age = 15
match age:
    case x if x < 10:
        print(f'<10 years old:{x}')
    case 10:
        print('10 years old.')
    case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 :
        print('11~18 years old.')
    case 19:
        print('19 years old.')
    case _:
        print('not sure.')
```
match 可以匹配列表

```python
args = ['gcc','hello.c','world.c']
match args:
    case ['gcc']:
        print('gcc:missing source file(s)')
    case ['gcc',file1,*files]:
        print('gcc compile:'+file1+','+','.join(files))
    case ['clean']:
        print('clean')
    case _:
        print('invalid command')
```
第一个 case['gcc']表示列表仅有 'gcc' 一个字符串，没有指定文件名，报错
第二个 case['gcc',file,*files] 表示第一个字符串是'gcc'，第二个字符串绑定到变量 file1,后面的任意个字符串绑定到 *files，它实际上表示至少一个文件；
第三个 case['clean']表示列表仅有 'clean' 一个字符串；
最后一个 case _ 表示所有的情况。


### 10.循环
python循环有两种，一种是 for...in循环，依次把list 或者 tuple种的每个元素迭代出来

```python
names = ['Michael','Bob','Tracy']
for name in names:
    print(name)
```

```python
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n -2
print(sum)
```