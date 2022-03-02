'''
用像素点绘制正弦曲线
-2PI 2PI
drawPoint(x,y)

'''
import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class DrawPoints(QWidget):
    def __init__(self):
        super(DrawPoints, self).__init__()
        self.InitUI()
    def InitUI(self):
        self.setWindowTitle("绘制正弦曲线")
        self.resize(300,300)
    def paintEvent(self, event):# 方法重写，自动调用
        painter = QPainter(self)
        painter.begin(self)
        painter.setPen(Qt.blue)
        size = self.size()
        # 绘制正弦波
        for i in range(1000):
            x = 100*(-1.5+3.0*i/1000)+size.width()/2.0
            y = -100*math.sin((x-size.width()/2.0)*math.pi/50)+size.height()/2.0
            painter.drawPoint(x,y)
        
        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    widget = DrawPoints()
    widget.show()

    sys.exit(app.exec_())