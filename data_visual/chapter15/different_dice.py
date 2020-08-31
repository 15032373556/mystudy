import pygal

from die import Die
from sum_2num import sum as s

#创建一个D6和一个D10
die_1 = Die()
die_2 = Die(10)

#掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#分析结果
frequencies = []
max_result = die_1.num_sides+1 + die_2.num_sides+1
for value in range(2,max_result):
    frequency = results.count(value)
    frequencies.append(frequency)

#对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling a D6 and a D10 dice 50000 times."
# hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12']
hist.x_labels = s(6,10)
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6 + D10',frequencies)
hist.render_to_file('different_dice_visual.svg')