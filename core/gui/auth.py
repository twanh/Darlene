from layouts import authDialog

from PyQt4.QtGui import QDialog


class AuthDialog(QDialog, authDialog.Ui_Dialog):

    def __init__(self, parent = None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.submitBtn.clicked.connect(self.submit)

    def submit(self):
        self.name, self.age, self.sex = self.nameBox.text(), self.ageBox.text(), self.sexBox.text()
        self.accept()
