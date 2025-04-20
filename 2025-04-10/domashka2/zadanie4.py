#!/usr/bin/python3

# Пользователь вводит с клавиатуры два числа. Первое число — это значение, второе число процент, который нобходимо посчитать.

SetDate = ['число', 'процент']
val = [0, 0]

for _ in range(0, len(val)):
    Flag = True
    while Flag:
        val[_] = input(f'Ведите {SetDate[_]}: ')
        if val[_].isnumeric():
           Flag = False
           val[_] = int(val[_])
        else:
           print('Ошибка: Введенные данные не содержат чило!\n')

print(f'\nРезультат: {val[0] * val[1] / 100}')
