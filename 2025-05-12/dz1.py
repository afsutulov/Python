#!/usr/bin/python3

import random

# Функция ввода числа с проверкой
def Num(txt, n1, n2):
    _ = input(f'{txt}: ')
    if _.isnumeric() and n1 <= int(_) <=n2: return int(_)
    else: print(f'Ошибка ввода! Необходимо ввести число от {n1} до {n2}!\n'); return Num(txt, n1, n2)

def ObshiyKod(mass):
    match Num('\nВарианты:\n\t1 - отсортировать по возрастанию\n\t2 - отсортировать по убыванию\nВыберите дейстие', 1, 2):
       case 1: mass.sort()
       case 2: mass.sort(reverse=True)
    print(f'\nОтсортированный список: {mass}\n')
    _ = Num("Введите число для поиска", 0, 10)
    mass = [i for i, val in enumerate(mass) if val == _]
    print(f'Индексы совпадений: {mass}\n')

# Задание 1
print('ЗАДАНИЕ 1: Есть четыре списка целых. Необходимо их объединить в пятом списке. Полученный результат в зависимости от выбора пользователя отсортировать по убыванию или возрастанию. Найти значение, введенное пользователем, с использованием линейного поиска.\n\nРЕШЕНИЕ:')
mass = []
for _ in range(4):
    i = [random.randint(0, 10) for i in range(10)]
    print(f'Список\t{_ + 1}: {i}')
    mass += i
print(f'Объедиденный список: {mass}')
ObshiyKod(mass)

# Задание 2
print('\nЗАДАНИЕ 2: Есть четыре списка целых. Необходимо объединить в пятом списке только те элементы, которые уникальны для каждого списка. Полученный результат в зависимости от выбора пользователя отсортировать по убыванию или возрастанию. Найти значение, введенное пользователем\n\nРЕШЕНИЕ:')
mass = []
for _ in range(4):
    i = [random.randint(0, 10) for i in range(10)]
    print(f'Список\t{_ + 1}: {i}\tУникальные значения: {list(set(i))}')
    mass += list(set(i))
print(f'Объедиденный список с уникальными значениями: {mass}')
ObshiyKod(mass)
