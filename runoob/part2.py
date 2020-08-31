def reverseWords(input):
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    inputWords = input.split(" ")

    # 翻转字符串
    # 假设列表 list = [1,2,3,4],
    # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    inputWords = inputWords[-1::-1]
    # 重新组合字符串
    output = ' '.join(inputWords)
    return output

# 加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vartuple)

# 加了两个星号 ** 的参数会以字典的形式导入
def printinfo(arg1, **vardict):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vardict)

# python 使用 lambda 来创建匿名函数
'''
sum = lambda arg1, arg2: arg1 + arg2

# 调用sum函数
print("相加后的值为 : ", sum(10, 20))
print("相加后的值为 : ", sum(20, 20))
'''

# 嵌套列表解析
'''
matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
 ]

print([[row[i] for row in matrix] for i in range(4)])     # 方法一

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])    # 方法二
print(transposed)

transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)       # 方法三
print(transposed)
'''

# 模块
'''
import sys

print('命令行参数如下:')
for i in sys.argv:
    print(i)

print('\n\nPython 路径为：', sys.path, '\n')
'''

# 输入输出
'''

for i in range(10):
    print(repr(i).rjust(1),repr(i**2).rjust(2),repr(i**3).rjust(3))
    
for i in range(10):
    print('{0:d} {1:2d} {2:3d}'.format(i,i**2,i**3))

# format    
print('{} 和 {}'.format('Google', 'Runoob'));
print('{1} 和 {0}'.format('Google', 'Runoob'));
print('{name} 和 {site}'.format(name='Google',site='Runoob'));
import math
print('pi的值为 {!r}'.format(math.pi));
print('pi的值为 {0:.3f}'.format(math.pi))

table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
for name, number in table.items():
   print('{0:10} ==> {1:10d}'.format(name, number))
   print('Google:{0[Google]:d} Runoob:{0[Runoob]:d} Taobao:{0[Taobao]:d}'.format(table))
   print('Google:{Google:d} Runoob:{Runoob:d} Taobao:{Taobao:d}'.format(**table))
   
f = open('example.txt',encoding='utf-8')
str = f.read();print(str);
str1 = f.readline();print(str1);
str2 = f.readlines();print(str2);
for line in f.readlines():
    print(line,end='')
f.close()

f = open('example.txt','w',encoding='utf-8')
num = f.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n")
print(num)
f.close()

f = open('example.txt','rb+')
f.write(b'0123456789abcdef')
print(f.seek(5));print(f.read(1));
print(f.seek(-3,2));print(f.read(1));
f.close()

f = open('example.txt','rb+')
print(f.tell())
'''

# 类
'''
# 1
class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0  # 公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)


counter = JustCounter()
counter.count()
counter.count()
print(counter.publicCount)
print(counter.__secretCount)  # 报错，实例不能访问私有变量

# 2
class Site:
    def __init__(self, name, url):
        self.name = name  # public
        self.__url = url  # private

    def who(self):
        print('name  : ', self.name)
        print('url : ', self.__url)

    def __foo(self):  # 私有方法
        print('这是私有方法')

    def foo(self):  # 公共方法
        print('这是公共方法')
        self.__foo()


x = Site('菜鸟教程', 'www.runoob.com')
x.who()  # 正常输出
x.foo()  # 正常输出
x.__foo()  # 报错


# 3
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)

v2 = Vector(5, -2)
print(v1+v2)
'''

# 标准库概览
'''
import re            #字符串正则匹配
print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'));
print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'));
print( 'tea for too'.replace('too', 'two'))

from urllib.request import urlopen           #访问互联网
for line in urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
    line = line.decode('utf-8')           # Decoding the binary data to text.
    if 'EST' in line or 'EDT' in line:      # look for Eastern Time
        print(line)
        
        
from datetime import date   # 日期和时间
now = date.today()
print(now)
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))
birthday = date(1964,7,31)
age = now - birthday
print(age.days)

import zlib          # 数据压缩
s = b'witch which has which witches wrist watch'; print(len(s))
t = zlib.compress(s); print(len(t))
a = zlib.decompress(t); print(a)
b = zlib.crc32(s); print(b)

from timeit import Timer    # 性能度量
print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
print(Timer('a,b = b,a', 'a=1; b=2').timeit())

def average(values):    # 测试模块
    return sum(values) / len(values)

import doctest
doctest.testmod()   # 自动验证嵌入测试


import unittest

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        self.assertRaises(ZeroDivisionError, average, [])
        self.assertRaises(TypeError, average, 20, 30, 70)

unittest.main() # Calling from the command line invokes all tests
'''

# 正则表达式
'''
import re
print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配

line = "Cats are smarter than dogs"
# .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
else:
    print("No match!!")


import re
print(re.search('www','www.runoob.com').span())      # 在起始位置匹配
print(re.search('com','www.runoob.com').span())      # 不在起始位置匹配

line = "Cats are smarter than dogs"
searchObj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)

if searchObj:
    print("searchObj.group() : ", searchObj.group())
    print("searchObj.group(1) : ", searchObj.group(1))
    print("searchObj.group(2) : ", searchObj.group(2))
else:
    print("Nothing found!!")
    
    
import re
phone = "2004-959-559 # 这是一个电话号码"
# 删除注释
num = re.sub(r'#.*$', "", phone)
print("电话号码 : ", num)
# 移除非数字的内容
num = re.sub(r'\D', "", phone)
print("电话号码 : ", num)

import re
# 将匹配的数字乘于 2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)
s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))


import re
pattern = re.compile(r'\d+')                    # 用于匹配至少一个数字
m = pattern.match('one12twothree34four')        # 查找头部，没有匹配
print( m )
m = pattern.match('one12twothree34four', 2, 10) # 从'e'的位置开始匹配，没有匹配
print( m )
m = pattern.match('one12twothree34four', 3, 10) # 从'1'的位置开始匹配，正好匹配
print( m )                                        # 返回一个 Match 对象
print(m.group(0))   # 可省略 0
print(m.start(0))   # 可省略 0
print(m.end(0))     # 可省略 0
print(m.span(0))    # 可省略 0

import re
pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)   # re.I 表示忽略大小写
m = pattern.match('Hello World Wide Web')
print(m)                                     # 匹配成功，返回一个 Match 对象
print(m.group(0))                            # 返回匹配成功的整个子串
print(m.span(0))                             # 返回匹配成功的整个子串的索引
print(m.group(1))                            # 返回第一个分组匹配成功的子串
print(m.span(1))                             # 返回第一个分组匹配成功的子串的索引
print(m.group(2))                            # 返回第二个分组匹配成功的子串
print(m.span(2))                             # 返回第二个分组匹配成功的子串索引
print(m.groups())                            # 等价于 (m.group(1), m.group(2), ...)
print(m.group(3))                            # 不存在第三个分组


import re

pattern = re.compile(r'\d+')  # 查找数字
result1 = pattern.findall('runoob 123 google 456')
result2 = pattern.findall('run88oob123google456', 0, 10)
print(result1)    # 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表
print(result2)

it = re.finditer(r"\d+", "12a32bc43jf3")   # 在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回
for match in it:
    print(match.group())
    
import re
print(re.split('\W+', 'runoob, runoob, runoob.'))
print(re.split('(\W+)', ' runoob, runoob, runoob.'))
print(re.split('\W+', ' runoob, runoob, runoob.', 1))
print(re.split('a*', 'hello world'))  # 对于一个找不到匹配的字符串而言，split 不会对其作出分割
'''

# time
'''
import time

print("---RUNOOB EXAMPLE ： Loading 效果---")

print("Loading",end = "")
for i in range(20):
    print(".",end = '',flush = True)
    time.sleep(0.5)
    
    
import time

scale = 50

print("执行开始".center(scale//2,"-"))  # .center() 控制输出的样式，宽度为 25//2，即 22，汉字居中，两侧填充 -

start = time.perf_counter() # 调用一次 perf_counter()，从计算机系统里随机选一个时间点A，计算其距离当前时间点B1有多少秒。
# 当第二次调用该函数时，默认从第一次调用的时间点A算起，距离当前时间点B2有多少秒。两个函数取差，即实现从时间点B1到B2的计时功能。
for i in range(scale+1):
    a = '*' * i             # i 个长度的 * 符号
    b = '.' * (scale-i)  # scale-i） 个长度的 . 符号。符号 * 和 . 总长度为50
    c = (i/scale)*100  # 显示当前进度，百分之多少
    dur = time.perf_counter() - start    # 计时，计算进度条走到某一百分比的用时
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end='')  # \r用来在每次输出完成后，将光标移至行首，
    # 这样保证进度条始终在同一行输出，即在一行不断刷新的效果；{:^3.0f}，输出格式为居中，占3位，小数点后0位，浮点型数，对应输出的数为c；
    # {}，对应输出的数为a；{}，对应输出的数为b；{:.2f}，输出有两位小数的浮点数，对应输出的数为dur；end=''，用来保证不换行，不加这句默认换行。
    time.sleep(0.1)     # 在输出下一个百分之几的进度前，停止0.1秒
print("\n"+"执行结果".center(scale//2,'-'))
'''



