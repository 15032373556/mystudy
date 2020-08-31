reponses = {}

#设置一个标志，指出调查是否继续
poll_active = True

while poll_active:
    #提示输入被调查者的名字和回答
    name = input('\nWhat is your name? ')
    reponse = input('Which mountain would you like to climb someday? ')

    #将答案存储在字典中
    reponses[name] = reponse

    #看看是否还有人要参与调查
    repeat = input('Would you like to let another person respond?(yes/no) ')
    if repeat == 'no':
        poll_active = False

#调查结束，显示结果
print('\n---Poll Results---')
for name,reponse in reponses.items():
    print(name + 'would like to climb ' + reponse + '.')