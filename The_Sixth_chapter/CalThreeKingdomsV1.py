#CalThreeKingdomsV1
import jieba
import time

start = time.perf_counter()
counts = dict()
with open("F:\\vscode\\python\\course\\The_Sixth_chapter\\text.txt", 'r', encoding="utf-8") as f:
    words = jieba.lcut(f.read())
    for word in words:
        if len(word) == 1:
            continue
        else:
            counts[word] = counts.get(word,0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True) 
for i in range(15):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))
print('花费的时间为：{:.4f}s'.format(time.perf_counter()-start))