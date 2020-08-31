msg = "请输入您的年龄,按'q'退出 "

age = ''
while age != 'q':
    age = input(msg)
    if age != 'q':
        if int(age) < 3 and int(age) > 0:
            print("免费")
        elif int(age) <= 12:
            print("票价为10美元")
        elif int(age) > 12:
            print("票价为15美元")



# while True:
#     age = input(msg)
#     if age == 'q':
#         break
#     else:
#         age = int(age)
#         if age < 3:
#             print("免费")
#         elif age <= 12:
#             print("票价为10美元")
#         elif age > 12:
#             print("票价为15美元")


# active = True
# while active:
#     age = input(msg)
#     if age == 'q':
#         active = False
#     else:
#         age = int(age)
#         if age < 3:
#             print("免费")
#         elif age <= 12:
#             print("票价为10美元")
#         elif age > 12:
#             print("票价为15美元")



