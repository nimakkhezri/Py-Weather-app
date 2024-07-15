# Weather class

import requests, json

class Weather:
    def __init__(self, city = "Tehran", api_key = "c72f8b108bde29d725e0fe467e42e228") -> None:
        self.api_key = api_key
        self.city = city
        self.set_url()

    def get_responce(self) -> json:
        res = requests.get(self.url)
        return res.json() 

    def set_url(self) -> None:
        self.url = f"https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.api_key}"

    def get_kelvin_temp(self) -> float:
        data = self.get_responce()
        main = data["main"]
        return main["temp"]
        
    def get_celcius_temp(self) -> int:
        kelvin = self.get_kelvin_temp()
        celsius = kelvin - 273.15
        return round(celsius)

    def set_city(self, city) -> None :
        self.city = city
        self.set_url()