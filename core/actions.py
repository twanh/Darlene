from plugins.image_recognition.image_reconision import ImageRecognition
from plugins import weather
from core import terminal
import os, random


class Actions(object):
    """
    A class to handle all actions from the bot
    """

    def __init__(self):
        """
        Holds the most important variables that are needed in other functions
        """
        # A dictionary containing all the function names and actual function objects
        self.SUPPORTED_ACTIONS = {'recon_image': [self.recon_img, {'args': ['path']}], 'get_forecast': [self.get_forecast, {'args': ['inp']}]}

        self.img_recon = ImageRecognition()
        self.TERM = terminal.Terminal()
        self.WEATHER = weather.Weather()

    def check_supported(self, action):
        """
        Checks if a function is supported
            :param action: A sting containing a function name
            :return: If a function is supported or not (True, Fales)
        """
        if action in self.SUPPORTED_ACTIONS:
            return True
        else:
            return False

    def recon_img(self, path):
        """
        A function that interacts with the image recognition plugin
            :param path: Path (directory,file,url) to the image(s) to tag
            :return: None
        """
        path = path
        if path.startswith('http'):
            response = self.img_recon.tag_image_url(path)
        elif os.path.isdir(path):
            response = self.img_recon.tag_images_dir(path)
        else:
            response = self.img_recon.tag_image(path)

        most_likely = self.img_recon.get_most_likely(response)
        randomnr = random.randint(0, 4)
        if randomnr == 0:
            self.TERM.print_bot('I think that it is a: %s' % most_likely)
        elif randomnr == 1:
            self.TERM.print_bot('I guess that it is a: %s' % most_likely)
        elif randomnr == 2:
            self.TERM.print_bot('I assume that is is a: %s' % most_likely)
        elif randomnr == 3:
            self.TERM.print_bot('It\'s a: %s' % most_likely)
        elif randomnr == 4:
            self.TERM.print_bot('My guess is that it is a: %s' % most_likely)
        else:
            self.TERM.print_bot('I guess that it is a: %s' % most_likely)

    def get_forecast(self, inp):
        place, country = inp.split(',')
        forecast = self.WEATHER.forecast(place, country)
        randomnr = random.randint(0, 4)
        if randomnr == 0:
            self.TERM.print_bot('The weather in '+ place + ',' + country + ' will be: %s' % ','.join(map(str,
                                                                                                         forecast)))
        elif randomnr == 1:
            self.TERM.print_bot('I think the weather in ' + place + ',' + country + ' will be: %s'
                                % ','.join(map(str, forecast)))
        elif randomnr == 2:
            self.TERM.print_bot('My sources say that weather in ' + place + ',' + country + ' will be: %s'
                                % ','.join(map(str, forecast)))
        elif randomnr == 3:
            self.TERM.print_bot('In ' + place + ',' + country + ' will the weather be: %s' % ','.join(map(str,
                                                                                                          forecast)))
        elif randomnr == 4:
            self.TERM.print_bot('The weather in ' + place + ',' + country + ' will be: %s' % ','.join(map(str,
                                                                                                          forecast)))
        else:
            self.TERM.print_bot('The weather in ' + place + ',' + country + ' will be: %s' % ','.join(map(str,
                                                                                                          forecast)))



