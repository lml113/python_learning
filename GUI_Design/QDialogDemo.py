'''
对话框:QDialog
QMseeageBox
QColorDialog
QFontDialog
QInputDialog

QMainWindow
QWidget
QDialog
'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
# 设置对话框
class DialogSet(QDialog):
    def __init__(self):
        super(DialogSet, self).__init__()
        self.InitUI()
    def InitUI(self):
        self.setWindowTitle('设置')
        self.setWindowIcon(QIcon('./Images/4.ico'))

        layout = QHBoxLayout()
        self.button1 = QPushButton('确定')
        self.button1.clicked.connect(self.dialogClose)
        self.button2 = QPushButton('取消')
        self.button2.clicked.connect(self.dialogClose)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        self.setLayout(layout)

    def dialogClose(self):
        btn = self.sender()
        if btn == self.button1:
            print('确定更改,对话框退出')
        else:
            print('取消更改,对话框退出')
        self.close()
# 消息对话框
class DialogHelp(QDialog):
    def __init__(self):
        super(DialogHelp, self).__init__()
        self.InitUI()

    def InitUI(self):
        self.setWindowTitle('帮助')

        layout = QVBoxLayout()
        self.label = QLabel('帮助说明')
        layout.addWidget(self.label)
        self.button1 = QPushButton('退出')
        self.button1.clicked.connect(self.dialogClose)
        self.text = QTextEdit()
        layout.addWidget(self.button1)
        self.setLayout(layout)

    def dialogClose(self):
        print('退出帮助对话框')
        self.close()


# 主窗口
class QDialogDemo(QMainWindow):
    def __init__(self):
        super(QDialogDemo, self).__init__()
        self.InitUI()

    def InitUI(self):
        self.setWindowTitle("QDialog")
        self.setWindowIcon(QIcon("./Images/1.ico"))
        self.resize(300,200)

        #layout = QVBoxLayout()

        self.button1 = QPushButton(self)
        self.button1.setText("设置")
        self.button1.setToolTip('设置')
        self.button1.move(0,0)
        self.button1.clicked.connect(self.showDialog)
        #layout.addWidget(self.button1)

        self.button2 = QPushButton(self)
        self.button2.setText("帮助")
        self.button2.setToolTip('帮助信息')
        self.button2.move(self.button1.width(),0)
        self.button2.clicked.connect(self.showDialog)
        #layout.addWidget(self.button2)

        #self.setLayout(layout)

    def showDialog(self):
        btn = self.sender()
        if btn == self.button1:
            dialog = DialogSet()
        else:
            dialog = DialogHelp()
        dialog.setWindowModality(Qt.ApplicationModal)# 
        dialog.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    widget = QDialogDemo()
    widget.show()

    sys.exit(app.exec_())