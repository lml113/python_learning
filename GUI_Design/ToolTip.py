import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QHBoxLayout, QToolTip
from PyQt5.QtGui import QIcon, QFont

class ToolTip(QMainWindow):
    def __init__(self):
        super(ToolTip, self).__init__()
        self.InitUI()

    def InitUI(self):
        QToolTip.setFont(QFont("KaiTi",12))
        self.setToolTip('今天是<b>星期五</b>')
        self.resize(400,300)
        self.setWindowTitle("设置控件提示消息")
        self.setWindowIcon(QIcon("./Images/1.ico"))
        # 添加Button
        self.button1 = QPushButton('EXIT')
        self.button1.setToolTip("退出")
        # 将信号与槽关联
        self.button1.clicked.connect(self.onClick_Button)
        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)

        self.setCentralWidget(mainFrame)

    # 按键单击事件的方法(自定义的槽)
    def onClick_Button(self):
        sender = self.sender()
        print(sender.text()+' 按钮被按下')
        app = QApplication.instance()
        # 推出应用程序
        app.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainwin = ToolTip()
    mainwin.show()

    sys.exit(app.exec_())
