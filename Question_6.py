import itertools as it
import math
import matplotlib.pyplot as plt


a = range(0, 100)
b = range(0, 100)

x = []
y = []
for i, j in it.product(a, b):
    if (math.sqrt((i**2 + j**2) / ((i*j) + 1))).is_integer():
        print(i, j)
        x.append(i)
        y.append(j)

plt.scatter(x, y, alpha=0.5)
plt.title('Question 6 Problem')
plt.show()