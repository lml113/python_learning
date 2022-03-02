import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QWidget
from PyQt5.QtGui import QIcon

class QuitApplication(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(400,300)
        self.setWindowTitle("退出应用程序")
        self.setWindowIcon(QIcon('./Images/1.ico'))

        # 添加Button
        self.button1 = QPushButton('EXIT')
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
    MainWin = QuitApplication()
    MainWin.show()

    sys.exit(app.exec_())

