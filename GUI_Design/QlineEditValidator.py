'''
现在QlineEdit控件的输入（校验器）
如显限制只能输入整数、浮点数或满足一定条件的字符串


'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator,QIcon
from PyQt5.QtCore import QRegExp

class QLineEditValidator(QWidget):
    def __init__(self):
        super(QLineEditValidator, self).__init__()
        self.InitUI()

    def InitUI(self):
        self.setWindowTitle("校验器")
        self.setWindowIcon(QIcon("./Images/4.ico"))

        formLayout = QFormLayout()      # 创建表单布局
        
        intLineExit = QLineEdit()
        intLabel = QLabel("&整数类型")
        doubleLineExit = QLineEdit()
        doubleLabel = QLabel("&浮点类型")
        validatorLineExit = QLineEdit()
        validatorLabel = QLabel("&数字和字母")

        # 设置伙伴控件
        intLabel.setBuddy(intLineExit)
        doubleLabel.setBuddy(doubleLineExit)
        validatorLabel.setBuddy(validatorLineExit)

        formLayout.addRow(intLabel,intLineExit)
        formLayout.addRow(doubleLabel,doubleLineExit)
        formLayout.addRow(validatorLabel,validatorLineExit)

        intLineExit.setPlaceholderText("整型")
        doubleLineExit.setPlaceholderText("浮点型")
        validatorLineExit.setPlaceholderText("字母和数字")

        # 整数校验器[0,99]
        intValidator = QIntValidator()
        intValidator.setRange(0,99)

        # 浮点校验器[-360,360]
        doubleValidator = QDoubleValidator()
        doubleValidator.setRange(-360,360)
        doubleValidator.setNotation(QDoubleValidator.StandardNotation)
        # 设置精度，小数点2位
        doubleValidator.setDecimals(2)

        # 字符和数字
        reg = QRegExp(r'[a-zA-Z0-9]+$')
        validator = QRegExpValidator()
        validator.setRegExp(reg)

        # 设置校验位
        intLineExit.setValidator(intValidator)
        doubleLineExit.setValidator(doubleValidator)
        validatorLineExit.setValidator(validator)

        self.setLayout(formLayout)
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = QLineEditValidator()
    widget.show()

    sys.exit(app.exec_())
