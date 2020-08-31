friend_1 = {
    'first_nme':'david',
    'last_name':'mcurie',
    'age':'31',
    'location':'shanghai',
}
friend_2 = {
    'first_nme':'hendrix',
    'last_name':'jimi',
    'age':'22',
    'location':'beijing',
}
friend_3 = {
    'first_nme':'marie',
    'last_name':'curie',
    'age':'19',
    'location':'hebei',
}
friends = [friend_1,friend_2,friend_3]
for friend in friends:
    print('\n')
    for key,value in friend.items():
        print(key.title() + ': ' + value.title())