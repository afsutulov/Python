#!/usr/bin/python3

import pickle, json

class Samolet:
    def __init__(self):
        self.data = {}

    def num(self, txt, n1, n2):
        _ = input(f'{txt}: ')
        if _.isnumeric() and n1 <= int(_) <=n2: return int(_)
        else: print(f'Ошибка ввода! Необходимо ввести число от {n1} до {n2}!\n'); return self.num(txt, n1, n2)

    def Menu(self):
        while True:
            match self.num("Действия:\n\t1. Вывод данных\n\t2. Добавить данные\n\t3. Удалить данные\n\t4. Изменить данные\n\t5. Сохранить данные pickle\n\t6. Загрузить данные pickle\n\t7. Сохранить данные JSON\n\t8. Загрузить данные JSON\n\t0. Выход\nВаш выбор", 0, 8):
                case 0: break
                case 1: self.Print()
                case 2: self.Add()
                case 3: self.Del()
                case 4: self.Edit()
                case 5: self.Save(True, "dz1.pickle", self.data)
                case 6: self.data = self.Load(True, "dz1.pickle")
                case 7: self.Save(False, "dz1.json", self.data)
                case 8: self.data = self.Load(False, "dz1.json")

    def Print(self):
        print(f"Данные: {self.data}")

    def Add(self):
        x1 = input("Вdедите название: ")
        x2 = input("Вdедите модель: ")
        x3 = input("Вdедите серийный номер: ")
        self.data = {"name": x1, "model": x2, "serial": x3}

    def Del(self):
        self.data = {}

    def Edit(self):
        match self.num("Что редактируем:\n\t1. Название\n\t2. Модель\n\t3. Сериный номер\n\t0. Выход без изменений\nВаш выбор", 0, 3):
            case 1: self.data["name"] = input("Введите новое название: ")
            case 2: self.data["model"] = input("Введите новую модель: ")
            case 3: self.data["serial"] = input("Введите новый серийный номер: ")

    def Save(self, Flag, txt, data):
        if Flag:
            with open(txt, 'wb') as f: pickle.dump(data, f)
            print(f"Данные сохранены в файл: {txt}")
        else:
            with open(txt, "w") as f: json.dump(data, f)
            print(f"Данные сохранены в файл: {txt}!")

    def Load(self, Flag, txt):
        if Flag:
            with open(txt, 'rb') as f: data = pickle.load(f)
            print(f"Данные загружены из файла: {txt}")
        else:
            with open(txt, "r") as f: data = json.load(f)
            print(f"Данные Загружены их файла: {txt}!")
        return data

class Drob:
    def __init__(self, chis=1, znam=1):
        self.chis = chis
        self.znam = znam

    def Menu(self):
        while True:
            match Samolet().num(f"ДЕЙСТВИЯ (ДРОБЬ):\n\t1. Вывод данных\n\t2. Ввод данных\n\t3. Изменить данные\n\t4. Сложить\n\t5. Вычесть\n\t6. Умножить\n\t7. Разделить\n\t8. Сохранить данные pickle\n\t9. Загрузить данные pickle\n\t10. Сохранить данные JSON\n\t11. Загрузить данные JSON\n\t0. Выход\nВаше действие", 0, 11):
                case 1: self.Print()
                case 2: self.Input()
                case 3: self.Change()
                case 4: self.Arif(0)
                case 5: self.Arif(1)
                case 6: self.Arif(2)
                case 7: self.Arif(3)
                case 8: x = {"chis": self.chis, "znam": self.znam}; Samolet().Save(True, "dz22.pickle", x)
                case 9: x = Samolet().Load(True, "dz22.pickle"); self.chis = x["chis"]; self.znam = x["znam"]
                case 10: x = {"chis": self.chis, "znam": self.znam}; Samolet().Save(False, "dz22.json", x)
                case 11: x  = Samolet().Load(False, "dz22.json"); self.chis = x["chis"]; self.znam = x["znam"]
                case 0: break

    def Print(self):
        print(f"Числитель: {self.chis}\nЗнаменатель: {self.znam}\n")

    def Input(self):
        self.chis = Samolet().num("Введите числитель (1-10000)", 1, 10000)
        self.znam = Samolet().num("Введите знаменатель (1-10000)", 1, 10000)

    def Change(self):
        match Samolet().num(f"Что изменить:\n\t1. Числитель\n\t2. Знаменатель\n\t0. Без изменений\nВаш выбор", 0, 2):
            case 1: self.chis = Samolet().num("Введите числитель (1-10000)", 1, 10000)
            case 2: self.znam = Samolet().num("Введите знаменатель (1-10000)", 1, 10000)

    def Arif(self, x):
        match x:
            case 0: print(f"Результат сложения: {self.chis + self.znam}\n")
            case 1: print(f"Результат вычитания: {self.chis - self.znam}\n")
            case 2: print(f"Результат умножения: {self.chis * self.znam}\n")
            case 3: print(f"Результат деления: {self.chis / self.znam}\n")

class Chas:
    def __init__(self, chas=0, minut=0):
        self.data = {"chas": chas, "minut": minut}

    def Menu(self):
        while True:
            match Samolet().num("Действие:\n\t1. Вывод данных\n\t2. Ввести данные\n\t3. Сохранить данные в pickle\n\t4. Загрузить данные в pickle\n\t5. Сохранить данные в JSON\n\t6. Загрузить данные из JSON\n\t0. Выход\nВаше днйствие", 0, 6):
                case 1: self.Print()
                case 2: self.Add()
                case 3: Samolet().Save(True, "dz13.pickle", self.data)
                case 4: self.data = Samolet().Load(True, "dz13.pickle")
                case 5: Samolet().Save(False, "dz13.json", self.data)
                case 6: self.data = Samolet().Load(False, "dz13.json")
                case 0: break

    def Print(self):
        print(f'Часов: {self.data["chas"]}\t Минут: {self.data["minut"]}')

    def Add(self):
        x1 = Samolet().num("Введите часы", 0, 24)
        x2 = Samolet().num("Введите минуты", 0, 60)
        self.data["chas"] = x1
        self.data["minut"] = x2

if __name__ == "__main__":
    Samolet().Menu()
    Drob().Menu()
    Chas().Menu()