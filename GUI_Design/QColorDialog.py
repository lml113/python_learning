'''
颜色对话框:QColorDialog
'''
import sys
from turtle import color
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class QColorDialogDemo(QWidget):
    def __init__(self):
        super(QColorDialogDemo, self).__init__()
        self.InitUI()
    def InitUI(self):
        self.setWindowTitle("Color Dialog")
        self.setWindowIcon(QIcon('./Images/1.ico'))

        layout = QVBoxLayout()
        self.colorButton = QPushButton('选择颜色')
        self.colorButton.clicked.connect(self.getColor)
        self.colorLabel = QLabel('Hello,测试颜色例子')
        layout.addWidget(self.colorButton)
        layout.addWidget(self.colorLabel)

        self.setLayout(layout)
    def getColor(self):
        color = QColorDialog.getColor()
        p = QPalette()
        p.setColor(QPalette.WindowText,color)
        self.colorLabel.setPalette(p)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    widget = QColorDialogDemo()
    widget.show()

    sys.exit(app.exec_())
