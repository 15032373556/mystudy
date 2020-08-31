# re模块使用
'''
import re
s1 = '我12345abcde'
s2 = '.12345abcde'
s3 = '+?@!12345abcde'
pattern = r'\w+'
pattern_compile = re.compile(pattern)
# result1 = re.match(pattern,s1)
# result2 = re.match(pattern,s2)
result1 = re.search(pattern_compile,s1)
result2 = re.search(pattern_compile,s3)
print(result1)
print(result2)

s1 = '我12345abcde'
s2 = '+?@!12345abcde@786ty'
pattern = r'\d+'
pattern_compile = re.compile(pattern)
result1 = re.match(pattern_compile,s2)
result2 = re.search(pattern_compile,s1)
result3 = re.findall(pattern_compile,s2)
print(result1)
print(result2)
print(result3)

s1 = '我12345+abcde'
pattern = r'(\w+)\+(\w+)'
pattern_compile = re.compile(pattern)
result1 = re.match(pattern_compile,s1).group()
# result2 = re.match(pattern_compile,s1).start()
# result3 = re.match(pattern_compile,s1).end()
# result4 = re.match(pattern_compile,s1).span()
result2 = re.match(pattern_compile,s1).group(1)
result3 = re.match(pattern_compile,s1).group(2)
result4 = re.match(pattern_compile,s1).groups()
print(result1)
print(result2)
print(result3)
print(result4)

s1 = '我12345+aBCde'
pattern = r'(\w+)\+(\w+)'
pattern_compile = re.compile(pattern,re.IGNORECASE)
result1 = re.findall(pattern_compile,s1)
print(result1)

s1 = '我12345+aBCde'
pattern = r'(\w+)\+(\w+)'
result1 = re.findall(pattern,s1,re.IGNORECASE)
print(result1)
'''

# BeautifulSoup
'''
from bs4 import BeautifulSoup
import bs4

soup = BeautifulSoup('<b class="boldest">Extremely bold</b>','html5lib')
tag = soup.b
print(type(tag))
print(tag.name)
print(tag.attrs)
print(tag['class'])
print(tag.string)
tag.string.replace_with('no longer bold')
print(tag)
print(soup.name)

markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
soup = BeautifulSoup(markup,'html5lib')
# comment = soup.b.string
# print(type(comment))
# print(comment)
if type(soup.b.string) == bs4.element.Comment:
    print(soup.b.string)
    
# 遍历文档树
from bs4 import BeautifulSoup
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>

<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
and<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc,'html5lib')
print(soup.head.contents)    # 子节点
print(soup.body.contents)    # content属性可以将标签所有子节点以列表形式返回
print(soup.body.children)     # 返回的children是一个生成器（generator）
for child in soup.body.children:
    print(child)
for child in soup.head.descendants:        # 子孙节点
    print(child)
print(soup.title.parent)       # 父节点
print(soup.title.parent.name)
for parent in soup.a.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)
a_tag = soup.find("a", id="link1")
# print(a_tag.next_sibling)         # 兄弟节点
# print(a_tag.previous_element)
print(a_tag.next_element)          # 回退和前进
print(a_tag.previous_element)
for elem in a_tag.next_elements:
    if elem.name is None:
        continue
    else:
        print(elem.name)
 
        
# 搜索文档树
from bs4 import BeautifulSoup
import re
html_doc = """同上"""
soup = BeautifulSoup(html_doc,'html5lib')
print(soup.find_all('a'))
print(soup.find_all(id='link2'))
for tag in soup.find_all(re.compile('^t')):
    print(tag.name)
print(soup.find_all(id='link2'))
print(soup.find_all(href=re.compile('elsie')))
print(soup.find_all(href=re.compile('elsie'),id='link1'))
print(soup.find_all(text='Elsie'))
print(soup.find_all(text=re.compile('Dormouse')))
print(soup.find_all('a',limit=2))
print(soup.find_all('title'))
print(soup.find_all('title',recursive=False))
'''
