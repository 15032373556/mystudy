from random import randint

class Die():
    """骰子"""

    def __init__(self):
        self.sides = 6

    def roll_die(self):
        return randint(1,self.sides)


die_1 = Die()
num_list = []
num = 1
while num <= 10:
    num_list.append(die_1.roll_die())
    num += 1
print(num_list)

die_2 = Die()
die_2.sides = 10
num_list = []
num = 1
while num <= 10:
    num_list.append(die_2.roll_die())
    num += 1
print(num_list)


die_3 = Die()
die_3.sides = 20
num_list = []
num = 1
while num <= 10:
    num_list.append(die_3.roll_die())
    num += 1
print(num_list)

