class Restaurant():
    """一次模拟饭店的简单尝试"""

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        #self.number_served = number_served

    def describe_restaurant(self):
        print("\nThe restaurant's name is " + self.restaurant_name + '.')
        print("The cuisine's type is " + self.cuisine_type + '.')
        #print(str(self.number_served) + ' people have had dinner in this restaurant.')

    def open_restaurant(self):
        print("The restaurant is open.")

    def set_number_served(self,number_served):
        self.number_served = number_served
        print(str(self.number_served) + ' people have had dinner in this restaurant.')

    def increment_number_served(self,increment_numder):
        self.number_served += increment_numder
        print(str(self.number_served) + ' people have had dinner in this restaurant.')


class IceCreamStand(Restaurant):
    """模拟冰激凌小店"""

    def __init__(self,restaurant_name,cuisine_type):
        """冰激凌店的独特之处"""
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = ['matcha','strawberry','mango']

    def describe_icecream(self):
        """显示冰激凌的所有口味"""
        print("The store has the following flavors of ice cream: ")
        for flavor in self.flavors:
            print("\t-" + flavor.title() + ' ice cream')

# icecream = IceCreamStand('CoCo','ice')
# icecream.describe_icecream()



# restaurant = Restaurant('KFC','Fried')
# restaurant.describe_restaurant()
# restaurant.set_number_served(100)
# restaurant.increment_number_served(20)


# restaurant_1 = Restaurant('KFC','Fried')
# restaurant_1.describe_restaurant()
#
# restaurant_2 = Restaurant('Baozipu','Steam')
# restaurant_2.describe_restaurant()
#
# restaurant_3 = Restaurant('Quanjude','Roast')
# restaurant_3.describe_restaurant()