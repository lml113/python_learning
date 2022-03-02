'''
输入对话框:QInputDialog
QInputDialog.getItem
QInputDialog.getText
QInputDialog.getInt
'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class QInputDialogDemo(QWidget):
    def __init__(self):
        super(QInputDialogDemo, self).__init__()
        self.InitUI()
    def InitUI(self):
        self.setWindowTitle('输入对话框')
        self.setWindowIcon(QIcon("./images/1.ico"))

        layout = QFormLayout()
        self.button1 = QPushButton('获取列表中的选项')
        self.button1.clicked.connect(self.getItem)
        self.lineExit1 = QLineEdit()
        self.lineExit1.setAlignment(Qt.AlignCenter)
        layout.addRow(self.button1,self.lineExit1)

        self.button2 = QPushButton('获取字符串')
        self.button2.clicked.connect(self.getText)
        self.lineExit2 = QLineEdit()
        self.lineExit2.setAlignment(Qt.AlignCenter)
        layout.addRow(self.button2,self.lineExit2)

        self.button3 = QPushButton('获取整数')
        self.button3.clicked.connect(self.getInt)
        self.lineExit3 = QLineEdit()
        self.lineExit3.setAlignment(Qt.AlignCenter)
        layout.addRow(self.button3,self.lineExit3)

        self.setLayout(layout)
        pass
    def getItem(self):
        items = ('','C','C++','Python','Java','C#','JavaScript','QT')
        item,ok = QInputDialog.getItem(self,'请选择编程语言','语言列表',items)
        if ok and item:
            self.lineExit1.setText(item)
    def getText(self):
        text,ok = QInputDialog.getText(self,'文本输入框','输入姓名')
        if ok and text:
            self.lineExit2.setText(text)
    def getInt(self):
        num,ok = QInputDialog.getInt(self,'整数输入框','输入整数')
        if ok and num:
            self.lineExit3.setText(str(num))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    widget = QInputDialogDemo()
    widget.show()

    sys.exit(app.exec_())
