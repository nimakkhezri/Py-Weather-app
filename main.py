from Weather import Weather

while True :
    print("\t\t---------- WEATHER APP ----------")
    city = input("Please enter your city (\"exit\" for close): ")
    if city.lower() == "exit" :
        break
    api = Weather(city)
    print("\t\tCountry: ", api.get_country())
    print("\t\tCity: ", api.get_city())
    print("\t\tDescription: ", api.get_description())
    print("\t\tTemp: ", api.get_celsius_temp(), " Celsius")
    print("\t\tmin temp: ", api.get_min_celsius_temp(), "Celsius")
    print("\t\tMax temp: ", api.get_max_celsius_temp(), "Celsius")
    print("\t\tWind speed: ", api.get_wind_speed())
    print("\t\tPressure: ", api.get_pressure())
    print("\t\t---------- WEATHER APP ----------")