import sys
import Ui_MainWin
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon

class FirstMainWin(QMainWindow):
    def __init__(self):
        super(FirstMainWin, self).__init__()
        # 设置主窗口的标题
        self.setWindowTitle("第一个主窗口应用")
        # 窗口图标
        self.setWindowIcon(QIcon('./Images/4.ico'))
        # 设置窗口尺寸
        self.resize(400,300)
        # 窗口居中
        self.center()

    # 实例方法
    def center(self):
        # 获取屏幕坐标
        screen = QApplication.desktop()
        print("屏幕宽度：{0:4}；屏幕高度：{1:4}".format(screen.width(), screen.height()))
        size = self.geometry()
        print("窗口宽度：{0:4}；窗口高度：{1:4}".format(size.width(), size.height()))
        newLef = (screen.width() - size.width())/2
        newTop = (screen.height() - size.height())/2
        self.move(newLef, newTop)

    def message(self):
        self.status = self.statusBar()
        self.status.showMessage("只存在5秒的消息", 5000)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainWindow = FirstMainWin()
    ui = Ui_MainWin.Ui_MainWindow()
    # 主窗口添加控件
    ui.setupUi(mainWindow)

    mainWindow.message()
    mainWindow.show()

    sys.exit(app.exec_())