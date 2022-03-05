'''
柱状图
'''
import numpy as np
import matplotlib.pyplot as plt

n = 12
x = np.arange(n)
y1 = (1-x/float(n))*np.random.uniform(0.5,1,n)
y2 = (1-x/float(n))*np.random.uniform(0.5,1,n)

# facecolor:柱状条的颜色，edgecolor：柱状条的边框颜色
plt.bar(x,+y1,facecolor = '#9999ff',edgecolor = 'white')
plt.bar(x,-y2,facecolor = '#ff9999',edgecolor = 'white')

# 加标注
for x0,y01,y02 in zip(x,y1,y2):
    plt.text(x0-0.45,y01+0.05,'{:.2f}'.format(y01),fontdict={'size':10,'color':'black'})
    plt.text(x0-0.45,-y02-0.11,'{:.2f}'.format(y02),fontdict={'size':10,'color':'black'})

plt.xticks(x,x+1)

plt.show()
