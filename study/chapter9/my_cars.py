##从一个模块中导入多个类
# from electric_car import Car,ElectricCar
#
# my_bettle = Car('volkswagen','beetle',2016)
# print(my_bettle.get_descriptive_name())
#
# my_tesla = ElectricCar('tesla','roadster',2016)
# print(my_tesla.get_descriptive_name())


#导入整个模块
import electric_car

my_bettle = electric_car.Car('volkswagen','beetle',2016)
print(my_bettle.get_descriptive_name())

my_tesla = electric_car.ElectricCar('tesla','roadster',2016)
print(my_tesla.get_descriptive_name())