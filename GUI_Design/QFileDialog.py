'''
文件对话框:QFileDialog
1、
'''
import sys
from turtle import color, mode
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class QFileDialogDemo(QWidget):
    def __init__(self):
        super(QFileDialogDemo, self).__init__()
        self.InitUI()
    def InitUI(self):
        self.setWindowTitle("File Dialog")
        self.setWindowIcon(QIcon('./Images/1.ico'))
        self.resize(800,600)

        self.text = list()
        self.textLine = 0
        self.readLines = 20

        layout = QGridLayout()
        self.Button = QPushButton('加载图片')
        self.Button.clicked.connect(self.getImage)

        self.imageLabel = QLabel('图片路径')
        self.imageLabel.setToolTip(self.imageLabel.text())
        self.imageLabel.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.gray)
        self.imageLabel.setPalette(palette)
        self.imageLabel.setAlignment(Qt.AlignCenter)

        self.imageLabe2 = QLabel('图片')
        self.imageLabe2.setAlignment(Qt.AlignCenter)
        # 加载文件
        self.Button1 = QPushButton('加载文件')
        self.Button1.clicked.connect(self.getFile)

        self.fileLabe1 = QLabel('文件路径')
        self.fileLabe1.setToolTip(self.fileLabe1.text())
        self.fileLabe1.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.gray)
        self.fileLabe1.setPalette(palette)
        self.fileLabe1.setAlignment(Qt.AlignCenter)

        self.button2 = QPushButton('下一页')
        self.button2.clicked.connect(self.textDown)
        self.button3 = QPushButton('上一页')
        self.button3.clicked.connect(self.textUp)

        self.fileLabe2 = QLabel(self)
        self.fileLabe2.setToolTip('文件浏览窗口')

        layout.addWidget(self.imageLabe2,0,0,1,4)
        layout.addWidget(self.imageLabel,1,0,1,3)
        layout.addWidget(self.Button,1,3)
        layout.addWidget(self.fileLabe2,2,0,1,4)
        layout.addWidget(self.button3,3,1)
        layout.addWidget(self.button2,3,2)
        layout.addWidget(self.fileLabe1,4,0,1,3)
        layout.addWidget(self.Button1,4,3)

        self.setLayout(layout)
    def getImage(self):
        imageFile,_ = QFileDialog.getOpenFileName(self,'打开文件','.','图像文件 (*.jpg *.png) ')
        self.imageLabel.setText(imageFile)
        self.imageLabel.setToolTip(self.imageLabel.text())
        self.imageLabe2.setPixmap(QPixmap(imageFile))
    def getFile(self):
        File,_ = QFileDialog.getOpenFileName(self,'打开文件','.','文件(*.txt *.py)')
        self.fileLabe1.setText(File)
        self.fileLabe1.setToolTip(self.fileLabe1.text())
        if File:
            with open(File,encoding = 'utf-8',mode = 'r') as f:
                self.text = f.readlines()
                self.textLine = 0
                self.fileLabe2.setText('')
    def textDown(self):
        length = len(self.text)
        if length>0 and self.textLine<length:
            self.fileLabe2.setText(''.join(self.text[self.textLine:self.textLine+min(self.readLines,length-self.textLine)]))
            self.textLine = self.textLine+min(self.readLines,length-self.textLine)
    def textUp(self):
        length = len(self.text)
        if length>0 and self.textLine>0:
            self.fileLabe2.setText(''.join(self.text[self.textLine-min(self.textLine,self.readLines):self.textLine]))
            self.textLine = self.textLine-min(self.textLine,self.readLines)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    widget = QFileDialogDemo()
    widget.show()

    sys.exit(app.exec_())
