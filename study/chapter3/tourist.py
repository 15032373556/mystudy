tourist_place = ['Zhang Jia Jie','Eye of Tianjin','The Imperial Palace','Yuan Ming Yuan','Old dragon head']
print('\n原始顺序打印')
print(tourist_place)

print('\n使用sorted()按字母顺序打印')
print(sorted(tourist_place))
#核实排列顺序未变
print(tourist_place)

print('\n使用sorted()按字母顺序相反的顺序打印')
print(sorted(tourist_place,reverse = True))
#核实排列顺序未变
print(tourist_place)

print('\n使用reverse()修改排列顺序')
tourist_place.reverse()
#核实排列顺序变了
print(tourist_place)

print('\n使用reverse()再次修改排列顺序')
tourist_place.reverse()
#核实排列顺序恢复到原来
print(tourist_place)

print('\n使用sort()按字母顺序打印')
tourist_place.sort()
#核实排列顺序变了
print(tourist_place)

print('\n使用sort()按字母顺序相反的顺序打印')
tourist_place.sort(reverse = True)
#核实排列顺序变了
print(tourist_place)
