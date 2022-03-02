'''
下拉列表控件(QComboBox)
1、如何将列表项添加到QComboBox控件中
2、如何获取选中的列表项
'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class QComboBoxDemo(QWidget):
    def __init__(self):
        super(QComboBoxDemo, self).__init__()
        self.InitUI()
    
    def InitUI(self):
        self.setWindowTitle('下拉列表控件')
        self.resize(300,100)

        self.label = QLabel('请选择编程语言')
        # self.label.setAlignment(Qt.AlignCenter)
        self.cb = QComboBox()
        s=['','C/C++','Python','Java','JavaScript','C#','Html','CSS']
        self.cb.addItems(s)
        self.cb.currentIndexChanged.connect(self.selectionChange)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.cb)
        self.setLayout(layout)
        pass

    def selectionChange(self):
        self.label.setText(self.cb.currentText())
        self.label.adjustSize()
        for count in range(self.cb.count()):
            print('item{} = {}'.format(count,self.cb.itemText(count)))

if __name__ == "__main__":
    app =QApplication(sys.argv)

    widget = QComboBoxDemo()
    widget.show()

    sys.exit(app.exec_())
