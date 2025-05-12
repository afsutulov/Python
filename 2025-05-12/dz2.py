#!/usr/bin/python3

import random

# Функция ввода числа с проверкой
def Num(txt, n1, n2):
    _ = input(f'{txt}: ')
    if _.isnumeric() and n1 <= int(_) <=n2: return int(_)
    else: print(f'Ошибка ввода! Необходимо ввести число от {n1} до {n2}!\n'); return Num(txt, n1, n2)

# Задание 1
print('ЗАДАНИЕ 1: Есть список из 10 элементов, заполненный случайными числами. Необходимо найти число, введенное пользователем. Используйте алгоритм линейного поиска.\n\nРЕШЕНИЕ:')
mass = [random.randint(0, 10) for i in range(10)]
print(f'Список: {mass}')
_ = Num("Введите число для поиска", 0, 10)
mass = [i for i, val in enumerate(mass) if val == _]
print(f'Индексы совпадений: {mass}\n')

# Задание 2
print('\nЗАДАНИЕ 2: Есть список из 10 элементов, заполненный случайными числами. Необходимо найти число, введенное пользователем. Используйте алгоритм линейного поиска.\n\nРЕШЕНИЕ:')
mass = [random.randint(0, 10) for i in range(10)]
print(f'Список: {mass}')
_ = Num("Введите число для поиска", 0, 10)
mass = [i for i, val in enumerate(mass) if val == _]
print(f'Индексы совпадений: {mass}\n')
