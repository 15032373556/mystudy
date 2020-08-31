rivers = {
    'nile':'egypt',
    'yangtze':'China',
    'dead sea':'Spain',
}
for river,country in rivers.items():
    print('The ' + river.title() + ' runs through ' + country.title() + '.')

#将字典中每条河流的名字打印出来
print('\nThe rivers are following:')
for river in rivers.keys():
    print(river.title())

#将字典中每个国家的名字打印出来
print('\nThe countries are following:')
for country in rivers.values():
    print(country.title())