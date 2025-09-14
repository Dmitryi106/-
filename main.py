import json
from API import record_weather
from Classes_weather import Weather
from Loading import check_file_cleared, loading_weather


print("Добро пожаловать в погодное приложение!")
user_input = input("Хотите узнать погоду?(Да\Нет)\n")


def basic_actions():
    global user_input, loading_weather
    while user_input == "да":
            # Получаем город от пользователя
        city = input("Выберите город в котором хотите узнать погоду:\n").strip()
        record_weather(city)
        loading_weather = loading_weather()
        weather_city = Weather(city,loading_weather['coord'],loading_weather['weather'],loading_weather['main'],loading_weather['wind'],loading_weather['sys'])
        print(weather_city)
        with open('weather_data.json', 'w') as f:
            json.dump({}, f)
        check_file_cleared("weather_data.json")
        user_input = input("Хотите узнать погоду ещё одного города?(Да/Нет)")
    if user_input == "нет":
        print('Завершение программы')
    else:
        print("Некорректный ввод")
if __name__ == "__main__":
    basic_actions()