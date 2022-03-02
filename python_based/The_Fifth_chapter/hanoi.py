# 汉诺塔
count = 0

def hanoi(n,start,end,mid):
    global count
    if n==1:
        print('{}:{}-->{}'.format(n,start,end))
        count += 1
    else :
        hanoi(n-1,start,mid,end)
        print('{}:{}-->{}'.format(n,start,end))
        count += 1
        hanoi(n-1,mid,end,start)

hanoi(10,'A','C','B')
print(count)
