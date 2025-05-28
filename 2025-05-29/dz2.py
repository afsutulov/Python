#!/usr/bin/python3

def Num(txt, n1, n2):
    _ = input(f'{txt}: ')
    if _.isnumeric() and n1 <= int(_) <=n2: return int(_)
    else: print(f'Ошибка ввода! Необходимо ввести число от {n1} до {n2}!\n'); return Num(txt, n1, n2)

class People:
    def __init__(self, fio, date, phone, city, country, address):
        self.Flag = "ЧЕЛОВЕК"
        self.p1 = fio
        self.P1 = "ФИО"
        self.p2 = date
        self.P2 = "Дата рождения"
        self.p3 = phone
        self.P3 = "Телефон"
        self.p4 = city
        self.P4 = "Город"
        self.p5 = country
        self.P5 = "Страна"
        self.p6 = address
        self.P6 = "Адрес"

    def Menu(self):
        while True:
            match Num(f"ДЕЙСТВИЯ ({self.Flag}):\n\t1. Вывод данных\n\t2. Ввод данных\n\t3. Изменить данные\n\t0. Выход\n\nВаше действие", 0, 3):
                case 1: self.Print()
                case 2: self.Input()
                case 3: self.Change()
                case 0: break

    def Print(self):
        print(f"ДАННЫЕ ({self.Flag}):\n\t{self.P1}: {self.p1}\n\t{self.P2}: {self.p2}\n\t{self.P3}: {self.p3}\n\t{self.P4}: {self.p4}\n\t{self.P5}: {self.p5}\n\t{self.P6}: {self.p6}\n")

    def Input(self):
        self.p1 = input(f"Введите {self.P1}: ")
        self.p2 = input(f"Введите {self.P2}: ")
        self.p3 = input(f"Введите {self.P3}: ")
        self.p4 = input(f"Введите {self.P4}: ")
        self.p5 = input(f"Введите {self.P5}: ")
        self.p6 = input(f"Введите {self.P6}: ")

    def Change(self):
        print(f"ЧТО ИЗМЕНИТЬ {self.Flag}:\n\t1. {self.P1}\n\t2. {self.P2}\n\t3. {self.P3}\n\t4. {self.P4}\n\t5. {self.P5}\n\t6. {self.P6}\n\t0. Без изменений")
        match Num(f"\n\nВаше действие", 0, 6):
            case 1: self.p1 = input(f"Введите {self.P1}: ")
            case 2: self.p2 = input(f"Введите {self.P2}: ")
            case 3: self.p3 = input(f"Введите {self.P3}: ")
            case 4: self.p4 = input(f"Введите {self.P4}: ")
            case 5: self.p5 = input(f"Введите {self.P5}: ")
            case 6: self.p6 = input(f"Введите {self.P6}: ")

class City(People):
    def __init__(self, name, region, country, peoples, inx, code):
        self.Flag = "ГОРОД"
        self.p1 = name
        self.P1 = "Название города"
        self.p2 = region
        self.P2 = "Название региона"
        self.p3 = country
        self.P3 = "Название страны"
        self.p4 = peoples
        self.P4 = "Количество жителей"
        self.p5 = inx
        self.P5 = "Индекс"
        self.p6 = code
        self.P6 = "Телефонный код"

class Country(People):
    def __init__(self, country, continent, peoples, code, capitals, cityes):
        self.Flag = "СТРАНА"
        self.p1 = country
        self.P1 = "Название страны"
        self.p2 = continent
        self.P2 = "Название континента"
        self.p3 = peoples
        self.P3 = "Количество жителей"
        self.p4 = peoples
        self.P4 = "Телефонный код"
        self.p5 = capitals
        self.P5 = "Столица"
        self.p6 = cityes
        self.P6 = "Перечень городов"

class Drob:
    def __init__(self, chis, znam):
        self.chis = chis
        self.znam = znam

    def Menu(self):
        while True:
            match Num(f"ДЕЙСТВИЯ (ДРОБЬ):\n\t1. Вывод данных\n\t2. Ввод данных\n\t3. Изменить данные\n\t4. Сложить\n\t5. Вычесть\n\t6. Умножить\n\t7. Разделить\n\t0. Выход\n\nВаше действие", 0, 7):
                case 1: self.Print()
                case 2: self.Input()
                case 3: self.Change()
                case 4: self.Arif(0)
                case 5: self.Arif(1)
                case 6: self.Arif(2)
                case 7: self.Arif(3)
                case 0: break

    def Print(self):
        print(f"Числитель: {self.chis}\nЗнаменатель: {self.znam}\n")

    def Input(self):
        self.chis = Num("Введите числитель (1-10000)", 1, 10000)
        self.znam = Num("Введите знаменатель (1-10000)", 1, 10000)

    def Change(self):
        match Num(f"Что изменить:\n\t1. Числитель\n\t2. Знаменатель\n\t0. Без изменений\nВаш выбор", 0, 2):
            case 1: self.chis = Num("Введите числитель (1-10000)", 1, 10000)
            case 2: self.znam = Num("Введите знаменатель (1-10000)", 1, 10000)
    def Arif(self, x):
        match x:
            case 0: print(f"Результат сложения: {self.chis + self.znam}\n")
            case 1: print(f"Результат вычитания: {self.chis - self.znam}\n")
            case 2: print(f"Результат умножения: {self.chis * self.znam}\n")
            case 3: print(f"Результат деления: {self.chis / self.znam}\n")

def main():
    People("Иванов Иван Иванович", "01.04.1982", "88002000600", "Красноярск", "Россия", "ул. Леина, 1").Menu()
    City("Петропавловск", "Северо-Казахстанская область", "Казахстан", "250000", "150000", "+7-7152").Menu()
    Country("Россия", "Евразия", "143000000", "+7", "Москва", "Питер, Екатеринбург, Новосибирск").Menu()
    Drob(10, 100).Menu()

if __name__ == '__main__': main()
