from gui import main_window
from PyQt4 import QtCore, QtGui
import sys


class Handler(object):
    def __init__(self):

        self.inp = ''

        self.USER_NAME = 'Unknown'

        self.user_prefix = '<h4 style="color:#3E6BC6;">[' + self.USER_NAME + ']> </h4>'
        self.bot_prefix = '<h4 style="color:#4EC909;">[Darlene]> </h4>'
        self.app = QtGui.QApplication(sys.argv)
        self.MainWindow = QtGui.QMainWindow()
        self.MainGUI = main_window.MainWindow()
        self.MainGUI.setup(self.MainWindow)
        self.MainGUI.sendBtn.clicked.connect(self.user_inp)
        self.MainGUI.messageBox.returnPressed.connect(self.MainGUI.sendBtn.click)

        self.chatBoxCursor = QtGui.QTextCursor(self.MainGUI.chatBox.document())

    def user_inp(self):
        self.inp = self.MainGUI.messageBox.text()
        self.MainGUI.messageBox.clear()

    def print_user(self, text):
        self.chatBoxCursor.insertHtml(self.user_prefix)
        self.chatBoxCursor.insertHtml(text + '<br>')

    def print_bot(self, text):
        self.chatBoxCursor.insertHtml(self.bot_prefix)
        self.chatBoxCursor.insertHtml(text + '<br>')

