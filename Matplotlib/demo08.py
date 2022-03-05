'''
等高线图
'''
from tkinter import Y
import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

n = 256
x = np.linspace(-3,3,n)
y = np.linspace(-3,3,n)
X,Y = np.meshgrid(x,y)

h = f(X,Y)

# 画等高图use.plt.contourf to filling contours
plt.contourf(X,Y,h,8,alpha=0.7,cmap='jet')
# 画等高线use plt.contour to add contour lines
C = plt.contour(X,Y,h,8,linewidths=1)
# adding labels for
plt.clabel(C,inline = True,fontsize=12)

plt.xticks([])
plt.yticks([])

plt.show()
