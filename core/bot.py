import apiai
import json


class Bot(object):
    """

    Class to handle the API.AI chat bot api

    """
    def __init__(self, client_token='dc85266a8be84c3ca88fbc70528bd157'):
        """
        Creates the API object and stores the important variables
            :param client_token: the client token given by API.AI
        """

        self.AI = apiai.ApiAI(client_token)
        self.BOSS_NAME = 'Unknown'
        self.BOSS_AGE = 0
        self.BOSS_SEX = 'Unknown'

    def set_boss(self, name, age, sex):
        self.BOSS_NAME = name
        self.BOSS_AGE = int(age)
        self.BOSS_SEX = sex

    def text_query(self, text):
        """
        Handles text queries
            :param text: text to give api.ai to work with
            :return: the response in json format
        """
        request = self.AI.text_request()
        request.query = text
        response = request.getresponse()
        response_json = json.loads(response.read())
        return response_json

    def get_speech(self, json_response):
        """
        Filters out the speech value from a json object given by api.ai
            :param json_response: A python dictionary which contains the converted json string given by api.ai
            :return: A string with the speech response from api.ai
        """
        return str(json_response['result']['fulfillment']['speech'])

    def get_action(self, json_response):
        """
        Filers out the action value from a json object given by api.ai:
            :param json_response: A python dictionary which contains the converted json string given by api.ai
            :return: A string with the suggested action from api.ai
        """
        # print json_response
        try:
            return str(json_response['result']['action'])
        except KeyError:
            return None

    def get_params(self, json_response):
        return str(json_response['result']['action']['parameters'])


