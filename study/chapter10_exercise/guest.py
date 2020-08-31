# filename = 'guest.txt'
#
# user_name = input('Please enter your name: ')
# if True:
#     with open(filename, 'w') as gu:
#         gu.write(user_name)

filename = 'guest_book.txt'
print("Enter q at any time to quit.")
while True:
    user_name = input('Please enter your name: ')
    if user_name != 'q':
        print('Hello,' + user_name + '!')
        with open(filename,'a') as gb:
            gb.write(user_name + ' visited\n')
    else:
        break



