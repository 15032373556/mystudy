import json

filename = 'favorite_number.json'
try:
    with open(filename) as fn:
        number = json.load(fn)
except FileNotFoundError:
    favorite_number = input("Please input your favorite number: ")
    with open(filename, 'w') as fn:
        json.dump(favorite_number, fn)
else:
    print("I know your favorite number!It's " + number + '.')

