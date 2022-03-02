'''
滑块控件
'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class QSliderDemo(QWidget):
    def __init__(self):
        super(QSliderDemo, self).__init__()
        self.InitUI()

    def InitUI(self):
        self.setWindowTitle("滑块控件演示")
        self.resize(400,200)

        self.label = QLabel('你好 PyQt5')
        self.label.setFont(QFont('Arial',12))
        self.label.setAlignment(Qt.AlignCenter)

        self.label1 = QLabel('PyQt5')
        self.label1.setFont(QFont('Arial',12))
        self.label1.setAlignment(Qt.AlignCenter)


        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(4)      # 设置最小值
        self.slider.setMaximum(32)      # 设置最大值
        self.slider.setSingleStep(2)    # 设置步长
        self.slider.setValue(24)        # 设置当前值
        self.slider.setTickPosition(QSlider.TicksBelow) #设置刻度的位置，刻度在下面
        self.slider.setTickInterval(2)# 设置刻度间隔
        self.slider.valueChanged.connect(self.sliderChanged)

        self.slider1 = QSlider(Qt.Vertical)
        self.slider1.setMinimum(4)      # 设置最小值
        self.slider1.setMaximum(32)      # 设置最大值
        self.slider1.setSingleStep(2)    # 设置步长
        self.slider1.setValue(24)        # 设置当前值
        self.slider1.setTickPosition(QSlider.TicksBelow) #设置刻度的位置，刻度在下面
        self.slider1.setTickInterval(2)# 设置刻度间隔

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.slider)
        layout.addWidget(self.slider1)
        self.setLayout(layout)
        pass

    def sliderChanged(self):
        size = self.slider.value()
        print('滑块控件当前值:{0}'.format(size))
        self.label.setFont(QFont('Arial',size))

if __name__ == '__main__':
    app = QApplication(sys.argv)

    widget = QSliderDemo()
    widget.show()

    sys.exit(app.exec_())
