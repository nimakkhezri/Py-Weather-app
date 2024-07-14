# Weather class

import requests, json

class Weather:
    def __init__(self, city = "Tehran", api_key = "c72f8b108bde29d725e0fe467e42e228") -> None:
        self.api_key = api_key
        self.city = city

    def get_temp(self) -> float :
        


    def set_city(self, city) -> None :
        self.city = city