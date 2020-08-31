#导入整个模块
#import pizza_1
# pizza_1.make_pizza(12,'mushrooms')
# pizza_1.make_pizza(16,'mushrooms','green peppers','extra cheese')

# #导入特定的函数，用逗号分隔函数名
# from pizza_1 import make_pizza
# make_pizza(12,'mushrooms')
# make_pizza(16,'mushrooms','green peppers','extra cheese')

#使用as给函数指定别名
# from pizza_1 import make_pizza as mp
# mp(12,'mushrooms')
# mp(16,'mushrooms','green peppers','extra cheese')

# #使用as给模块指定别名
# import pizza_1  as p
# p.make_pizza(12,'mushrooms')
# p.make_pizza(16,'mushrooms','green peppers','extra cheese')

#导入模块中的所有函数
# from study.chapter8.pizza_1 import *
from study.chapter8.pizza_1 import make_pizza, make_pizza1

make_pizza(12,'mushrooms')
make_pizza1(16,'mushrooms','green peppers','extra cheese')

