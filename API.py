import json
import requests


API_KEY = "593aee73708a143796cedf4f9d4f1c80"

def record_weather(city):
    """Функция обращается по API к сайту Openweathermap и если возникает ошибка, предупреждает о ней """
    url_get_HH = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=ru"
    response = requests.get(url_get_HH)
    if response.status_code == 404:
        print("404\n*** Запрашиваемый ресурс не найден на сервере.Введите другой город ***")
    elif response.status_code == 401:
        print("401\n*** Требуется аутентификация пользователя ***")
    elif response.status_code == 400:
        print("400\n*** неверный синтаксис запроса или невалидные параметры ***")
    elif response.status_code == 429:
        print("429\n*** Cлишком много запросов (защита от DDoS) ***")
    else:
        weather = response.json()
        with open("weather_data.json",'w') as file_weather:
            json.dump(weather, file_weather,indent=4)

