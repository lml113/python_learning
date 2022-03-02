'''
计数器控件(QSpinBox)
'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class QSpinBoxDemo(QWidget):
    def __init__(self):
        super(QSpinBoxDemo, self).__init__()
        self.InitUI()

    def InitUI(self):
        self.setWindowTitle("计数器控件演示")
        self.resize(300,100)

        layout = QVBoxLayout()
        self.label = QLabel('当前值')
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        self.sb = QSpinBox()
        self.sb.setMaximum(20)
        self.sb.setSingleStep(2)
        self.sb.valueChanged.connect(self.QSpinBoxChanged)
        layout.addWidget(self.sb)

        self.setLayout(layout)

    def QSpinBoxChanged(self):
        self.label.setText("当前值:{}".format(self.sb.value()))
        #print('当前值:{0}'.format(self.sb.value()))
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)

    widget = QSpinBoxDemo()
    widget.show()

    sys.exit(app.exec_())