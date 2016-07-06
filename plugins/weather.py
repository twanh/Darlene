import pyowm


class Weather(object):
    def __init__(self, api_key='fb819c60c039da5b4ab8a57c027561ad'):
        self.API = pyowm.OWM(api_key)

    def get_weather(self, place, country):
        weather = self.API.weather_at_place('%s,%s' % (place, country))
        return weather

    def wind_speed(self, obj):
        weather = obj
        wind = weather.get_wind()
        speed = wind['speed']

    def get_temp(self, obj):
        temp = obj.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
        max, cur, min = temp['temp_max'], temp['temp'], temp['temp_min']
        return max, cur, min

    def forecast(self, place, country):
        fc = self.API.daily_forecast('%s,%s' % (place, country), limit=6)
        will_have = []

        if fc.will_have_rain():
            will_have.append('rainy')
        if fc.will_have_clouds():
            will_have.append('cloudy')
        if fc.will_have_snow():
            will_have.append('snowy')
        if fc.will_have_storm():
            will_have.append('stormy')
        if fc.will_have_sun():
            will_have.append('sunny')

        return will_have

