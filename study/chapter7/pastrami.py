sandwich_orders = ['vegetable','pastrami','pastrami','beef','cheese','pastrami']
print(sandwich_orders)

print("There have no pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)