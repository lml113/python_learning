'''
subplot分格显示
'''
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# method 1: gridspec
########################
plt.figure()
ax1 = plt.subplot2grid((3,3),(0,0),colspan=3,rowspan=1)
plt.plot([1,2],[1,2])
ax2 = plt.subplot2grid((3,3),(1,0),colspan=1,rowspan=1)
plt.plot([1,2],[1,2])
ax3 = plt.subplot2grid((3,3),(1,1),colspan=1,rowspan=1)
plt.plot([1,2],[1,2])
ax4 = plt.subplot2grid((3,3),(1,2),colspan=1,rowspan=2)
plt.plot([1,2],[1,2])
ax5 = plt.subplot2grid((3,3),(2,0),colspan=2,rowspan=1)
plt.plot([1,2],[1,2])

# method 2: gridspec
########################
plt.figure()
G = gridspec.GridSpec(3, 3)

axes_1 = plt.subplot(G[0, :])
plt.xticks([]), plt.yticks([])
plt.text(0.5,0.5, 'Axes 1',ha='center',va='center',size=24,alpha=.5)

axes_2 = plt.subplot(G[1,:-1])
plt.xticks([]), plt.yticks([])
plt.text(0.5,0.5, 'Axes 2',ha='center',va='center',size=24,alpha=.5)

axes_3 = plt.subplot(G[1:, -1])
plt.xticks([]), plt.yticks([])
plt.text(0.5,0.5, 'Axes 3',ha='center',va='center',size=24,alpha=.5)

axes_4 = plt.subplot(G[-1,0])
plt.xticks([]), plt.yticks([])
plt.text(0.5,0.5, 'Axes 4',ha='center',va='center',size=24,alpha=.5)

axes_5 = plt.subplot(G[-1,-2])
plt.xticks([]), plt.yticks([])
plt.text(0.5,0.5, 'Axes 5',ha='center',va='center',size=24,alpha=.5)


# method 3: easy to define structure
####################################

plt.show()

