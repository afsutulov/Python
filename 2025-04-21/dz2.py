#!/usr/bin/python3

# Функция ввода числа с проверкой
def Num(txt):
    while True:
        _ = input(f'{txt}: ')
        if _.isnumeric(): return int(_)
        else: print('Ошибка: Введенные данные не содержат чило!\n')

val = [0, 0]

# Задание 1
val[0] = Num('Введите размер стороны квадрата')
print('Результат:')
for _ in range(val[0]):
   print('*' * val[0])

# Задание 2
val[0] = Num('\nВведите ширину прямоугольника')
val[1] = Num('Введите высоту прямоугольника')
print('Результат:')
for _ in range(val[1]):
   print('*' * val[0])

# Задание 3
val[0] = Num('\nВведите размер стороны квадрата')
print('Результат:')
for i in range(val[0]):
    for j in range(val[0]):
        if i == 0 or j == 0 or i == val[0] - 1 or j == val[0] - 1: print('*', end = '')
        else: print(' ', end = '')
    print('')

# Задание 4
val[0] = Num('\nВведите ширину прямоугольника')
val[1] = Num('Введите высоту прямоугольника')
print('Результат:')
for i in range(val[1]):
    for j in range(val[0]):
        if i == 0 or j == 0 or i == val[1] - 1 or j == val[0] - 1: print('*', end = '')
        else: print(' ', end = '')
    print('')
