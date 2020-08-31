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

print('\n添加嘉宾')
#添加嘉宾insert()
print('I have found a bigger table.')
guest.insert(0,'徐晗')
guest.insert(2,'刘明欣')
guest.append('张誉')
for person in guest:
    print('\t' + person.title() + ",I'd like to invite you to my party.")

print('\n缩减嘉宾')
#缩减嘉宾pop()
print('Only two people can be invited.')
popped_person = guest.pop()
print(popped_person + ",I'm sorry I can't invite you to dinner.")
popped_person = guest.pop()
print(popped_person + ",I'm sorry I can't invite you to dinner.")
popped_person = guest.pop()
print(popped_person + ",I'm sorry I can't invite you to dinner.")
popped_person = guest.pop()
print(popped_person + ",I'm sorry I can't invite you to dinner.")
popped_person = guest.pop()
print(popped_person + ",I'm sorry I can't invite you to dinner.")

print(guest[0] + "You're still on the list.")
print(guest[1] + "You're still on the list.")

print('\n删除嘉宾')
#删除嘉宾del
del guest[0]
del guest[0]
print(guest)