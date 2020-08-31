users = {
    'asinstein':{
     'first':'albert',
     'last':'asinstein',
     'location':'princeton',
 },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
    },
}

for username,user_info in users.items():
    print('\nUsername: ' + username.title())
    full_name = user_info['first'] + ' '+ user_info['last']
    location = user_info['location']

    print('\tFullname: ' + full_name.title())
    print('\tlocation: ' + location.title())