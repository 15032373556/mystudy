guest = ['boyfriend','friends','parents','sisters']
print('\t' + guest[0].title() + ",I'd like to invite you to my party.")
print('\t' + guest[1].title() + ",I'd like to invite you to my party.")
print('\t' + guest[2].title() + ",I'd like to invite you to my party.")
print('\t' + guest[3].title() + ",I'd like to invite you to my party.")

print('\n修改嘉宾')
#修改
print(guest[1].title() + " can't come.")
guest[1] = '柴雅楠'
for person in guest:
    print('\t' + person.title() + ",I'd like to invite you to my party.")

