# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'core/gui/auth.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(212, 143)
        Form.setStyleSheet(_fromUtf8("background-color: #444;"))
        self.nameLabel = QtGui.QLabel(Form)
        self.nameLabel.setGeometry(QtCore.QRect(20, 20, 64, 20))
        self.nameLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.nameLabel.setObjectName(_fromUtf8("nameLabel"))
        self.nameBox = QtGui.QLineEdit(Form)
        self.nameBox.setGeometry(QtCore.QRect(90, 10, 113, 30))
        self.nameBox.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.nameBox.setObjectName(_fromUtf8("nameBox"))
        self.ageBox = QtGui.QLineEdit(Form)
        self.ageBox.setGeometry(QtCore.QRect(90, 40, 113, 30))
        self.ageBox.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.ageBox.setObjectName(_fromUtf8("ageBox"))
        self.sexBox = QtGui.QLineEdit(Form)
        self.sexBox.setGeometry(QtCore.QRect(90, 70, 113, 30))
        self.sexBox.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.sexBox.setObjectName(_fromUtf8("sexBox"))
        self.ageLabel = QtGui.QLabel(Form)
        self.ageLabel.setGeometry(QtCore.QRect(20, 50, 64, 20))
        self.ageLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.ageLabel.setObjectName(_fromUtf8("ageLabel"))
        self.sexLabel = QtGui.QLabel(Form)
        self.sexLabel.setGeometry(QtCore.QRect(20, 80, 64, 20))
        self.sexLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.sexLabel.setObjectName(_fromUtf8("sexLabel"))
        self.submitBtn = QtGui.QPushButton(Form)
        self.submitBtn.setGeometry(QtCore.QRect(60, 110, 92, 28))
        self.submitBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.submitBtn.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"border: none;\n"
"background-color: rgb(108, 103, 103);\n"
""))
        self.submitBtn.setObjectName(_fromUtf8("submitBtn"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.nameLabel.setText(_translate("Form", "Name:", None))
        self.ageLabel.setText(_translate("Form", "Age:", None))
        self.sexLabel.setText(_translate("Form", "Sex:", None))
        self.submitBtn.setText(_translate("Form", "Submit", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

