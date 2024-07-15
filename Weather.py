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
        
    def get_celsius_temp(self) -> int:
        kelvin = self.get_kelvin_temp()
        celsius = kelvin - 273.15
        return round(celsius)
    
    def get_max_kelvin_temp(self) -> float:
        data = self.get_responce()
        main = data["main"]
        return main["temp_max"]
    
    def get_min_kelvin_temp(self) -> float:
        data = self.get_responce()
        main = data["main"]
        return main["temp_min"]
    
    def get_min_celsius_temp(self) -> int:
        kelvin = self.get_min_kelvin_temp()
        celsius = kelvin - 273.15
        return round(celsius)
    
    def get_max_celsius_temp(self) -> int:
        kelvin = self.get_max_kelvin_temp()
        celsius = kelvin - 273.15
        return round(celsius)
    
    def get_description(self) -> str:
        data = self.get_responce()
        description = data["weather"][0]["main"] + " : " + data["weather"][0]["description"]
        return description

    def set_city(self, city) -> None :
        self.city = city
        self.set_url()

    def get_wind_speed(self) -> float:
        data = self.get_responce()
        return data["wind"]["speed"]
    
    def get_country(self) -> str:
        data = self.get_responce()
        return data["sys"]["country"]
    
    def get_city(self) -> str:
        data = self.get_responce()
        return data["name"]
    
    def get_pressure(self) -> int:
        data = self.get_responce()
        return data["main"]["pressure"]