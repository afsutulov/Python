#!/usr/bin/python3

# Напишите программу, вычисляющую площадь прямоугольника.

SetDate = ['ширину', 'высоту']
val = [0, 0]

for _ in range(0, len(val)):
    Flag = True
    while Flag:
        val[_] = input(f'Ведите {SetDate[_]} прямоугольника: ')
        if val[_].isnumeric():
           Flag = False
           val[_] = int(val[_])
        else:
           print('Ошибка: Введенные данные не содержат чило!\n')

print(f'\nПлощадь прямоугольника: {val[0] * val[1]}')
