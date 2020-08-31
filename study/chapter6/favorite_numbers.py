favorite_numbers = {
    '老大':'5,8',
    '二姐':'3,6,9',
    '老三':'8',
    '四妹':'6,2',
    '老五':'9,0,1',
}
for friend_name,numbers in favorite_numbers.items():
    print(friend_name.title() + "最喜欢的数字是 " + numbers)