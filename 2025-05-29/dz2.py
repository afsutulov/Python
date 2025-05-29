#!/usr/bin/python3

def Num(txt, n1, n2):
    _ = input(f'{txt}: ')
    if _.isnumeric() and n1 <= int(_) <=n2: return int(_)
    else: print(f'Ошибка ввода! Необходимо ввести число от {n1} до {n2}!\n'); return Num(txt, n1, n2)

class People:
    def __init__(self, data):
        self.Flag = "ЧЕЛОВЕК"
        self.p = data
        self.P = []
        self.P.append("ФИО")
        self.P.append("Дата рождения")
        self.P.append("Телефон")
        self.P.append("Город")
        self.P.append("Страна")
        self.P.append("Адрес")

    def Menu(self):
        while True:
            match Num(f"ДЕЙСТВИЯ ({self.Flag}):\n\t1. Вывод данных\n\t2. Ввод данных\n\t3. Изменить данные\n\t0. Выход\n\nВаше действие", 0, 3):
                case 1: self.Print()
                case 2: self.Input()
                case 3: self.Change()
                case 0: break

    def Print(self):
        print(f"ДАННЫЕ ({self.Flag}):")
        for _ in range(len(self.p)): print(f"\t{self.P[_]}: {self.p[_]}")
        print()

    def Input(self):
        for _ in range(len(self.p)): self.p[_] = input(f"Введите {self.P[_]}: ")

    def Change(self):
        print(f"ЧТО ИЗМЕНИТЬ {self.Flag}:\n\t")
        for _ in range(len(self.p)): print(f"\t{_+1}. {self.P[_]}")
        print("\t0. Без изменений")
        _ = Num("\n\nВаше действие", 0, len(self.p))
        if _ != 0: self.p[_-1] = input(f"Введите {self.P[_-1]}: ")

class City(People):
    def __init__(self, data):
        self.Flag = "ГОРОД"
        self.p = data
        self.P = []
        self.P.append("Название города")
        self.P.append("Название региона")
        self.P.append("Название страны")
        self.P.append("Количество жителей")
        self.P.append("Индекс")
        self.P.append("Телефонный код")

class Country(People):
    def __init__(self, data):
        self.Flag = "СТРАНА"
        self.p = data
        self.P = []
        self.P.append("Название страны")
        self.P.append("Название континента")
        self.P.append("Количество жителей")
        self.P.append("Телефонный код")
        self.P.append("Столица")
        self.P.append("Перечень городов")

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
    People(["Иванов Иван Иванович", "01.04.1982", "88002000600", "Красноярск", "Россия", "ул. Леина, 1"]).Menu()
    City(["Петропавловск", "Северо-Казахстанская область", "Казахстан", "250000", "150000", "+7-7152"]).Menu()
    Country(["Россия", "Евразия", "143000000", "+7", "Москва", "Питер, Екатеринбург, Новосибирск"]).Menu()
    Drob(10, 100).Menu()

if __name__ == '__main__': main()
