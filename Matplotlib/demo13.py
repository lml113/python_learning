'''
图中图
'''
import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7]
y = [1,3,4,2,5,8,6]

fig = plt.figure()
left,bottom,width,height = 0.1,0.1,0.8,0.8
ax1 = fig.add_axes([left,bottom,width,height])
ax1.plot(x,y,'r')
ax1.set_title('title')
ax1.set_xlabel('x')
ax1.set_ylabel('y')

left,bottom,width,height = 0.2,0.6,0.25,0.25
ax2 = fig.add_axes([left,bottom,width,height])
ax2.plot(x,y,'b')
ax2.set_title('title')
ax2.set_xlabel('x')
ax2.set_ylabel('y')

left,bottom,width,height = 0.6,0.2,0.25,0.25
# ax3 = fig.add_axes([left,bottom,width,height])
# ax3.plot(x,y,'black')
# ax3.set_title('title')
# ax3.set_xlabel('x')
# ax3.set_ylabel('y')

# 另一种方法
plt.axes([left,bottom,width,height])
plt.plot(x,y)
plt.title('title')
plt.xlabel('x')
plt.ylabel('y')

plt.show()
