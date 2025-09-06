import json

def loading_weather():
    with open("weather_data.json","r",encoding='utf8') as file:
        """Загружает данные с погодой"""
        data = json.load(file)
    return data
loading_weather = loading_weather()


