import time

import keyboard
import pyautogui
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
            self.keyboardRunner()
        else:
            self.pushButton.setText("准备完毕")

    def keyboardRunner(self):
        print(self.lineEdit_8.text())
        print(self.comboBox.currentText())
        keyboard.add_hotkey(self.lineEdit_8.text(), self.on_space)

    def on_space(self):
        pyautogui.press(self.comboBox.currentText(),presses=10000000, interval=float(self.lineEdit.text())/1000)