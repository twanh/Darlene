import pickle, os, random


class Storage:
    """
    Manages and saves information from the user
    """
    def __init__(self):
        """
        Contains the most important variables and creates a save directory
        """
        if os.path.exists(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'saves'))):
            self.save_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'saves'))
        else:
            os.mkdir(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'saves')))
            self.save_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'saves'))

        self.bot_save_name = 'bot.p'

    def save(self, data, name=None):
        """
        Saves data
            :param data: Data to save
            :param name: Name to save the data (*.*)
            :return: None
        """
        if name is None:
            name = self.bot_save_name
        if os.path.isfile(self.save_dir + '/%s' % name):
            os.rename(self.save_dir + '/%s' % name, self.save_dir + '/%s_old%s' % (name, str(random.randint(0, 19000))))

        save_file = open(self.save_dir + '/%s' % name, 'w')
        pickle.dump(data, save_file)
        save_file.close()

    def load(self, name=None):
        """
        Loads saved data
            :param name: Name of the saved data
            :return: The saved data
        """
        if name is None:
            name = self.bot_save_name
        load_file = open(self.save_dir + '/%s' % name, 'r')
        data = pickle.load(load_file)
        load_file.close()
        return data

    def check_saved(self):
        """
        Checks is data is saved
            :return: Returns if data is saved (True, False)
        """
        if os.listdir(self.save_dir) == []:
            return False
        else:
            return True




