import os, time, sys
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format


class Terminal:
    """
    Provides usefull functions for in the terminal
    """
    def __init__(self):
        """
        Holds all the colors
        """
        init(strip=not sys.stdout.isatty())

        self.HEADER = '\033[95m'
        self.OKBLUE = '\033[94m'
        self.OKGREEN = '\033[92m'
        self.WARNING = '\033[93m'
        self.FAIL = '\033[91m'
        self.ENDC = '\033[0m'
        self.BOLD = '\033[1m'
        self.UNDERLINE = '\033[4m'
        self.CYAN = '\033[36m'

    def print_bot(self, text):
        """
        Prints the default way of printing for the bot
            :param text: Text to print (string)
            :return: NONE
        """
        print '%s%s[Darlene]>%s%s %s' % (self.OKBLUE, self.BOLD, self.ENDC, self.CYAN, text)

    def print_boss(self, text, name):
        """
        Prints the default way of printing for the boss
            :param text: Text to print (string)
            :param name: Name of the boss (string)
            :return: NONE
        """
        print '%s%s[%s]>%s%s %s' % (self.OKBLUE, self.BOLD, name, self.ENDC, self.OKGREEN, text)

    def input_boss(self, name):
        """
        Gets input from the boss using the default terminal printing
            :param name: Name of the boss (string)
            :return: input given by the user (string)
        """
        inp = raw_input('%s%s[%s]>%s%s ' % (self.OKBLUE, self.BOLD, name, self.ENDC, self.OKGREEN))
        return inp

    def clear(self):
        """
        Clears the terminal
            :return: None
        """
        os.system('clear')

    def header(self, welcome_back=False):
        """
        Prints the header of the application
            :param welcome_back: Boolean, If the user has used the application before
            :return: None
        """
        self.clear()
        print 'Darlene is starting.'
        time.sleep(0.4)
        self.clear()
        print 'Darlene is starting..'
        time.sleep(0.4)
        self.clear()
        print 'Darlene is starting..'
        time.sleep(0.4)
        self.clear()
        if welcome_back:
            print '%sWelcome back to%s: \n\n' % (self.OKBLUE, self.ENDC)
        else:
            print '%sWelcome to%s: \n\n' % (self.OKBLUE, self.ENDC)
        cprint(figlet_format("Darlene", font='block'),
               'blue', attrs=['bold'])
