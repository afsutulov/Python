#!/usr/bin/python3

# Классы для Задания 1
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Челвек: {self.name} возраста {self.age}"

class Builder(Human):
    def __init__(self, name, age):
        Human.__init__(self, name, age)
        self.Stroit()

    def Stroit(self):
        print(f"Строитель {self.name} возраста {self.age} строит здания")

class Sailor(Human):
    def __init__(self, name, age):
        Human.__init__(self, name, age)
        self.Plivet()

    def Plivet(self):
        print(f"Моряк {self.name} возраста {self.age} плывет на корабле")

class Pilot(Human):
    def __init__(self, name, age):
        Human.__init__(self, name, age)
        self.Letit()

    def Letit(self):
        print(f"Пилотк {self.name} возраста {self.age} леитт на самолеет")

# Классы Задания 2
class Passport:
    def __init__(self, name, number, country):
        self.name = name
        self.number = number
        self.country = country

    def Vidacha(self):
        return f"Гражданину {self.country} с имененм {self.name} выдан паспорт с номером {self.number}"

class Zagran(Passport):
    def __init__(self, name, number, country, zag_number, visa=[]):
        Passport.__init__(self, name, number, country)
        self.zag_number = zag_number
        self.visa = visa

    def Vidacha(self):
        return f"Гражданину {self.country} с имененм {self.name}, паспорт с номером {self.number}, выда загранпаспорт с номером {self.zag_number}"

    def visaInfo(self):
        return f"Информация о визах стран в паспорте: {', '.join(self.visa)}"

    def addVisa(self, item):
        self.visa.append(item)
        return f"Добавлена виза в страну {item}\n{self.visaInfo()}"

    def removeVisa(self, item):
        self.visa.remove(item)
        return f"Удалена виза в страну {item}\n{self.visaInfo()}"

# Классы Задания 3
class Jivotnoe:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def main():
    print("ЗАДАНИЕ 1:")
    Builder("Петя", 44)
    Sailor("Вася", 50)
    Pilot("Григорий", 35)
    print("\nЗАДАНИЕ 2:")
    pasp = Passport("Иванов Иван Иванович", 123456, "Россия")
    print(pasp.Vidacha())
    zagr = Zagran("Петров Петр Петрович", 987654, "Беларусь", 223344)
    print(zagr.Vidacha())
    print(zagr.addVisa("Китай"))
    print(zagr.addVisa("Аргентина"))
    print(zagr.removeVisa("Китай"))
    print("\nЗАДАНИЕ 3:")

if __name__ == "__main__": main()
