favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
persons = ['jen','edward','jimi','david']

for name,language in favorite_languages.items():
    if name in persons:
        print('\n' + name.title() +  ',thank you for your participation.' + '.')
    else:
        print('\n' + name.title() + ',invite you to participate in the survey.')



