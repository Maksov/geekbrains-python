import gzip
import json
from io import BytesIO
import requests
from pymongo import MongoClient


class WeatherDB(object):
    """An API to Weather MongoDB"""

    version = '0.2'
    _url = 'http://bulk.openweathermap.org/sample/city.list.json.gz'

    def __init__(self, host, port, name):
        self.client = MongoClient(host, port)
        self.db = self.client[name]
        self.collection = self.db[name]

    @classmethod
    def create_db(cls, host, port, name):
        """Create cities db and collection from OpenWeatherMap source"""
        gzip_data = BytesIO(requests.get(cls._url).content)
        json_file = gzip.open(gzip_data)
        cities_db = cls(host, port, name)
        cities = cities_db.collection
        for line in json_file.readlines():
            city = json.loads(line.decode())
            cities.insert_one(city)
        return cities_db


if __name__ == '__main__':
    db_host = '172.17.0.2'
    db_port = 27017
    db_name = 'cities'
    # db = WeatherDB.create_db(db_host, db_port, db_name)
    db = WeatherDB(db_host, db_port, db_name)
