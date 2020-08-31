favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
#遍历字典中的所有键
for name in favorite_languages.keys():
    print(name.title())

#指定朋友名字
friends = ['phil','sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(' Hi ' + name.title() +
              ', I see your favorite language is ' +
              favorite_languages[name].title() + '!')

#确定 Erin 是否接受了调查
if 'erin' not in favorite_languages.keys():
    print('\nErin,please take our poll!')
