from gui import main_window
from PyQt4 import QtCore, QtGui
import sys


class Handler(object):
    def __init__(self):
        self.app = QtGui.QApplication(sys.argv)
        self.MainWindow = QtGui.QMainWindow()
        self.GUI = main_window.MainWindow()

    def run(self):
        self.GUI.setup(self.MainWindow)
        self.MainWindow.show()
        sys.exit(self.app.exec_())
