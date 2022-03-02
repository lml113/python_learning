
import time

def gettxt():
    with open('F:\\vscode\\python\\course\\The_Sixth_chapter\\Hamlet.txt', 'r') as f:
        t = f.read()
        t = t.lower()
    for item in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        t = t.replace(item, ' ')
    t = t.replace('\n'," ")
    return t

def main():
    start = time.perf_counter()
    txt = gettxt()
    words = txt.split(' ')
    count = {}
    for item in words:
        if len(item) ==0:
            continue
        else:
            count[item] = count.get(item,0)+1
    count_list = list(count.items())
    count_list.sort(key=lambda x:x[1],reverse=True)
    for i in range(20):
        word,counter = count_list[i]
        print('{0:<2}\t{1:<10}\t{2:>5}'.format(i+1,word,counter))
    print('花费的时间为：{:.4f}'.format(time.perf_counter()-start))


if __name__ == '__main__':
    main()
