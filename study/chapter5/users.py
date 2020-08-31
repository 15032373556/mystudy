users = ['admin','albert','bob','jenny','david']

for user in users:
    if user == 'admin':
        print('Hello admin,would you like to see a status report?')
    else:
        print('\nHello ' + user.title() + ',thank you for logging in again.')

# users = []
if users == []:
    print('We need to find some users!')
