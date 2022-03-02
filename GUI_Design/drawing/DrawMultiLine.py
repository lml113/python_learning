'''
绘制不同类型的直线
虚线、点划线等

'''
import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class DrawMultiLine(QWidget):
    def __init__(self):
        super(DrawMultiLine,self).__init__()
        self.InitUI()
    def InitUI(self):
        self.setWindowTitle("设置Pen的样式")
        self.resize(300,300)
    def paintEvent(self, event):# 方法重写，自动调用
        painter = QPainter(self)
        painter.begin(self)

        pen = QPen(Qt.red,2,Qt.SolidLine)
        painter.setPen(pen)
        painter.drawLine(20,40,250,40)

        pen.setStyle(Qt.DashLine)
        painter.setPen(pen)
        painter.drawLine(20,60,250,60)

        pen.setStyle(Qt.DashDotDotLine)
        pen.setColor(Qt.blue)
        painter.setPen(pen)
        painter.drawLine(20,80,250,80)

        size = self.size()

        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    widget = DrawMultiLine()
    widget.show()

    sys.exit(app.exec_())