from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

#遍历字典中的所有键-值对
for name,language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + '.\n')