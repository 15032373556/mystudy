from collections import OrderedDict

word_list = OrderedDict()

word_list['title'] = '将首字母大写'
word_list['len()'] = '确定列表的长度'
word_list['sort'] = '永久性排序'
word_list['del'] = '删除'
word_list['append'] = '在末尾添加元素'
word_list[ 'strip'] ='删除首尾空行'
word_list['insert'] ='在任意位置添加新元素'
word_list['str'] ='将其他类型转换为字符串类型'
word_list['pop'] ='删除列表末尾的元素，并可接着使用'
word_list['remove'] ='根据值删除元素'

for key,value in word_list.items():
    print(key + ':' + value)