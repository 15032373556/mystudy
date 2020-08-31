pizzas = ['onion','chicken','cheese','beef','ham']

#创建副本
friend_pizzas = pizzas[:]

#在原列表中添加一种披萨
pizzas.append('fruit')

#在列表friend_pizzas中添加另一种披萨
friend_pizzas.append('durian')

#打印原列表
print('My favorite pizzas are:')
for pizza in pizzas:
    print(pizza)

#打印列表friend_pizzas
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)