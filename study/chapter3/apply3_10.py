favorites = ['china','yun nan','sea','mountain','fruit','meat','movies','toys','milk']
print('\n原始列表')
print(favorites)

print('\n在列表末尾添加元素')
favorites.append('animals')
print(favorites)

print('\n在列表中插入元素')
favorites.insert(1,'boyfriend')
print(favorites)

print('\n在列表中删除元素')
del favorites[3]
print(favorites)

print('\n使用pop()删除元素')
pop_1 = favorites.pop(-2)
print(pop_1 + ' is hard for me to drink.')
print(favorites)

print('\n根据值删除元素')
favorites.remove('meat')
print(favorites)

print('\n对列表按字母顺序进行临时排序')
print(sorted(favorites))

print('\n对列表按字母相反顺序进行临时排序')
print(sorted(favorites,reverse=True))

print('\n对列表按字母顺序进行永久性排序')
favorites.sort()
print(favorites)

print('\n反转列表元素的排列顺序')
favorites.reverse()
print(favorites)

print('\n获取列表长度')
print(len(favorites))