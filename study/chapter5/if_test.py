#检查是否相等
car = 'subaru'
print("1. Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("  Is car == 'audi'? I predict False.")
print(car == 'audi')

#检查是否不相等
pet = 'dog'
print("\n2. Is pet != 'subaru'? I predict True.")
print(pet != 'subaru')
print("   Is car != 'dog'? I predict False.")
print(pet != 'dog')

#比较数字
age = 21
print("\n3. Is age = 21? I predict True.")
print(age == 21)
print("   Is age != 21? I predict False.")
print(age != 21)
print("   Is age > 18 ? I predict True.")
print(age > 18)
print("   Is age > 25? I predict False.")
print(age > 25)
print("   Is age >= 20 ? I predict True.")
print(age > 18)
print("   Is age <= 18? I predict False.")
print(age > 25)

#使用and检查多个条件
number_1 = 18
number_2 = 23
print("\n4. Is number_1 > 16 and number_2 <= 25 ? I predict True.")
print(number_1 > 16 and number_2 <= 25)
print("   Is number_1 > 18 and number_2 <= 25 ? I predict False.")
print(number_1 > 18 and number_2 <= 25)

#使用or检查多个条件
number_1 = 18
number_2 = 23
print("\n5. Is number_1 > 16 or number_2 > 25 ? I predict True.")
print(number_1 > 16 or number_2 > 25)
print("   Is number_1 > 18 or number_2 > 25 ? I predict False.")
print(number_1 > 18 or number_2 > 25)

#检查特定值是否包含在列表中
pizzas = ['onion','chicken','cheese','beef','ham']
print("\n6. Is 'onion' in pizzas ? I predict True.")
print('onion' in pizzas)
print("   Is 'fruit' in pizzas ? I predict False.")
print('fruit' in pizzas)

#检查特定值是否不包含在列表中
pizzas = ['onion','chicken','cheese','beef','ham']
print("\n7. Is 'fruit' not in pizzas ? I predict True.")
print('fruit' not in pizzas)
print("   Is 'onion' not in pizzas ? I predict False.")
print('onion' not in pizzas)

#使用函数lower()的测试
fruit = 'Lemon'
print("\n8. Is fruit == 'lemon'? I predict False.")
print(fruit == 'lemon')
print("\n8. Is fruit.lower() == 'lemon'? I predict True.")
print(fruit.lower() == 'lemon')
