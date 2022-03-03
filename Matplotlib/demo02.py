'''

设置坐标轴

'''
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-2*np.pi, 2*np.pi,1000)
y1 = np.cos(x)
y2 = x**2-1
plt.figure()
plt.plot(x, y1)
plt.plot(x,y2,color='red',linewidth = 2,linestyle = '-')#改变线条的颜色，粗细和样式
plt.xlim(-2*np.pi, 2*np.pi)#设置图片x轴边界
# plt.xlabel("I am x")
plt.ylim(-1,1)#设置图片y轴边界
# plt.ylabel('I am y')

new_ticks = np.linspace(-2*np.pi,2*np.pi,9)
print(new_ticks)
plt.xticks(new_ticks,['-2π', '-1.5π', '-π', '-0.5π', '0','0.5π','π','1.5π','2π'])#设置x轴记号，设置记号的标签
#设置y轴记号
#设置记号的标签
plt.yticks([-1,-0.5,0,0.5,1],[r'$really\ bad$', r'$bad\ \alpha$', r'$normal$', r'$good$', r'$very\ good$'])

#移动脊柱,axis:轴
# gca = 'get current axis'
ax = plt.gca()
ax.spines['right'].set_color('none')#右端脊梁设置为无色
ax.spines['top'].set_color('none')#上端脊梁设置为无色
ax.spines['left'].set_position(('data',0))#设置y轴的位置
ax.spines['bottom'].set_position(('data',0))#设置x轴的位置
ax.xaxis.set_ticks_position('bottom')#下面的脊梁代替x轴
ax.yaxis.set_ticks_position('left')#左面的脊梁代替y轴
# ax.spines['left'].set_position(('data',0))#设置y轴的位置
# ax.spines['bottom'].set_position(('data',0))
""" ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0)) """

##设置标题
plt.title('test01')
plt.show()