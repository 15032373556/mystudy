pizzas = ['onion','chicken','cheese','beef','ham']

#打印前三
print('The first three items in the list are: ')
for pizza in pizzas[:3]:
    print(pizza)

#打印中间三个
print('\nThree items from the middle of the list are: ')
for pizza in pizzas[1:4]:
    print(pizza)

#打印后三
print('\nThe last three items in the list are: ')
for pizza in pizzas[-3:]:
    print(pizza)