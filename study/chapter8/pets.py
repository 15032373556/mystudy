def describe_pet(animal_type,pet_name):
    """显示宠物的信息"""
    print('\nI have a ' + animal_type + '.')
    print('My ' + animal_type + "'s name is " + pet_name.title() + '.')

#调用函数多次
describe_pet('hamster','harry')
describe_pet('dog','willie')
#位置实参的顺序性很重要
describe_pet('harry','hamster')

#关键字实参
describe_pet(animal_type='hamster',pet_name='harry')
describe_pet(pet_name='harry',animal_type='hamster')