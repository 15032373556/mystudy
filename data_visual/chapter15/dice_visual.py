import pygal

from die import Die
from sum_num import sum_2,sum_3,multip

#创建两个D6骰子
die_1 = Die()
die_2 = Die()
# #创建两个D8骰子
# die_1 = Die(8)
# die_2 = Die(8)
# #创建三个D6骰子
# die_1 = Die()
# die_2 = Die()
# die_3 = Die()

#掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die_1.roll() * die_2.roll()
    #result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

#分析结果
frequencies = []
max_result = die_1.num_sides+1 * die_2.num_sides + 1
#max_result = die_1.num_sides+1 + die_2.num_sides + die_3.num_sides + 1
#for value in range(2,max_result):
for value in range(1, max_result):
    frequency = results.count(value)
    frequencies.append(frequency)

#对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling two D6 dice 1000 times."
# hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12']
#hist.x_labels = sum(6,6)
#hist.x_labels = sum_2(8,8)
#hist.x_labels = sum_3(6,6,6)
hist.x_labels = multip(6,6)
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
# hist.add('D6 + D6',frequencies)
# hist.render_to_file('dice_visual.svg')
# hist.add('D8 + D8',frequencies)
# hist.render_to_file('dice_visual_8.svg')
# hist.add('D6 + D6 + D6',frequencies)
# hist.render_to_file('dice_visual_6.svg')
hist.add('D6 * D6',frequencies)
hist.render_to_file('dice_visual_66.svg')