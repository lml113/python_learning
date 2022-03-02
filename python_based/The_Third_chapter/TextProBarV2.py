#TextProBarV2.py
import time

scale = 100
print('执行开始'.center(scale//2,'-'))
start = time.perf_counter()
for i in range(scale+1):
    a = '*'*i
    b = '-'*(scale-i)
    c = i/scale*100
    t = time.perf_counter()-start
    print('\r{:^3.0f}%[{}->{}]{:.4f}s'.format(c,a,b,t),end='')
    time.sleep(0.1)
print('\n'+'执行结束'.center(scale//2,'-'))