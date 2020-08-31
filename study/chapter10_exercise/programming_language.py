filename = 'reason_book.txt'
print("Enter q at any time to quit.")
while True:
    reason = input('Why do you like programming? ')
    if reason != 'q':
        print('Thanks for your participation!')
        with open(filename,'a') as rb:
            rb.write(reason +'\n')
    else:
        break


