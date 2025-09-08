from API import record_weather
from Classes_weather import Weather
from Loading import loading_weather


"""Тут корень программы"""
city = input("Выберите город в котором хотите узнать погоду\n")
record_weather(city)
loading_weather = loading_weather()

weather_city = Weather(loading_weather['coord'],loading_weather['weather'],loading_weather['main'],loading_weather['wind'],loading_weather['sys'])

print(weather_city)