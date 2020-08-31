question = input("请输入您的用餐人数：")

number = int(question)
if number > 8:
    print("抱歉，没有空桌。")
else:
    print("有空桌。")