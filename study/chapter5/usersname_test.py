current_users = ['ecic','admin','ALBERT','bob','jenny','david']
new_users = ['ecic','lucy','Albert','tom','jack']

#将列表中元素全部转换为小写
current_users1 = [line.lower() for line in current_users]
print(current_users1)

#检查用户名
for user in new_users:
    if user.lower() in current_users1:
        print('Please input other user-name.')
    else:
        print('The user-name have not been used.')