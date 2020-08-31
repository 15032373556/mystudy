import json

filename = 'favorite_number.json'
with open(filename) as fn:
    number = json.load(fn)
    print("I know your favorite number!It's " + number +  '.')