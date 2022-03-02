'''
QLabel与伙伴控件
mainlayout.addWidget(控件对象,rowIndex,columnIndex,row,column)
'''
from os import name
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

class QLabelButton(QWidget):
    def __init__(self):
        super(QLabelButton, self).__init__()
        self.InitUI()

    def InitUI(self):
        #self.resize(400,300)
        self.setWindowIcon(QIcon("./Images/4.ico"))
        self.setWindowTitle("QLabel与伙伴控件")

        namelabel = QLabel('&Name',self)# 创建name标签
        nameLIneEdit = QLineEdit(self)# 创建
        # 设置伙伴控件
        namelabel.setBuddy(nameLIneEdit)

        passwordlabel = QLabel('&Password',self)# 创建password标签
        passwordLineEdit = QLineEdit(self)# 创建
        # 设置伙伴控件
        passwordlabel.setBuddy(passwordLineEdit)

        btnOK = QPushButton('&OK')
        btnCancel = QPushButton('&Cancel')

        mainlayout = QGridLayout()
        mainlayout.addWidget(namelabel,0,0)
        mainlayout.addWidget(nameLIneEdit,0,1,1,2)
        mainlayout.addWidget(passwordlabel,1,0)
        mainlayout.addWidget(passwordLineEdit,1,1,1,2)
        mainlayout.addWidget(btnOK,2,1)
        mainlayout.addWidget(btnCancel,2,2)

        self.setLayout(mainlayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainwin = QLabelButton()
    mainwin.show()

    sys.exit(app.exec_())
