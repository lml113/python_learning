'''
QLable 控件
setAlignment()：设置文本的对齐方式
setIndent()：设置文本缩进
text()：获取文本内容
setBuddy()：设置伙伴关系
setText()：设置文本内容
selectedText()：返回所选择的字符
setWordWrap()：设置是否允许换行
QLable常用的信号（时间）：
1、当鼠标滑过QLable控件时触发：linkHovered
2、当鼠标单击QLable控件时触发：linkActivated

'''
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QIcon, QFont, QPalette, QPixmap
from PyQt5.QtCore import Qt

class QlabelDemo(QWidget):
    def __init__(self):
        super(QlabelDemo, self).__init__()
        self.InitUI()

    def InitUI(self):
        self.resize(400,300)
        self.setWindowTitle("Qlabel控件演示")
        self.setWindowIcon(QIcon("./Images/4.ico"))
        # 
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText("<font color=yellow>这是一个文本标签。</font>")# 显示文字
        label1.setAutoFillBackground(True)  # 设置背景颜色
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.blue)
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)# 文字居中

        label2.setText('<a href="#">欢迎使用Python GUI程序</a>')

        label3.setAlignment(Qt.AlignCenter)# 居中
        label3.setToolTip("这是一个图片标签")
        label3.setPixmap(QPixmap('./Images/1.ico'))# 加载图片

        label4.setText("<a href='https://www.taobao.com'>淘宝</a>")
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip("这是一个淘宝链接")

        vbox = QVBoxLayout()# 垂直布局

        vbox.addWidget(label1)# 加载控件
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)

        label2.linkHovered.connect(self.linkHovered)# 信号/槽绑定
        label4.linkActivated.connect(self.linkClicked)

        self.setLayout(vbox)

    def linkHovered(self):
        print("当鼠标划过label2标签时，触发事件")

    def linkClicked(self):
        print("当鼠标划过label4标签时，触发事件")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainwin  = QlabelDemo()
    mainwin.show()

    sys.exit(app.exec_())