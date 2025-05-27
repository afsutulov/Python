#!/usr/bin/python3

def Num(txt, n1, n2):
    _ = input(f'{txt}: ')
    if _.isnumeric() and n1 <= int(_) <=n2: return int(_)
    else: print(f'Ошибка ввода! Необходимо ввести число от {n1} до {n2}!\n'); return Num(txt, n1, n2)

class Auto:
    def __init__(self, name, year, manufac, volume, color, price):
        self.Flag = 1
        self.name = name
        self.Name = "Название автомобиля"
        self.year = year
        self.Year = "Год выпуска"
        self.manufac = manufac
        self.Manufac = "Производитель"
        self.volume = volume
        self.Volume = "Обхем двигателя"
        self.color = color
        self.Color = "Цвет"
        self.price = price
        self.Price = "Цена"

    def Menu(self):
        while True:
            match Num("ДЕЙСТВИЯ:\n\t1. Вывод данных\n\t2. Ввод данных\n\t3. Изменить данные\n\t0. Выход\n\nВаше действие", 0, 3):
                case 1: self.Print()
                case 2: self.Input()
                case 3: self.Change()
                case 0: break

    def Print(self):
        print(f"ДАННЫЕ:\n\t{self.Name}: {self.name}\n\t{self.Year}: {self.year}\n\t{self.Manufac}: {self.manufac}\n\t{self.Volume}: {self.volume}\n\t{self.Color}: {self.color}")
        if self.Flag != 0: print(f"\t{self.Price}: {self.price}\n")
        else: print("\n")

    def Input(self):
        self.name = input(f"Введите {self.Name}: ")
        self.year = Num(f"Введите {self.Year}", 1900, 2025)
        self.manufac = input(f"Введите {self.Manufac}: ")
        self.volume = input(f"Введите {self.Volume}: ")
        self.color = input(f"Введите {self.Color}: ")
        if self.Flag != 1: self.price = Num(f"Введите {self.Price}", 0, 10000000)

    def Change(self):
        print(f"ЧТО ИЗМЕНИТЬ:\n\t1. {self.Name}\n\t2. {self.Year}\n\t3. {self.Manufac}\n\t4. {self.Volume}\n\t5. {self.Color}", end = "")
        if self.Flag != 0: print(f"\n\t6. {self.Price}", end = "")
        match Num(f"\n\t0. Без изменений\n\nВаше действие", 0, 6):
            case 1: self.name = input(f"Введите {self.Name}: ")
            case 2: self.year = Num(f"Введите {self.Year}", 1900, 2025)
            case 3: self.manufac = input(f"Введите {self.Manufac}: ")
            case 4: self.volume = input(f"Введите {self.Volume}: ")
            case 5: self.color = input(f"Введите {self.Color}: ")
            case 6:
                if self.Flag != 0: self.price = Num(f"Введите {self.Price}", 0, 10000000)

class Book(Auto):
    def __init__(self, name, year, manufac, janr, autor, price):
        self.Flag = 1
        self.name = name
        self.Name = "Название книги"
        self.year = year
        self.Year = "Год выпуска"
        self.manufac = janr
        self.Manufac = "Автор"
        self.volume = janr
        self.Volume = "Жанр"
        self.color = autor
        self.Color = "Автор"
        self.price = price
        self.Price = "Цена"

class Stadion(Auto):
    def __init__(self, name, year, country, city, peoples):
        self.Flag = 0
        self.name = name
        self.Name = "Название стадиона"
        self.year = year
        self.Year = "Год открытия"
        self.manufac = country
        self.Manufac = "Страна"
        self.volume = city
        self.Volume = "Город"
        self.color = peoples
        self.Color = "Вместимость"

def main():
    Auto("Honda CRV", 2008, "Honda", "2.5", "Blaсk", 2750000).Menu()
    Book("Гарри Поттер", 2012, "Дисней Ленд", "Приключения", "Какая-то баба", 100).Menu()
    Stadion("Лужники", 1975, "Россия", "Москва", "20000").Menu()

if __name__ == '__main__': main()
