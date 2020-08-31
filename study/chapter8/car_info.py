# import make_car_function
# my_car = make_car_function.make_car('subaru','outback',color='blue',tow_package=True)
# print(my_car)

# from make_car_function import make_car
# my_car = make_car('subaru','outback',color='blue',tow_package=True)
# print(my_car)

# from make_car_function import make_car as mc
# my_car = mc('subaru','outback',color='blue',tow_package=True)
# print(my_car)

# import make_car_function as mcf
# my_car = mcf.make_car('subaru','outback',color='blue',tow_package=True)
# print(my_car)

from make_car_function import *
my_car = make_car('subaru','outback',color='blue',tow_package=True)
print(my_car)

# def make_car(manu,model,**car_info):
#     """将一辆汽车的信息存储在一个字典中"""
#     car_file = {}
#     car_file['manufacturer'] = manu
#     car_file['car_model'] = model
#     for key,value in car_info.items():
#         car_file[key] = value
#     return car_file

