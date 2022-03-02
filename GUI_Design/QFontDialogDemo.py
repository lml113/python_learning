'''
字体对话框:QFontDialog
'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class QFontDialogDemo(QWidget):
    def __init__(self):
        super(QFontDialogDemo, self).__init__()
        self.InitUI()
    def InitUI(self):
        self.setWindowTitle("Font Dialog")
        self.setWindowIcon(QIcon('./Images/1.ico'))

        layout = QVBoxLayout()
        self.fontButton = QPushButton('选择字体')
        self.fontButton.clicked.connect(self.getFont)
        self.fontLabel = QLabel('Hello,测试字体例子')
        layout.addWidget(self.fontButton)
        layout.addWidget(self.fontLabel)

        self.setLayout(layout)
    def getFont(self):
        font,ok = QFontDialog.getFont()
        if ok and font:
            self.fontLabel.setFont(font)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    widget = QFontDialogDemo()
    widget.show()

    sys.exit(app.exec_())