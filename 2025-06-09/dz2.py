#!/usr/bin/python3

from datetime import datetime, timedelta

# Классы Задания 1
class Number:  
    def __init__(self, x=0):
        self.x = x

    def __str__(self):  
        return str(self.x)

    def __add__(self, other):
        return self.x + other.x

    def __sub__(self, other):
        return self.x - other.x

    def __mul__(self, other):
        return self.x * other.x

    def __truediv__(self, other):
        return self.x / other.x

# Классы Задания 2
class Drob(Number):
    pass

# Классы Задания 3
class Biblioteka(Number):
    def __init__(self, name="", address="", x=0):
        self.name = name
        self.address = address
        self.x = x

    def __add__(self, other):
        self.x += other
        return self.x

    def __sub__(self, other):
        self.x -= other
        return self.x

    def __lt__(self, other):
        return self.x < other.x

    def __gt__(self, other):
        return self.x > other.x

    def __le__(self, other):
        return self.x <= other.x

    def __ge__(self, other):
        return self.x >= other.x

    def __eq__(self, other):
        return self.x == other.x

# Классы Задания 4
class Date:
    def __init__(self, day, month, year):
        self.data = datetime(year, month, day)

    def __str__(self):
        return self.data.strftime("%d.%m.%Y")

    def __sub__(self, other):
         return abs((self.data - other.data).days)

    def __add__(self, other):
        new_date = self.data + timedelta(days=other)
        return new_date.strftime("%d.%m.%Y")

def main():
    p1 = Number(10)
    p2 = Number(5)
    print(f"ЗАДАНИЕ1:\nЧисло 1: {p1}\nЧисло 2: {p2}\n\tСложение: {p1 + p2}\n\tВычитание: {p1 - p2}\n\tУмножение: {p1 * p2}\n\tДеление: {p1 / p2}")
    p1 = Drob(8)
    p2 = Drob(2)
    print(f"\nЗАДАНИЕ2:\nДробь 1: {p1}\nДробь 2: {p2}\n\tСложение: {p1 + p2}\n\tВычитание: {p1 - p2}\n\tУмножение: {p1 * p2}\n\tДеление: {p1 / p2}")
    p1 = Biblioteka("Пушкина", "г. Омск, ул. Ленина 5", 10000)
    p2= Biblioteka("Ленина", "г. Пермь, ул. Пушкина 10", 8000)
    print(f"\nЗАДАНИЕ3:\nКниг в бибилиотеке 1: {p1}\nКниг в библиотеке 2: {p2}\n\tДобавим 5 книг Библиотеке 1: {p1 + 5}\n\tУдалим 10 книг Библиотеки 2: {p2 - 10}")
    print(f"\tp1 < p2: {p1 < p2}\n\tp1 > p2: {p1 > p2}\n\tp1 <= p2: {p1 <= p2}\n\tp1 >= p2: {p1 >= p2}\n\tp1 == p2: {p1 == p2}\n\tp1 != p2: {p1 != p2}".replace("True", "Да").replace("False", "Нет"))
    p1 = Date(22, 3, 1980)
    p2 = Date(30, 6, 1982)
    print(f"\nЗАДАНИЕ 4:\nДата 1: {p1}\nДата 2: {p2}\n\tРазница в днях: {p1 - p2}\n\tДата 1 + 15 дней: {p1 + 15}")

if __name__ == "__main__": main()
