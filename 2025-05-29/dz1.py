#!/usr/bin/python3

import random

def Num(txt, n1, n2):
    _ = input(f'{txt}: ')
    if _.isnumeric() and n1 <= int(_) <=n2: return int(_)
    else: print(f'Ошибка ввода! Необходимо ввести число от {n1} до {n2}!\n'); return Num(txt, n1, n2)

class Spravochnik:
    def __init__(self, code, phone):
        self.Flag = "СПРАВОЧНИК"
        self.code = code
        self.Code = "кодам"
        self.phone = phone
        self.Phone = "телефонам"

    def Menu(self):
        while True:
            match Num(f"ДЕЙСТВИЯ ({self.Flag}):\n\t1. Вывод списка\n\t2. Сортировка по {self.Code}\n\t3. Сортировка по {self.Phone}\n\t0. Выход\n\nВаше действие", 0, 3):
                case 1: self.Print()
                case 2: self.Sort(True)
                case 3: self.Sort(False)
                case 0: break

    def Print(self):
        print(f"{'-'*45}")
        if self.Flag == "СПРАВОЧНИК": print(f"| {'КОД':^30} | {'ТЕЛЕФОН':^8} |\n{'-'*45}")
        else: print(f"| {'КНИГА':^30} | {'ГОД':^8} |\n{'-'*45}")
        for _ in range(len(self.code)):
            print(f"| {self.code[_]:<30} |  {self.phone[_]:7} |")
        print(f"{'-'*45}\n")

    def Sort(self, flag):
        self.flag = flag
        for i in range(len(self.code)):
            for j in range(len(self.code)):
                if self.flag:
                    if self.code[i] < self.code[j]:
                        self.code[i], self.code[j] = self.code[j], self.code[i]
                        self.phone[i], self.phone[j] = self.phone[j], self.phone[i]
                else:
                    if self.phone[i] < self.phone[j]:
                        self.code[i], self.code[j] = self.code[j], self.code[i]
                        self.phone[i], self.phone[j] = self.phone[j], self.phone[i]

class Book(Spravochnik):
    def __init__(self, book, year):
        self.Flag = "КНИГИ"
        self.code = book
        self.Code = "названию книги"
        self.phone = year
        self.Phone = "году выхода"

def main():
    Spravochnik([random.randint(1000, 9999) for i in range(20)], [random.randint(100000, 999999) for i in range(20)]).Menu()
    Book(["Гарри Поттер", "Винни Пух", "Глюки в космосе", "Война и мир", "Как я писал эту шнягу", "Девушки нелегкого поведения"],[2002, 1975, 2018, 1890, 1917, 2000]).Menu()

if __name__ == "__main__": main()
