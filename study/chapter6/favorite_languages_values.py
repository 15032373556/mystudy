favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
#遍历字典中的所有值
print('The following languages have been mentioned:')
for language in favorite_languages.values():
    print(language.title())

print('\n')

#去除重复元素调用set()
print('The following languages have been mentioned:')
for language in set(favorite_languages.values()):
    print(language.title())