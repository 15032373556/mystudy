favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}

print("Sarah's favorite language is " +
      favorite_languages['sarah'].title() +
      "."
      )
#遍历字典中的所有键-值对
for name,language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + '.\n')

