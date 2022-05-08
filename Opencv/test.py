import numpy as np

g = np.array([[1,1,2,1,1],
             [1,3,4,3,1],
             [2,4,8,4,2],
             [1,3,4,3,1],
             [1,1,2,1,1]]
             )
g_sum = sum(sum(g))

g = g/g_sum
print(g)

a = []
print(a+[1]+[2])