responses = {}

#设置一个标志，指出调查是否继续
resort = True
while resort:
    #提示输入被调查者的名字和回答
    name = input("\nWhat your name? ")
    response = input("If you could visit one place in the world,where would you go?")

    #将答案存储在字典中
    responses[name] = response

    #看看是否还有人要参与调查
    repeat = input("Would you like another person respond?(Yes/No) ")
    if repeat == 'no':
        resort = False

#调查结束，显示结果
print("\n---resort results---" )
for name,response in responses.items():
    print(name.title() + " would like to go to " + response.title() + '.')
