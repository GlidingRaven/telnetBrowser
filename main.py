import sys, socket, re, time
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QColor
import Server, Browser
HOST = '127.0.0.1'
PORT = 23


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = Browser.MyWindow()
    window.show()

    sys.exit(app.exec())
