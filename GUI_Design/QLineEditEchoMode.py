'''
QLineExit控件与回显模式
基本功能：输入单行的文本
EchoMode（回显模式）

4中回显模式
1、Normal       输入的时候显示
2、NoEcho       输入的时候不显示
3、Password
4、passwordEchoOnEdit

'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

class QLineEditEchoMode(QWidget):
    def __init__(self):
        super(QLineEditEchoMode,self).__init__()
        self.InitUI()

    def InitUI(self):
        self.setWindowTitle('文本输入框的回显模式')
        self.setWindowIcon(QIcon("./Images/4.ico"))

        formLayout = QFormLayout()

        normelLineEdit = QLineEdit()
        noEchoLineEdit = QLineEdit()
        passwordLineEdit = QLineEdit()
        passwordEchoOnEditLineEdit = QLineEdit()

        formLayout.addRow("Normael",normelLineEdit)
        formLayout.addRow("NoEcho",noEchoLineEdit)
        formLayout.addRow("Password",passwordLineEdit)
        formLayout.addRow("PasswordEchoOnEdit",passwordEchoOnEditLineEdit)

        normelLineEdit.setPlaceholderText("Normal")
        noEchoLineEdit.setPlaceholderText("NoEcho")
        passwordLineEdit.setPlaceholderText("Password")
        passwordEchoOnEditLineEdit.setPlaceholderText("PasswordEchoOnEdit")

        normelLineEdit.setEchoMode(QLineEdit.Normal)
        noEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        passwordLineEdit.setEchoMode(QLineEdit.Password)
        passwordEchoOnEditLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.setLayout(formLayout)



if __name__ == '__main__':
    app = QApplication(sys.argv)

    weight = QLineEditEchoMode()
    weight.show()

    sys.exit(app.exec_())

