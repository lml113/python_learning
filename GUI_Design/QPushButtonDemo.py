'''
按钮控件(QPshButton)

QAbstractButton

QPushButton
AToolButton
QRadioButton
QCheckBox

'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class QPushButtonDemo(QWidget):
    def __init__(self):
        super(QPushButtonDemo, self).__init__()
        self.InitUI()

    def InitUI(self):
        self.setWindowTitle('按钮控件(QPshButton)')
        self.setWindowIcon(QIcon('./Images/4.ico'))
        self.resize(400,300)

        self.button1 = QPushButton('第1个按钮')
        self.button1.toggle()# 设置按钮可以按下去
        self.button1.setCheckable(True)

        self.button1.clicked.connect(lambda:self.buttonStatus(self.button1))
        self.button1.clicked.connect(self.button1Print)

        self.button2 = QPushButton('图像按钮')
        self.button2.setIcon(QIcon(QPixmap('./Images/1.ico')))

        self.button2.clicked.connect(lambda:self.buttonStatus(self.button2))
        self.button2.clicked.connect(self.button2Print)

        self.button3 = QPushButton('不可用的按钮')
        self.button3.setEnabled(False)

        self.button4 = QPushButton('&M')
        self.button4.setDefault(True)
        self.button4.clicked.connect(lambda:self.buttonStatus(self.button4))

        layout = QVBoxLayout()
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)

        self.setLayout(layout)

    def buttonStatus(self,btn):
        print('被单击的按钮是<{}>'.format(btn.text()))

    def button1Print(self,btn):
        print('按键{}...'.format('已按下' if btn else '未按下'))

    def button2Print(self):
        print('图像按钮按下...')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    widget = QPushButtonDemo()
    widget.show()

    sys.exit(app.exec_())

