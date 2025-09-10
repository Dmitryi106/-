import json

from API import record_weather
from Classes_weather import Weather
from Loading import loading_weather, check_file_cleared

user_input = input("Хотите узнать погоду?(Да\Нет)\n")
while user_input != "Нет":
    """Тут корень программы"""
    city = input("Выберите город в котором хотите узнать погоду\n")
    record_weather(city)
    loading_weather = loading_weather()
    weather_city = Weather(city,loading_weather['coord'],loading_weather['weather'],loading_weather['main'],loading_weather['wind'],loading_weather['sys'])
    print(weather_city)
    user_input = input("Хотите узнать погоду ещё одного города?(Да/Нет)")
    if user_input == "Нет":
        with open('weather_data.json', 'w') as f:
            json.dump({}, f)
        check_file_cleared("weather_data.json")
        print("Завершение работы программы!")
        # Проверка
        if check_file_cleared("weather_data.json"):
            print("Файл успешно очищен")
        else:
            print("Файл не очищен или содержит данные")
    else:
        print("Некорректный ввод!!!")
        break
