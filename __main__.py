from core import actions, bot, storage, gui_handler
import time, sys


def main():

    STORAGE = storage.Storage()
    ACTION = actions.Actions()
    GUI = gui_handler.Handler()
    GUI.start()

if __name__ == '__main__':
    main()
