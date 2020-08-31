import json

filename = 'favorite_number.json'
favorite_number = input("Please input your favorite number: ")
with open(filename,'w') as fn:
    json.dump(favorite_number,fn)
