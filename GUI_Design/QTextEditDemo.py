'''
QTextEdit控件
'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

class QTextEditDemo(QWidget):
    def __init__(self):
        super(QTextEditDemo, self).__init__()
        self.InitUI()

    def InitUI(self):
        self.setWindowTitle('QTextEdit控件演示')
        self.setWindowIcon(QIcon('./Images/4.ico'))
        self.resize(300,200)
        self.textEdit = QTextEdit()
        self.buttonText = QPushButton('显示文本')
        self.buttonHTML = QPushButton('显示HTML')
        self.buttonToText = QPushButton('获取文本')
        self.buttonToHTML = QPushButton('获取HTML')

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.buttonText)
        layout.addWidget(self.buttonHTML)
        layout.addWidget(self.buttonToText)
        layout.addWidget(self.buttonToHTML)

        self.setLayout(layout)

        self.buttonText.clicked.connect(self.onClick_ButtonText)
        self.buttonHTML.clicked.connect(self.onClick_ButtonHTML)
        self.buttonToText.clicked.connect(self.onClick_ButtonToText)
        self.buttonToHTML.clicked.connect(self.onClick_ButtonToHTML)
        pass

    def onClick_ButtonText(self):
        self.textEdit.setPlainText("Hello World，世界你好！")

    def onClick_ButtonHTML(self):
        self.textEdit.setHtml('<font color="blue" size="5">Hello World!</font>')

    def onClick_ButtonToText(self):
        print('获取文本'+self.textEdit.toPlainText())

    def onClick_ButtonToHTML(self):
        print(''+self.textEdit.toHtml())


if __name__ == '__main__':
    app = QApplication(sys.argv)

    widget = QTextEditDemo()
    widget.show()

    sys.exit(app.exec_())
