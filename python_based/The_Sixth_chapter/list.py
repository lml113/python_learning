lt = list()
lt += 'pptho'
lt[1] = 'y'
lt.insert(1,'y')
del lt[0]
del lt[0:3]
if 0 in lt:
    print('True')
else:
    print('False')
lt.append('0')
x = lt.index('0')
print('数字0所在lt中的索引为：{}'.format(x))
print('lt的长度：{}'.format(len(lt)))
print('lt中最大元素为：{}'.format(max(lt)))
lt.clear()
print('清空：{}'.format(lt))