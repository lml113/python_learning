'''
单选按钮控件(QRadioButton)
'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class QRadioButtonDemo(QWidget):
    def __init__(self):
        super(QRadioButtonDemo, self).__init__()
        self.InitUI()

    def InitUI(self):
        self.setWindowTitle("QRadioButton")

        layout = QHBoxLayout()
        self.button1 = QRadioButton('单选按钮1')
        #self.button1.setChecked(True)
        self.button1.toggled.connect(lambda:self.ButtonStatus(self.button1))

        self.button2 = QRadioButton('单选按钮2')
        #self.button2.setChecked(True)
        self.button2.toggled.connect(lambda:self.ButtonStatus(self.button2))

        layout.addWidget(self.button1)
        layout.addWidget(self.button2)

        self.setLayout(layout)

    def ButtonStatus(self,btn):
        if btn.isChecked():
            print('<' + btn.text() + '>被选中')
        else:
            print('<' + btn.text() + '>被取消选中状态')
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = QRadioButtonDemo()
    widget.show()

    sys.exit(app.exec_())
