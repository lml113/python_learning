'''
绘图API:绘制文本

1、文本
2、各种图形(直线、点、椭圆、弧、扇形、多边形等)
3、图像

QPainter
painter = QPainter()
painter.begin()
painter.drawText()
painter.end()

必须在painterEvent事件方法中绘制各种元素
'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class DrawText(QWidget):
    def __init__(self):
        super(DrawText, self).__init__()
        self.InitUI()
    def InitUI(self):
        self.setWindowTitle('绘图API')
        self.resize(600,400)
        self.text = "Python从菜鸟到高手"
    def paintEvent(self, event):# 方法重写，自动调用
        painter = QPainter(self)
        painter.begin(self)
        painter.setPen(QColor(150,43,5))
        painter.setFont(QFont('Arial',25))
        painter.drawText(event.rect(),Qt.AlignCenter,self.text)
        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    widget = DrawText()
    widget.show()

    sys.exit(app.exec_())