import json


def loading_weather():
    with open("weather_data.json","r",encoding='utf8') as file:
        """Загружает данные с погодой"""
        data = json.load(file)
    return data



def check_file_cleared(filename: str) -> bool:
    """Проверяет что файл содержит пустые данные"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)

        if isinstance(data, dict):
            return len(data) == 0
        elif isinstance(data, list):
            return len(data) == 0
        else:
            return False

    except:
        return False