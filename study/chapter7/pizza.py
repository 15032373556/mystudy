msg = "请输入披萨配料，按‘quit'可随时退出"

# while True:
#     pizza_topping = input(msg)
#     if pizza_topping == 'quit':
#         break
#     else:
#         print("我们会在披萨中添加" + pizza_topping + "配料。")


# active = True
# while active:
#     pizza_topping = input(msg)
#     if pizza_topping == 'quit':
#         active = False
#     else:
#         print("我们会在披萨中添加" + pizza_topping + "配料。")

pizza_topping = ''
while pizza_topping != 'quit':
    pizza_topping = input(msg)
    print("我们会在披萨中添加" + pizza_topping + "配料。")