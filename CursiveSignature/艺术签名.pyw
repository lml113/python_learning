import sys
import re
import os
import requests
from Ui_Widget import Ui_Form
import FCid
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication,QMainWindow,QFileDialog

class CursiveSignature(QMainWindow,Ui_Form):
    def __init__(self):
        super(CursiveSignature,self).__init__()
        self.setupUi(self)
        self.initUI()
    def initUI(self):
        self.setWindowTitle('艺术签名')
        self.setWindowIcon(QIcon(r'F:\vscode\python\python_learning\CursiveSignature\images\1.ico'))

        self.res = None
        self.lineEdit.setPlaceholderText('2-20个汉字')
        self.pushButton_save.clicked.connect(self.save)
        self.pushButton_generate.clicked.connect(self.generate)
        pass
    def save(self):
        # QFileDialog.getSaveFileName(str = 'CursiveSignature/tmp.jpg')
        if self.res is not None:
            filename = QFileDialog.getSaveFileName(self, '保存', './CursiveSignature/tmp.%s' % self.show_image_ext, '文件类型(*.jpg)')
            if filename[0] != '':
                with open(filename[0], 'wb') as f:
                    f.write(self.res)

    def generate(self):
        url = 'http://www.jiqie.com/a/re14.php'
        headers = {
                    'Referer': 'http://www.jiqie.com/a/14.htm',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
                    'Host': 'www.jiqie.com',
                    'Origin': 'http://www.jiqie.com'
                    }
        fontdata = FCid.font2ids_dict[self.comboBox_2.currentText()]
        colordata = FCid.color2ids_dict[self.comboBox_3.currentText()]
        data = {
                'id': self.lineEdit.text(),
                'zhenbi': '20191123',
                'id1': fontdata[0],# 默认一笔艺术签
                'id2': fontdata[1],
                'id3': colordata[0],# 默认黑色字体
                'id5': colordata[1]
                }
        if len(data['id'])>=2:
            res = requests.post(url, headers=headers, data=data)
            image_url = re.findall(r'src="(.*?)"', res.text)[0]
            self.show_image_ext = image_url.split('.')[-1].split('?')[0]
            self.res = requests.get(image_url).content
            fp = open('./tmp.%s' % self.show_image_ext, 'wb')
            fp.write(self.res)
            fp.close()
            self.textBrowser.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html>\n"
            "<img src=\"./tmp.jpg\" width =\"770\" height =\"390\"\n"
            "</html>")
            os.remove('./tmp.%s' % self.show_image_ext)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwin = CursiveSignature()
    mainwin.show()
    sys.exit(app.exec_())
