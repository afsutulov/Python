#!/usr/bin/python3

import json

class dz1:
    def __init__(self, name='страна', txt="столица"):
        self.data = {}
        self.name = name
        self.txt = txt

    def Num(self, txt, n1, n2): # Функция ввода и проверки цифры в заданном диапазоне
        _ = input(f'{txt}: ')
        if _.isnumeric() and n1 <= int(_) <= n2: return int(_)
        else: print(f'\u001b[31mОшибка ввода! Необходимо ввести число от {n1} до {n2}!\u001b[0m\n'); return self.Num(txt, n1, n2)

    def Menu(self):
        while True:
            match self.Num(f"Действие ({self.name} + {self.txt}):\n\t1. Добавить данные\n\t2. Удалить данные\n\t3. Поиск данных\n\t4. Редактировать данные\n\t5. Сохранить данные\n\t6. Загрузить данные\n\t7. Вывод данныъ\n\t0. Выход\nВаш выбор", 0, 7):
                case 0: break
                case 1: self.Add()
                case 2: self.Del()
                case 3: self.Search(input(f"Введите [{self.name}] для поиска: "))
                case 4: self.Edit(input(f"Введите [{self.name}] для редактирования: "))
                case 5: self.Save()
                case 6: self.Load()
                case 7: self.Print()

    def Add(self):
        _ = input(f"Введите [{self.name}]: ")
        self.data[_] = input(f"Введите [{self.txt}]: ")

    def Del(self):
        del self.data[input(f"Введите [{self.name}]: ")]

    def Search(self, txt):
        for _ in self.data:
            if _ == txt: print(f'{self.txt}: {self.data[_]}')

    def Edit(self, txt):
        self.data[txt] = input(f"Введите новую [{self.txt}]: ")

    def Save(self):
        with open("dz1.json", "w") as file: json.dump(self.data, file)
        print("Данные сохранены в файл: dz1.jspn!")

    def Load(self):
        with open("dz1.json", "r") as file: self.data = json.load(file)
        print("Данные Загружены их файла: dz1.jspn!")

    def Print(self):
        print(self.data)

if __name__ == "__main__":
    dz1().Menu()
    dz1("группа", "альбом").Menu()
