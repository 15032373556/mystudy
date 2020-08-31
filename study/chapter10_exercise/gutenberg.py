filename = '3152.txt'

with open(filename, encoding = 'ISO-8859-1') as gt:
    contents = gt.read()
    number = contents.lower().count('the')
    print(number)