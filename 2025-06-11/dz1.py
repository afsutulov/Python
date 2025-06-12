#!/usr/bin/python3

import random

# Добавил возможность задать размер поря (переменная self.dln). По умолчанию поставил 5
# Добавил выделение цветом пустой позиции через ANSI. Плюс очистку экрана. Не уверен, что PyCham отразит правильно.
# Управление кнопками не стал добавлять - в Win и Lin реализуется через разные модули. Получается конкретный гемморой.
# Алгоритм автоматической игры реализуется с помощью алгоритма А* и эвристики Манхэттена

class Pyatak:
    def __init__(self):
        self.dln = 5   # Задаем размер поля
        self.pole = []
        for i in range(self.dln * self.dln): # Заполняем поле
            while True:
                _ = random.randint(0, self.dln * self.dln - 1)
                if not _ in self.pole: self.pole.append(_); break

    def num(self, txt, n1, n2): # Функция ввода и проверки цифры в заданном диапазоне
        _ = input(f'{txt}: ')
        if _.isnumeric() and n1 <= int(_) <= n2: return int(_)
        else: print(f'\u001b[31mОшибка ввода! Необходимо ввести число от {n1} до {n2}!\u001b[0m\n'); return self.num(txt, n1, n2)

    def print_board(self): # Печатаем игровое поле. Оно масштабируется в зависимости от размера поля
        print(f"\033[H\033[2JИГРА ПЯТНАШКИ!\n\n{'-'*(5 * self.dln + 1)}")
        for i in range(self.dln):
            for y in range(self.dln):
                if self.pole[i * self.dln + y] != 0: print(f"|{self.pole[i * self.dln + y]:^4}", end = "")
                else: print(f"|\033[47m\033[30m{' ':^4}\033[0m", end = "")
            print(f"|\n{'-'*(5 * self.dln + 1)}")

    def is_solved(self): # Проверка победы по сравнению поля с отсортированным
        y = self.pole.copy()
        y.remove(0)
        if y == sorted(y): self.print_board(); print("\033[32mВЫ ПОБЕДИЛИ!!\033[0m"); exit()

    def move(self, x): # Функция хода
        y = self.pole.index(0) # Определяем позицию пустой клетки
        match x:
            case 1:
                if y - self.dln >= 0: self.pole[y - self.dln], self.pole[y] = self.pole[y], self.pole[y - self.dln]
            case 2:
                if y + self.dln < len(self.pole): self.pole[y + self.dln], self.pole[y] = self.pole[y], self.pole[y + self.dln]
            case 3:
                if y - 1 >= 0 and (y % self.dln != 0): self.pole[y - 1], self.pole[y] = self.pole[y], self.pole[y - 1]
            case 4:
                if y + 1 < len(self.pole) and ((y + 1) % self.dln != 0): self.pole[y + 1], self.pole[y] = self.pole[y], self.pole[y + 1]
        self.is_solved()

    def play_game(self): # Функция игры
        while True:
            self.print_board()
            _ = self.num("\nПоменять местами пустую клетку с позицией:\n\t1. Сверху\n\t2. Снизу\n\t3. Слева\n\t4. Справа\n\t0. Завершение игры\nВаш выбор", 0, 4)
            if _ == 0: break
            self.move(_)

if __name__ == "__main__": Pyatak().play_game()