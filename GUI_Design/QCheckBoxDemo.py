'''
复选框控件(QCheckBox)
3种状态
未选中:0
半选中:1
选中:2
'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class QCheckBoxDemo(QWidget):
    def __init__(self):
        super(QCheckBoxDemo, self).__init__()
        self.InitUI()

    def InitUI(self):
        self.setWindowTitle("复选框控件")

        self.checkBox1 = QCheckBox('复选框控件1')
        self.checkBox1.setChecked(True)
        self.checkBox1.stateChanged.connect(lambda:self.checkBoxStatus(self.checkBox1))
        self.checkBox2 = QCheckBox('复选框控件2')
        self.checkBox2.stateChanged.connect(lambda:self.checkBoxStatus(self.checkBox2))
        self.checkBox3 = QCheckBox('半选中')
        self.checkBox3.stateChanged.connect(lambda:self.checkBoxStatus(self.checkBox3))
        self.checkBox3.setTristate(True)# 设置三只状态时，必须先设置这个
        self.checkBox3.setCheckState(Qt.PartiallyChecked)# 设置三种状态中的其中一种
        
        layout = QHBoxLayout()
        layout.addWidget(self.checkBox1)
        layout.addWidget(self.checkBox2)
        layout.addWidget(self.checkBox3)
        self.setLayout(layout)

    def checkBoxStatus(self,btn):
        print('{0},isChecked = {1},checkState = {2}'.format(btn.text(),btn.isChecked(),btn.checkState()))
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = QCheckBoxDemo()
    widget.show()

    sys.exit(app.exec_())
