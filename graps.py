from matplotlib import pyplot as plt
x1 = [5,8,10]
y1 = [12,6,6]
x2 = [6,9,11]
y2 = [6,15,17]
plt.bar(x1,y1, align='center',color='r')
plt.bar(x2,y2, align='center',color='y')
plt.xlabel('x -axis')
plt.ylabel('y-axis')
plt.show()

