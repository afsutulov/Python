#!/usr/bin/python3

import math

# Классы Задания 1
class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

    def perimeter(self):
        return 4 * self.side_length

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

class Zad1(Square, Circle):
    def __init__(self, side_length):
        Square.__init__(self, side_length)
        Circle.__init__(self, side_length / 2)

    def __str__(self):
        return f"\tРазмер стороны квадрата: {self.side_length}\n\tРадиус окружности: {self.radius}\n\tПлощадь квадрата: {Square.area(self)}\n\tПлощадь круга: {Circle.area(self)}\n\tПериметр квадрата: {self.perimeter()}\n\tДлинна окружности: {self.circumference()}"

# Классы Задания 2
class Kolesa:
    def __init__(self, razm_koles):
        self.razm_koles = razm_koles

    def __str__(self):
        return f"Размер колес: {self.razm_koles}\""

class Dvigatel:
    def __init__(self, dvigatel):
        self.dvigatel = dvigatel

    def __str__(self):
        return f"Объем двигателя: {self.dvigatel}"

class Dveri:
    def __init__(self, dvery):
        self.dvery = dvery

    def __str__(self):
        return f"Количество дверей: {self.dvery}"

class Auto(Kolesa, Dvigatel, Dveri):
    def __init__(self, marka, razm_koles, dvigatel, dvery):
        self.marka = marka
        Kolesa.__init__(self, razm_koles)
        Dvigatel.__init__(self, dvigatel)
        Dveri.__init__(self, dvery)

    def __str__(self):
        return f"Марка автомобиля: {self.marka}\n{Kolesa(self.razm_koles)}\n{Dvigatel(self.dvigatel)}\n{Dveri(self.dvery)}"

# Классы Задания 3
class Animal:
    def __init__(self, name):
        self.name = name

    def Sound(self):
        return "Делаю звуки животного"

    def Show(self):
        return f"Имя животного: {self.name}"

    def Type(self):
        return "Тип животного: Домашнее"

    def __str__(self):
        return f"\t{self.Show()}\n\t{self.Type()}\n\t{self.Sound()}"

class Cat(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)

    def Sound(self):
        return "Звук животного: Мяууу\n"

class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)

    def Sound(self):
        return "Звук животного: Гав-Гав\n"

class Popugay(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)

    def Sound(self):
        return "Звук животного: Чирик-Чирик\n"

class Homyak(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)

    def Sound(self):
        return "Звук животного: фыр-фыр\n"

# Классы задания 4
class Employer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Print(self):
        print("\tThis is Emoployer class\n")

    # Задание 5
    def __str__(self):
        return f"Имя: {self.name}"

    def __int__(self):
        return self.age

class President(Employer):
    def Print(self):
        print(f"\tИмя: {self.name}\n\tДолжность: Президент\n\tВозраст: {self.age}\n")

class Manager(Employer):
    def Print(self):
        print(f"\tИмя: {self.name}\n\tДолжность: Менеджер\n\tВозраст: {self.age}\n")

class Worker(Employer):
    def Print(self):
        print(f"\tИмя: {self.name}\n\tДолжность: Рабочий\n\tВозраст: {self.age}\n")

def main():
    print(f"ЗАДАНИЕ 1:\n{Zad1(5)}\n")
    print(f"ЗАДАНИЕ 2:\n{Auto('Lada', 15, 1.6, 5)}\n")
    print(f"ЗАДАНИЕ 3:\n{Cat('Мурка')}\n{Dog('Тузик')}\n{Popugay('Кеша')}\n{Homyak('Пыха')}")
    print("ЗАДАНИЕ 4:")
    Employer("Василий", 18).Print()
    president = President("Иван Иванович", 50)
    president.Print()
    Manager("Владислав", 22).Print()
    Worker("Петрович", 47).Print()
    print("ЗАДАНИЕ 5:")
    print(f"\t{president}\n\tВозраст: {int(president)}")

if __name__ == "__main__": main()
