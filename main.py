import datetime
from API import record_weather
from Classes_weather import Weather
from Loading import loading_weather

"""Тут корень программы"""
city = input("Выберите город в котором хотите узнать погоду\n")
record_weather(city)

weather_city = Weather(loading_weather['coord'],loading_weather['weather'],loading_weather['main'],loading_weather['wind'],loading_weather['sys'])
#print(f"Погода для города {city}\n{(weather_city.weather[0]['description']).upper()}"
 #     f"\nТемпература воздуха: {weather_city.main['temp']}"
 #     f"\nОщущается как: {weather_city.main['feels_like']}"
  #    f"\nСкорость ветра: {weather_city.wind['speed']} м/с"
   #   f"\nВосход: {datetime.datetime.fromtimestamp(weather_city.sys['sunrise'])}"
    #  f"\nЗакат: {datetime.datetime.fromtimestamp(weather_city.sys["sunset"])}"
     # f"\nКоординаты\nДолгота: {weather_city.coord['lon']}, \nШирота: {weather_city.coord['lat']}")
print(weather_city)