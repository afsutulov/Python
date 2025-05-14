#!/usr/bin/python3

import random

x = (tuple(random.randint(0, 10) for i in range(20)),
    tuple(random.randint(0, 10) for i in range(20)),
    tuple(random.randint(0, 10) for i in range(20)))

print('НАЧАЛЬНЫЕ ДАННЫЕ:')
for _ in range(len(x)):
    print(f'Кортеж {_ + 1}: {x[_]}')


# Задание 1
print('\nЗАДАНИЕ 1: Есть три кортежа целых чисел необходимо найти элементы, которые есть во всех кортежах.\n\nРЕШЕНИЕ:')
print(set(set(x[0]).intersection(x[1]).intersection(x[2])))

# Задание 2
print('\nЗАДАНИЕ 2: Есть три кортежа целых чисел необходимо найти элементы, которые уникальны для каждого списка.\n\nРЕШЕНИЕ:')
for _ in x:
    print(f'Уникальные значения: {set(_)}')

# Задание 3
print('\nЗАДАНИЕ 3: Есть три кортежа целых чисел необходимо найти элементы, которые есть в каждом из кортежей и находятся в каждом из кортежей на той же позиции.\n\nРЕШЕНИЕ:')
Flag = True
for i in x[0]:
    if x[0][i] == x[1][i] == x[2][i]: print(f'Индекс: {i}\tЗначение: {x[0][i]}'); Flag = False
if Flag: print('Таких элементов нет')
