import sys
import re
import os
from PIL import Image
import requests
from Ui_Widget import Ui_Form
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication,QMainWindow,QFileDialog

class CursiveSignature(QMainWindow,Ui_Form):
    def __init__(self):
        super(CursiveSignature,self).__init__()
        self.setupUi(self)
        self.initUI()
    def initUI(self):
        self.setWindowTitle('艺术签名')
        self.setWindowIcon(QIcon('./GUI_Design/Images/1.ico'))

        self.show_image = None
        self.pushButton_save.clicked.connect(self.save)
        self.pushButton_generate.clicked.connect(self.generate)
        pass
    def save(self):
        # QFileDialog.getSaveFileName(str = 'CursiveSignature/tmp.jpg')
        if self.show_image is not None:
            filename = QFileDialog.getSaveFileName(self, '保存', './CursiveSignature/tmp.%s' % self.show_image_ext, '文件类型(*.jpg)')
            self.show_image.save(filename[0])

    def generate(self):
        font2ids_dict = {
                            '一笔艺术签': ['901', '15'],
                            '连笔商务签': ['904', '15'],
                            '一笔商务签': ['905', '14'],
                            '真人手写': ['343', '14'],
                            '卡通趣圆字': ['397', '14'],
                            '暴躁字': ['380', '14']
                    }
        color2ids_dict = {
                            'Black': ['#000000', '#FFFFFF'],
                            'Blue': ['#0000FF', '#FFFFFF'],
                            'Red': ['#FF0000', '#FFFFFF'],
                            'Green': ['#00FF00', '#FFFFFF'],
                            'Yellow': ['#FFFF00', '#FFFFFF'],
                            'Pink': ['#FFC0CB', '#FFFFFF'],
                            'DeepSkyBlue': ['#00BFFF', '#FFFFFF'],
                            'Cyan': ['#00FFFF', '#FFFFFF'],
                            'Orange': ['#FFA500', '#FFFFFF'],
                            'Seashell': ['#FFF5EE', '#FFFFFF']
                        }
        url = 'http://www.jiqie.com/a/re14.php'
        headers = {
                    'Referer': 'http://www.jiqie.com/a/14.htm',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
                    'Host': 'www.jiqie.com',
                    'Origin': 'http://www.jiqie.com'
                    }
        fontdata = font2ids_dict[self.comboBox_2.currentText()]
        colordata = color2ids_dict[self.comboBox_3.currentText()]
        data = {
                'id': self.lineEdit.text(),
                'zhenbi': '20191123',
                'id1': fontdata[0],# 默认一笔艺术签
                'id2': fontdata[1],
                'id3': colordata[0],# 默认黑色字体
                'id5': colordata[1]
                }
        res = requests.post(url, headers=headers, data=data)
        image_url = re.findall(r'src="(.*?)"', res.text)[0]
        self.show_image_ext = image_url.split('.')[-1].split('?')[0]
        res = requests.get(image_url)
        fp = open('CursiveSignature/tmp.%s' % self.show_image_ext, 'wb')
        fp.write(res.content)
        fp.close()
        self.show_image = Image.open('CursiveSignature/tmp.%s' % self.show_image_ext).convert('RGB')
        self.textBrowser.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html>\n"
        "<img src=\"CursiveSignature/tmp.jpg\" width =\"770\" height =\"390\"\n"
        "</html>")
        os.remove('CursiveSignature/tmp.%s' % self.show_image_ext)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwin = CursiveSignature()
    mainwin.show()
    sys.exit(app.exec_())
