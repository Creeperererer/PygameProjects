import time

import keyboard
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from main import Ui_MainWindow

class mainUI(QMainWindow,Ui_MainWindow):
    flag = 1
    def __init__(self, parent=None):
        super(mainUI, self).__init__(parent)
        self.setupUi(self)
        # TODD 初始化事件
        self.pushButton.clicked.connect(self.onClicked)
        self.pushButton_2.clicked.connect(self.onClicked2)


    def onClicked(self):
        if(self.pushButton.text()=="准备完毕"):
            self.pushButton.setText("运行中")
            self.flag=1
            self.keyboardRunner()
        else:
            QMessageBox.information(self, "警告", "不要乱按",
                                    QMessageBox.Yes)

    def onClicked2(self):
        if(self.pushButton.text()=="运行中"):
            self.pushButton.setText("准备完毕")
            self.flag=0
        else:
            self.pushButton.setText("准备完毕")
            self.flag=0
            self.keyboardRunner()


    def keyboardRunner(self):
        keyboard.add_hotkey(self.lineEdit_b1.text(), self.on_space)
        # keyboard.add_hotkey(self.lineEdit_b2.text(), self.on_space2)
        # keyboard.add_hotkey(self.lineEdit_b3.text(), self.on_space3)
        # keyboard.add_hotkey(self.lineEdit_b4.text(), self.on_space4)

    def on_space(self):
        while(self.flag):
            keyboard.press_and_release(self.comboBox.currentText())
            time.sleep(float(self.lineEdit_a1.text())/1000)
    def on_space2(self):
        while(self.flag):
            keyboard.press_and_release(self.comboBox_2.currentText())
            time.sleep(float(self.lineEdit_a2.text())/1000)
    def on_space3(self):
        while(self.flag):
            keyboard.press_and_release(self.comboBox_3.currentText())
            time.sleep(float(self.lineEdit_a3.text())/1000)
    def on_space4(self):
        while(self.flag):
            keyboard.press_and_release(self.comboBox_4.currentText())
            time.sleep(float(self.lineEdit_a4.text())/1000)