#默认值
def describe_pet(pet_name,animal_type='dog'):
    """显示宠物的信息"""
    print('\nI have a ' + animal_type + '.')
    print('My ' + animal_type + "'s name is " + pet_name.title() + '.')

describe_pet('harry')
describe_pet(pet_name='willie')
describe_pet('willie','hamster')
describe_pet(pet_name='willie',animal_type='hamster')
describe_pet(animal_type='hamster',pet_name='willie')

#避免实参错误
# describe_pet()