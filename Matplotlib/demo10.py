'''
饼状图pie
'''
import numpy as np
import matplotlib.pyplot as plt

n = 20
x = np.random.uniform(0,1,n)
y = np.arange(n)

plt.subplot(1,2,1)
plt.pie(x)

plt.subplot(1,2,2)
plt.pie(y)

plt.show()