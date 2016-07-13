# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'core/gui/mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:

    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class MainWindow(object):

    def setup(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(331, 438)
        MainWindow.setMinimumSize(QtCore.QSize(331, 438))
        MainWindow.setMaximumSize(QtCore.QSize(331, 438))
        MainWindow.setStyleSheet(_fromUtf8("background-color: #444;"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.chatBox = QtGui.QTextEdit(self.centralwidget)
        self.chatBox.setGeometry(QtCore.QRect(0, 0, 331, 401))
        self.chatBox.setStyleSheet(_fromUtf8("border: none;"))
        self.chatBox.setReadOnly(True)
        self.chatBox.setObjectName(_fromUtf8("chatBox"))
        self.messageBox = QtGui.QLineEdit(self.centralwidget)
        self.messageBox.setGeometry(QtCore.QRect(0, 410, 241, 31))
        self.messageBox.setStyleSheet(_fromUtf8("border: none;\n"
                                                "background-color: rgb(99, 99, 99);\n"
                                                "color: \'white\';"))
        self.messageBox.setObjectName(_fromUtf8("messageBox"))
        self.sendBtn = QtGui.QPushButton(self.centralwidget)
        self.sendBtn.setGeometry(QtCore.QRect(240, 410, 92, 31))
        self.sendBtn.setStyleSheet(_fromUtf8("background-color: rgb(99, 99, 99);\n"
                                             "color: \'white\';"))
        self.sendBtn.setObjectName(_fromUtf8("sendBtn"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Darlene", None))
        self.sendBtn.setText(_translate("MainWindow", "Send", None))

