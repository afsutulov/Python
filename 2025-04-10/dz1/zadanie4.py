#!/usr/bin/python3

# Напишите программу, вычисляющую площадь треугольника. Пользователь с клавиатуры вводит размер основания треугольника и размер высоты.

SetDate = ['основания', 'высоты']
val = [0, 0]

for _ in range(0, len(SetDate)):
    Flag = True
    while Flag:
        val[_] = input(f'Ведите размер {SetDate[_]} треугольника: ')
        if val[_].isnumeric():
           Flag = False
           val[_] = int(val[_])
        else:
           print('Ошибка: Введенные данные не содержат чило!\n')

print(f'\nПлощадь треугольника: {val[0] * val[1] /2}')
