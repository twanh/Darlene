import sys

from PyQt4 import QtGui

import core.actions
import core.bot
import core.storage
from core.gui import auth
from gui import main_window


class Handler(object):

    def __init__(self):

        self.inp = ''
        self.check_inp = 'startText..q.w.fq.f'
        self.need_input = False
        self.gave_input = False

        self.isUser = False

        self.app = QtGui.QApplication(sys.argv)
        self.MainWindow = QtGui.QMainWindow()
        self.MainGUI = main_window.MainWindow()
        self.MainGUI.setup(self.MainWindow)
        self.MainGUI.sendBtn.clicked.connect(self.user_inp)
        self.MainGUI.messageBox.returnPressed.connect(self.MainGUI.sendBtn.click)
        self.chatBoxCursor = QtGui.QTextCursor(self.MainGUI.chatBox.document())

        self.dialog = auth.AuthDialog()

        self.STORAGE = core.storage.Storage()

        if self.STORAGE.check_saved():
            self.Darlene = self.STORAGE.load()
            self.USER_NAME = self.Darlene.BOSS_NAME
            self.isUser = True
        else:
            self.Darlene = core.bot.Bot()

        self.ACTIONS = core.actions.Actions()

        self.USER_NAME = self.Darlene.BOSS_NAME

    def start(self):
        self.MainWindow.show()
        sys.exit(self.app.exec_())

    def user_inp(self):
        self.check_inp = self.inp
        self.inp = self.MainGUI.messageBox.text()
        self.MainGUI.messageBox.clear()
        self.print_user(self.inp)
        self.handle_inp()

    def handle_inp(self):
        inp = str(self.inp)
        if not self.isUser and not inp.startswith('!auth'):
            self.print_bot('You need to authenticate your self! Type: !authenticate or !auth to authenticate.')
        else:

            if inp.startswith('!'):
                if inp == '!auth' or inp == '!authenticate':
                    self.auth()
                elif inp == '!exit' or inp == '!quit':
                    sys.exit(0)
                elif inp == '!clear':
                    self.MainGUI.chatBox.clear()
                else:
                    pass
            else:
                resp = self.Darlene.text_query(inp)
                speech = self.Darlene.get_speech(resp)
                action = self.Darlene.get_action(resp)
                if not action == '':
                    if self.ACTIONS.check_supported(action):
                        if self.ACTIONS.SUPPORTED_ACTIONS[action][1]['args'] is not []:
                            if speech is not '':
                                self.print_bot(speech)
                            # inp = TERM.input_boss(Darlene.BOSS_NAME)
                            # ACTION.SUPPORTED_ACTIONS[action][0](inp)
                        else:
                            self.ACTIONS.SUPPORTED_ACTIONS[action][0]()
                    else:
                        if speech is not '':
                            self.print_bot(speech)
                else:
                    if speech is not '':
                        self.print_bot(speech)

    def print_user(self, text):
        self.chatBoxCursor.insertHtml('<h4 style="color:#3E6BC6;">[' + self.USER_NAME + ']> </h4>')
        self.chatBoxCursor.insertHtml(text + '<br>')

    def print_bot(self, text):
        self.chatBoxCursor.insertHtml('<h4 style="color:#4EC909;">[Darlene]> </h4>')
        self.chatBoxCursor.insertHtml(text + '<br>')

    def auth(self):
        if self.dialog.exec_():
            name, age, sex = str(self.dialog.name), int(str(self.dialog.age)), str(self.dialog.sex)
            print name
            self.USER_NAME = name
            self.Darlene.set_boss(name, age, sex)
            self.isUser = True




