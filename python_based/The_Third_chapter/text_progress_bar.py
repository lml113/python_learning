#text_progress_bar
import time

scale = 100
print('------执行开始------')
for i in range(scale+1):
    c = (i/scale)*100
    print('\r{:>10.0f}%'.format(c),end='')
    time.sleep(0.1)
print('\n------执行结束------')