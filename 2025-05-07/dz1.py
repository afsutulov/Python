#!/usr/bin/python3

import random

# Функция ввода числа с проверкой
def Num(txt, n1, n2):
    if n1 > n2: n1, n2 = n2, n1
    _ = input(f'{txt}: ')
    if _.isnumeric() and n1 <= int(_) <=n2: return int(_)
    else: print(f'Ошибка ввода! Необходимо ввести число от {n1} до {n2}!\n'); return Num(txt, n1, n2)

def Sort(mass, x):
    for i in range(x):
       for j in range(i, x):
          if mass[i] > mass[j]: mass[i], mass[j] = mass[j], mass[i]
    return mass

rnd = [random.randint(-100, 100) for i in range(30)]

# Задание 1
print(f'Первоначальный список: {rnd}')
if sum(rnd) / len(rnd) > 0 : print('Больше нуля!'); Sort(rnd, len(rnd) // 3 * 2)
else: print('Меньше нуля!'); Sort(rnd, len(rnd) // 3)
print(f'Конечный список: {rnd}')

# Задание 2
mass = []
while len(mass) < 10: mass.append(Num(f'Введите оценку {len(mass) + 1}', 1, 12))
print(f'\nОценки: {mass}')
mass[Num('Какую оценку заменить (1 - 10)', 1, 10) -1] = Num('\nВведите новую оценку', 1, 12)
print(f'Новые Оценки: {mass}')
if sum(mass) > 70: print('Стипендия будет!')
else: print('Стипендии не будет :(')
mass.sort()
print(f'Отсортированные оценки {mass}')

# Задание 3
rnd = [random.randint(-100, 100) for i in range(30)]
print(f'Первоначальный список: {rnd}')
i = 1
while i != 0:
    i = 0
    for j in range(len(rnd) - 1):
      if rnd[j] > rnd[j+1]: rnd[j], rnd[j+1] = rnd[j+1], rnd[j]; i += 1
print(f'Отсортированный список: {rnd}')
