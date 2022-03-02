'''
QlineEdit综合案例
'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

class QLineEditDemo(QWidget):
    def __init__(self):
        super(QLineEditDemo, self).__init__()
        self.InitUI()

    def InitUI(self):
        self.setWindowTitle('QlineEdit综合案例')
        self.setWindowIcon(QIcon('./Images/4.ico'))

        edit1 = QLineEdit(self)
        edit1.setValidator(QIntValidator())
        edit1.setMaxLength(4)
        edit1.setAlignment(Qt.AlignRight)
        edit1.setFont(QFont('Arial',12))

        edit2 = QLineEdit(self)
        edit2.setValidator(QDoubleValidator(0.99,99.99,2))

        edit3 = QLineEdit(self)
        edit3.setInputMask('99-9999-999999;#')
        edit3.setAlignment(Qt.AlignCenter)

        edit4 = QLineEdit(self)
        edit4.setValidator(QIntValidator(0,9999))
        edit4.textChanged.connect(self.textChange)
        edit4.editingFinished.connect(self.edit4TextFinished)

        edit5 = QLineEdit(self)
        edit5.setEchoMode(QLineEdit.Password)
        edit5.editingFinished.connect(self.enterPress)

        edit6 = QLineEdit('Hello PyQt5')
        edit6.setReadOnly(True)

        formLayout = QFormLayout()
        formLayout.addRow('整数校验',edit1)
        formLayout.addRow('浮点数校验',edit2)
        formLayout.addRow('Input Mask',edit3)
        formLayout.addRow('文本变化',edit4)
        formLayout.addRow('密码',edit5)
        formLayout.addRow('只读',edit6)

        self.setLayout(formLayout)

    def textChange(self,text):
        print('输入内容：' + text)
        self.edit4Text = text

    def edit4TextFinished(self):
        print('已输入值:' + self.edit4Text)

    def enterPress(self):
        print('已输入值')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    widget = QLineEditDemo()
    widget.show()

    sys.exit(app.exec_())
