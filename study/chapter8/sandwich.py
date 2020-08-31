def make_sandwich(*toppings):
    """打印顾客点的所有配料"""
    print("\nYour sandwich is made by:"  )
    for topping in toppings:
        print("-" + topping)

make_sandwich('vegetable','beef','cheese')
make_sandwich('vegetable','beef')
make_sandwich('vegetable')
