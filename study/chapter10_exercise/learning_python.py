filename = 'learning_python.txt'

# #读取整个文件
# with open(filename) as ly:
#     contents = ly.read()
#     print(contents)

# #遍历文件对象
# with open(filename) as ly:
#     for line in ly:
#         print(line)

# #将各行存储在一个列表中，在with代码块外打印他们
# with open(filename) as ly:
#     lines = ly.readlines()
#
# for line in lines:
#     print(line)

#replace()替换字符串中特定的单词
with open(filename) as ly:
    lines = ly.readlines()

for line in lines:
    msg = line.replace("python","C")
    print(msg)

