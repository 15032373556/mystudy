#创建任意数量的实参
#形参名*toppings中的星号让Python创建一个名为toppings的空元组
def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print('\nMaking a pizza with the following toppings:')
    for topping in toppings:
        print('-' + topping)

make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')