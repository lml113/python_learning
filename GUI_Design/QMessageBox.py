'''
消息对话框:QMessageBox
1、关于对话框
2、错误对话框
3、警告对话框
4、提问对话框
5、消息对话框

有两点差异
1、显示的对话框图标可能不同
2、显示的按钮是不一样的
'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# 对话框
class dialogDemo(QDialog):
    def __init__(self):
        super(dialogDemo, self).__init__()
        self.InitUI()
    def InitUI(self):
        self.setWindowTitle("对话框")
        self.resize(200,100)
        pass
# 主窗口
class QMessageBox(QWidget):
    def __init__(self):
        super(QMessageBox, self).__init__()
        self.InitUI()

    def InitUI(self):
        self.setWindowTitle('QMessageBox')
        self.resize(300,400)

        layout = QVBoxLayout()
        self.button1 = QPushButton(self)
        self.button1.setText('关于')
        self.button1.setToolTip('显示关于对话框')
        self.button1.clicked.connect(self.showDialog)
        layout.addWidget(self.button1)

        self.button2 = QPushButton(self)
        self.button2.setText('消息')
        self.button2.setToolTip('显示消息对话框')
        self.button2.clicked.connect(self.showDialog)
        layout.addWidget(self.button2)

        self.button3 = QPushButton(self)
        self.button3.setText('警告')
        self.button3.setToolTip('显示警告对话框')
        self.button3.clicked.connect(self.showDialog)
        layout.addWidget(self.button3)

        self.button4 = QPushButton(self)
        self.button4.setText('错误')
        self.button4.setToolTip('显示错误对话框')
        self.button4.clicked.connect(self.showDialog)
        layout.addWidget(self.button4)

        self.button5 = QPushButton(self)
        self.button5.setText('错误')
        self.button5.setToolTip('显示错误对话框')
        self.button5.clicked.connect(self.showDialog)
        layout.addWidget(self.button5)

        self.setLayout(layout)
    
    def showDialog(self):
        btn = self.sender()
        if btn == self.button1:
            dialog = dialogDemo()
        elif btn == self.button2:
            dialog = dialogDemo()
        elif btn == self.button3:
            dialog = dialogDemo()
        else:
            dialog = dialogDemo()
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    MainWin = QMessageBox()
    MainWin.show()

    sys.exit(app.exec_())
