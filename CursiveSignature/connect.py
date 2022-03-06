'''
获取网页信息
'''
import requests
import re
import matplotlib.pyplot as plt

url = 'http://www.jiqie.com/a/re14.php'
headers = {
            'Referer': 'http://www.jiqie.com/a/14.htm',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
            'Host': 'www.jiqie.com',
            'Origin': 'http://www.jiqie.com'
            }

data = {
        'id': '廖蒙林',
        'zhenbi': '20191123',
        'id1': '901',# 默认一笔艺术签
        'id2': '15',
        'id3': '#000000',# 默认黑色字体
        'id5': '#FFFFFF'
        }

res = requests.post(url, headers=headers, data=data)
image_url = re.findall(r'src="(.*?)"', res.text)[0]
print(image_url)
show_image_ext = image_url.split('.')[-1].split('?')[0]
print(show_image_ext)
res = requests.get(image_url)
# print(res.content)
# for i in res:
#     print(i)
# plt.imshow(res)
# plt.show()
fp = open('CursiveSignature/tmp.{}'.format(show_image_ext), 'wb')
fp.write(res.content)
fp.close()

f = plt.imread('CursiveSignature/tmp.{}'.format(show_image_ext))
plt.imshow(f)
plt.show()
# show_image = Image.open('tmp.%s' % self.show_image_ext).convert('RGB')
# self.updateimage()
# os.remove('tmp.%s' % self.show_image_ext)