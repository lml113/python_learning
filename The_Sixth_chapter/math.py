#输入数字数据处理函数：将输入的数据存在列表中。
def getnumbers():
    try:
        num = []
        num = input('请输入一组数据（以空格分隔）：').split(' ')
        for i in range(len(num)):
            num[i] = int(num[i])
    except:
        num = []
    finally:
        return num
#计算平均值
def mean(ls):
    s = 0.0
    for item in ls:
        s+=item
    return s/len(ls)
#计算方差
def dev(ls):
    m = mean(ls)
    s = 0.0
    for item in ls:
        s += (item-m)**2
    return pow(s/len(ls),0.5)
#计算中位数
def media(ls):
    sorted(ls)
    size = len(ls)
    if size%2==0:
        med = (ls[size//2-1]+ls[size//2])/2
    else :
        med = ls[size//2]
    return med
#主函数
def main():
    num = getnumbers()
    if num == []:
        print('没有正确输入数据！')
    else:
        print('平均值：{0:0.2f};方差：{1:0.2f};中位数：{2:0.2f}。'.format(mean(num),dev(num),media(num)))


if __name__ == '__main__':
    main()