# import matplotlib.pyplot as plt
#
# x_values = [1,2,3,4,5]
# y_values = [1,8,27,64,125]
# plt.scatter(x_values,y_values,s=100)
#
# plt.title("Cube Numbers",fontsize=40)
# plt.xlabel("Value",fontsize=10)
# plt.ylabel("Cube of Value",fontsize=10)
# plt.tick_params(axis='both',which='major',labelsize=10)
#
# plt.show()

import matplotlib.pyplot as plt

x_values = list(range(1,5001))
y_values = [x**3 for x in x_values]
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolors='none',s=20)

plt.title("Cube Numbers",fontsize=30)
plt.xlabel("Value",fontsize=10)
plt.ylabel("Cube of Value",fontsize=10)
plt.axis([0,5100,0,126000000000])
plt.tick_params(axis='both',which='major',labelsize=10)

plt.show()