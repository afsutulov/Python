#!/usr/bin/python3

#class RealString:
#    def __init__(self, a="", b=""):
#        self.a = a
#        self.b = b

#    def __str__(self):
#        if len(self.a) > len (self.b): return self.a
#        else: return self.b

#    def __lt__(self, other):
#        if len(self.a) > len(other.a): return self.a
#        else: return other.a

import random

class Pyat:
    def __init__(self):
        self.pole = []
        for i in range(16):
            while True:
                _ = random.randint(0, 15)
                if not _ in self.pole: self.pole.append(_); break

    def Num(self, txt, n1, n2):
        self.txt = txt
        self.n1 = n1
        self.n2 = n2
        _ = input(f'{self.txt}: ')
        if _.isnumeric() and self.n1 <= int(_) <= self.n2: return int(_)
        else: print(f'\u001b[31mОшибка ввода! Необходимо ввести число от {n1} до {n2}!\u001b[0m\n'); return self.Num(txt, n1, n2)

    def Print(self):
        print(f"\033[H\033[2JИГРА ПЯТНАШКИ!\n\n{'-'*21}")
        for i in range(4):
            for y in range(4):
                if self.pole[i*4+y] != 0: print(f"|{self.pole[i*4+y]:^4}", end="")
                else: print(f"|\033[47m\033[30m{' ':^4}\033[0m", end="")
            print(f"|\n{'-'*21}")

    def Error(self):
        print("\u001b[31mНеправильный ход\u001b[0m")
        _ = input("\nНажмите Enter")

    def Hod(self, x):
        y = self.pole.index(0)
        match x:
            case 1:
                if y - 4 >= 0: self.pole[y-4], self.pole[y] = self.pole[y], self.pole[y-4]
                else: self.Error()
            case 2:
                if y + 4 < len(self.pole): self.pole[y+4], self.pole[y] = self.pole[y], self.pole[y+4]
                else: self.Error()
            case 3:
                if y + 1 < len(self.pole) and ((y + 1) % 4 != 0): self.pole[y+1], self.pole[y] = self.pole[y], self.pole[y+1]
                else: self.Error()
            case 4:
                if y - 1 > 0 and (y % 4 != 0): self.pole[y-1], self.pole[y] = self.pole[y], self.pole[y-1]
                else: self.Error()
        y = self.pole.copy()
        y.remove(0)
        if y == sorted(y): self.Print(); print("Вы победили!"); exit()

    def Menu(self):
        while True:
            self.Print()
            _ = self.Num("\nДействия:\n\t1. Ход вверх\n\t2. Ход вниз\n\t3. Ход влево\n\t4. Ход влево\n\t0. Завершение игры\nВаш выбор", 0, 4)
            if _ == 0: break
            else: self.Hod(_)

def main():
#    print(RealString("Яблоко", "Apple"))
#    x = RealString("Яблоко")
#    y = RealString("Apple")
#    print(x < y)

    y = Pyat()
    y.Menu()

if __name__ == "__main__": main()
