from PyQt5 import QtCore, QtWidgets
import sys, Browser

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = Browser.MyWindow()
    window.show()

    sys.exit(app.exec())
