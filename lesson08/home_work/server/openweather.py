""" An API to OpenWeatherMap (https://openweathermap.org)"""
import requests


class OpenWeather(object):

    version = '0.1'

    def __init__(self, appid):
        self.appid = appid

    def get_by_id(self, city_id):
        url = 'http://api.openweathermap.org/data/2.5/weather'
        payload = {
            'id': city_id,
            'appid': self.appid
        }
        return requests.get(url, params=payload).json()


if __name__ == '__main__':
    with open('app.id', 'r') as f:
        data = f.read()
        app_id = data.split('=')[1].strip()
        print(app_id)
    weather = OpenWeather(app_id)
