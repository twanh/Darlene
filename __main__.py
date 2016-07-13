from core import actions, bot, storage, terminal, gui_handler
import time


def main():
    TERM = terminal.Terminal()
    STORAGE = storage.Storage()
    ACTION = actions.Actions()
    GUI = gui_handler.Handler()
    GUI.run()
    chatting = True
    if STORAGE.check_saved():
        Darlene = STORAGE.load()
        GUI.print_bot('Welcome back %s!' % Darlene.BOSS_NAME)
        GUI.USER_NAME = Darlene.BOSS_NAME
    else:
        TERM.header()
        Darlene = bot.Bot()
        TERM.print_bot('Hello I am Darlene!')
        TERM.print_bot('What is your name?')
        name = TERM.input_boss('You')
        TERM.print_bot('What is your age?')
        age = TERM.input_boss(name)
        TERM.print_bot('What is your sex?')
        sex = TERM.input_boss(name)
        Darlene.set_boss(name, age, sex)
        TERM.print_bot('Okay thank you!')
        STORAGE.save(Darlene)

    while chatting:
        try:
            inp = TERM.input_boss(Darlene.BOSS_NAME)
            if inp.startswith('!'):
                if inp == '!exit' or inp =='!quit':
                    exit(0)
                elif inp == '!clear':
                    TERM.clear()
            elif inp is '':
                continue
            else:
                resp = Darlene.text_query(inp)
                speech = Darlene.get_speech(resp)
                action = Darlene.get_action(resp)
                if not action == '':
                    if ACTION.check_supported(action):
                        if ACTION.SUPPORTED_ACTIONS[action][1]['args'] is not []:
                            if speech is not '':
                                TERM.print_bot(speech)
                            inp = TERM.input_boss(Darlene.BOSS_NAME)
                            ACTION.SUPPORTED_ACTIONS[action][0](inp)
                        else:
                            ACTION.SUPPORTED_ACTIONS[action][0]()
                    else:
                        if speech is not '':
                            TERM.print_bot(speech)
                else:
                    if speech is not '':
                        TERM.print_bot(speech)
        except KeyboardInterrupt:
            print '\n'
            TERM.print_bot('Are you leaving me?')
            inp = TERM.input_boss(Darlene.BOSS_NAME)
            if inp.lower() == 'y' or inp.lower() == 'yes' or inp.lower() == 'yeah':
                TERM.print_bot('Well bye then...')
                exit(0)

if __name__ == '__main__':
    main()
