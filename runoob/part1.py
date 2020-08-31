import math
import random

# 输出函数的注释
"""
def a():
    '''这是文档字符串'''
    pass                 
print(a.__doc__)
"""

# end关键字
'''
a,b = 0,1
while b < 500:
    print(b,end=',')
    a,b = b,a + b
'''

# 数学函数
'''
print(math.pow(10,2));print(pow(10,2))
print(9//2); print(-9//2)          #取整除 - 向下取接近商的整数
print(abs(10));print(math.fabs(10))
print(math.modf(10.12))            # 返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示
x = 8;y = 10; print( (x>y)-(x<y) ) # 如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1
'''

# 位运算符
'''
a = 60    # 60 = 0011 1100; b = 13    # 13 = 0000 1101
c = a & b   # 12 = 0000 1100; print("1 - c 的值为：", c)
c = a | b   # 61 = 0011 1101; print("2 - c 的值为：", c)
c = a ^ b   # 49 = 0011 0001; print("3 - c 的值为：", c)
c = ~a      # -61 = 1100 0011; print("4 - c 的值为：", c)
c = a << 2  # 240 = 1111 0000; print("5 - c 的值为：", c)
c = a >> 2  # 15 = 0000 1111; print("6 - c 的值为：", c)
'''

# 随机数函数
'''
print(random.choice(range(10)));print(random.choice([1,3,6,12,9,0]))
print(random.choice('runoob'))    # choice() 方法返回一个列表，元组或字符串的随机项
print(random.randrange(0,100,4))  # random.randrange ([start,] stop [,step])
print(random.random())            # random() 方法返回随机生成的一个实数，它在[0,1)范围内
print(random.uniform(3,9))        # uniform() 方法将随机生成下一个实数，它在 [x,y] 范围内
list1 = [3,1,23,12,6]; random.shuffle(list1);print(list1)   # shuffle() 方法将序列的所有元素随机排序
'''

# 进制
'''
print(chr(0x30), chr(0x31), chr(0x61))   # 十六进制,chr返回值是当前整数对应的 ASCII 字符
print(chr(48), chr(49), chr(97))         # 十进制
print(ord('a'),ord('b'),ord('c'))        # 返回值是对应的十进制整数

print(hex(12),hex(-255))        # 用于将10进制整数转换成16进制，以字符串形式表示
print(oct(10),oct(42))          # 将一个整数转换成8进制字符串
'''

# 字符串内建函数
"""
str = 'hello,python'
print(str.capitalize())
print(str.center(40));print(str.center(40,'*'));print(str.center(4))
print(str.count('o'));print(str.count('o',0,6));print(str.count('th'))
print(str.endswith('on'));print(str.endswith('th'));print(str.endswith('yt',0,9));
str = 'hello,\tpython';print(str);print(str.expandtabs());print(str.expandtabs(16))
print(str.find('o'));print(str.find('e',0));print(str.find('e',3))
print(str.index('th'));print(str.index('th',0,10));print(str.index('po'));
str = "runoob2016" ;print(str.isalnum());str = "www.runoob.com";print(str.isalnum());
str = "runoob";print (str.isalpha());str = "runoob菜鸟教程";print (str.isalpha())
str = "Runoob example....wow!!!";print (str.isalpha())
str = '1013455';print(str.isdigit());str = "Runoob example....wow!!!";print(str.isdigit())
str = "RUNOOB example....wow!!!";print (str.islower());str = "runoob example....wow!!!";print (str.islower());
str = "runoob2016" ;print (str.isnumeric());str = "23443434";print (str.isnumeric());
s = '\u00B23455';print(s.isnumeric());  # s = '²3455'
s = '\u00BD';print(s.isnumeric());      # s = '½'
a = "\u0030" ;print(a.isnumeric());     # unicode for 0
b = "\u00B2";print(b.isnumeric());      # unicode for ²
c = "10km2";print(c.isnumeric())
str = '           ';print(str.isspace());str = '1233abcd';print(str.isspace())
str = "This Is String Example...Wow!!!";print(str.istitle())
str = "This is string example....wow!!!";print(str.istitle())
str = "THIS IS STRING EXAMPLE....WOW!!!";print (str.isupper());
str = "THIS is string example....wow!!!";print (str.isupper());
s1 = '-';s2 = '';seq = ('h','e','l','l','o');print(s1.join(seq));print(s2.join(seq))
str1 = 'hello,python';print(len(str1));list1 = [1,3,6];print(len(list1))
str = "This is string example....wow!!!";print(str.ljust(60,'@'));
str = "        string example....wow!!!";print(str.lstrip());
str = "This is string example....wow!!!";print(str.lstrip('This'));
str = "This is string example....wow!!!";print(str.lstrip('this'));
intab = "aeiou";outtab = "12345";trantab = str.maketrans(intab,outtab);
str = "this is string example....wow!!!";print(str.translate(trantab))
d = {'h':'1','t':'2','c':'3','d':'4','n':'5'};trantab = str.maketrans(d);str = 'hello,python';print(str.translate(trantab));
x = 'abcdefs';y='1234567';z='ot';st='just do it';trantab = str.maketrans(x,y,z);print(st.translate(trantab))
x = 'abst';y = '1234';z = 's';st = 'just do it';trantab = str.maketrans(x,y,z);print(st.translate(trantab))
str = "this is string example....wow!!!";print(str.replace(str,'hello'));
str = "this is string example....wow!!!";print(str.replace('  is','was',3))
str = "this is string example....wow!!!";print(str.split( ));print(str.split('i'));print(str.split('w',1));
print('ab c\n\nde fg\rkl\r\n'.splitlines());print('ab c\n\nde fg\rkl\r\n'.splitlines(True));
str = "this is string!!!";print(str.swapcase());str = "This Is String";print(str.swapcase())；
# str = "菜鸟教程";
# str_utf8 = str.encode("UTF-8");str_gbk = str.encode("GBK")
# print(str);print("UTF-8 编码：", str_utf8);print("GBK 编码：", str_gbk)
# print("UTF-8 解码：", str_utf8.decode('UTF-8', 'strict'));print("GBK 解码：", str_gbk.decode('GBK', 'strict'))
"""

# set 与set 集合内置方法
'''
x = set('runoob'); y = set('google')       # set删除重复数据
print(x & y) # 计算交集;  
print(x | y) # 计算并集;  
print(x - y) # 计算差集

thisset = set(("Google", "Runoob", "Taobao"));
print('1' in thisset);print('Runoob' in thisset);
thisset.add('Facebook');thisset.update({1,3});
thisset.remove('Runoob');thisset.discard('Google');
thisset.pop();print(len(thisset));
thisset.clear(); print(thisset);

thisset = set(("Google", "Runoob", "Taobao"));x = thisset.copy();
y = set(("Google", "Run", "Facebook"));z = set(('A','c','f'));w = set(('c','f'));
print(x.difference(y) );  x.difference_update(y);print(x);
print(x.intersection(y)); x.intersection_update(y);print(x);
print(x.isdisjoint(y)); print(x.isdisjoint(z));
print(y.issubset(x)); rint(w.issubset(z)); print(z.issuperset(w));print(w.issuperset(z));
print(x.symmetric_difference(y)); x.symmetric_difference_update(y);print(x);
print(x.union(y));
'''

# 构造字典 及 字典内置函数
'''
dict1 = dict()                        # 创建空字典
dict2 = dict(a='a', b='b', t='t')     # 传入关键字
dict3 = dict(zip(['one', 'two', 'three'], [1, 2, 3]))   # 映射函数方式来构造字典
dict4 = dict([('one', 1), ('two', 2), ('three', 3)])    # 可迭代对象方式来构造字典
print(dict1,'\n',dict2,'\n',dict3,'\n',dict4)

# 字典内置函数
dict = {'Name': 'Zara', 'Age': 7}
print(len(dict));dict.clear();print(len(dict))
dict1 = {'user': 'runoob', 'num': [1, 2, 3]}
dict2 = dict1  # 浅拷贝: 引用对象
dict3 = dict1.copy()  # 浅拷贝：深拷贝父对象（一级目录），子对象（二级目录）不拷贝，还是引用
dict1['user'] = 'root'; dict1['num'].remove(1)      # 修改 data 数据
print(dict1);print(dict2);print(dict3)        # 输出结果
seq = ('a','b','c'); dict = dict.fromkeys(seq);print(dict);dict = dict.fromkeys(seq,10);print(dict);
dict = {'Name': 'Zara', 'Age': 7};dict1 = {'Sex': '男'}
print(dict.get('Age')); print('Name' in dict);print('name' not in dict);print(dict.items());
print(dict.keys());print(list(dict.keys()));print(dict.values());print(list(dict.values()));
print(dict.setdefault('Name',None));print(dict.setdefault('Sex',None));dict.update(dict1);print(dict)
pop0 = dict.pop('Name');print(pop0); pop_obj = dict.popitem();print(pop_obj);print(dict)
'''

# 创建不可变集合
'''
# a = frozenset(range(10)); print(a)      # 生成一个新的不可变集合
# b = frozenset('google');print(b)      
'''

# 将可迭代系列转换为元组、列表
'''
list1 = ['a','hello','5']
tuple1 = tuple(list1)  #将序列list1转换为一个元组;print(tuple1)
tuple1 = ('a','hello','5')
list1 = tuple(tuple1)  #将序列tuple1转换为一个列表;print(list1)
str1 = 'Hello,world'
list2 = list(str1)     #将序列str1转换为一个列表;print(list2)
'''

# 迭代器与生成器
'''
list = [1,2,3,4]    # 迭代器1
it = iter(list);  # 创建迭代器对象
print(next(it));print(next(it))   # 输出迭代器的下一个元素
for i in it:
   print(i,end=',')

   
import sys    # 迭代器2
list = [1,2,3,4]
it = iter(list);  # 创建迭代器对象
while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()
        
class MyNumbers():     # 迭代器3

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a; self.a += 1
            return x
        else:
            raise StopIteration
myclass = MyNumbers();        myiter = iter(myclass);
# print(next(myiter));print(next(myiter));print(next(myiter));print(next(myiter));
for x in myiter:
    print(x,end=' ')
    
    
import sys          # 生成器
def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1

f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成
while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()
'''











