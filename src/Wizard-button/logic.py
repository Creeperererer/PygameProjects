from PyQt5.QtWidgets import QApplication,QMainWindow
from main import Ui_MainWindow

class mainUI(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(mainUI, self).__init__(parent)
        self.setupUi(self)
        # TODD 初始化事件
        self.pushButton.clicked.connect(self.onClicked)


    def onClicked(self):
        if(self.pushButton.text()=="准备完毕"):
            self.pushButton.setText("运行中")
        else:
            self.pushButton.setText("准备完毕")
