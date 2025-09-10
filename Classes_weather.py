import datetime


class Weather():
    """Класс с общими данными погоды для определённого города"""
    def __init__(self,city, coord, weather, main, winds, sys):
        self.city = city
        self.coord = coord
        self.weather = weather
        self.main = main
        self.winds = winds
        self.sys = sys

    def __str__(self):
        return (
            f"Погода для города {self.city}\n{(self.weather[0]['description']).upper()}"
            f"\nТемпература воздуха: {self.main['temp']}"
            f"\nОщущается как: {self.main['feels_like']}"
            f"\nСкорость ветра: {self.winds['speed']} м/с"
            f"\nВосход: {datetime.datetime.fromtimestamp(self.sys['sunrise'])}"
            f"\nЗакат: {datetime.datetime.fromtimestamp(self.sys["sunset"])}"
            f"\nКоординаты\nДолгота: {self.coord['lon']}, \nШирота: {self.coord['lat']}"
        )