"""一组用于表示电动汽车的类"""

from car import Car

class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""

    def __init__(self,battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kwh battery.")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range =270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        """检查电瓶容量，如果不是85，就设置为85"""
        if self.battery_size != 85:
            self.battery_size = 85


class ElectricCar(Car):
    """Represent aspects of a car,specific to electric vehicles"""

    def __init__(self,make,model,year):
        """
        电动汽车的独特之处
        初始化父类的属性,再初始化电动汽车特有的属性
        """
        super().__init__(make,model,year)
        self.battery = Battery()
        #self.battery_size = 70

    # def describe_battery(self):
    #     print("This car has a " + str(self.battery_size) + "-kwh battery.")

my_tesla = ElectricCar('tesla','model s','2016')
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()







# my_tesla = ElectricCar('tesla','model s','2016')
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()