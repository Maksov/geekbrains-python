import gzip
import json
from io import BytesIO
import requests
from pymongo import MongoClient


class DB(object):
    """An API to MongoDB"""

    version = '0.3'

    def __init__(self, host, port, name):
        self.client = MongoClient(host, port)
        self.db = self.client[name]
        self.collection = self.db[name]


class CityDB(DB):
    """ An API to City DB"""

    _url = 'http://bulk.openweathermap.org/sample/city.list.json.gz'

    def find_by_city(self, city):
        return self.collection.find({"name": city})

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


class WeatherDB(DB):
    """ An API to Weather DB"""

    pass


if __name__ == '__main__':
    db_host = '172.17.0.2'
    db_port = 27017
    db_name = 'cities'
    # db = WeatherDB.create_db(db_host, db_port, db_name)
    db = CityDB(db_host, db_port, db_name)
