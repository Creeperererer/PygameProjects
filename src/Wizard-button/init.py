import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from logic import *


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = mainUI()
    myWin.show()
    sys.exit(app.exec_())