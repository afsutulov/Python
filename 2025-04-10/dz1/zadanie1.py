#!/usr/bin/python3

# Пользователь вводит с клавиатуры три цифры. Необходимо создать число, содержащее эти цифры

result = ""

for _ in range(1, 4):
    Flag = True
    while Flag:
        val = input(f'Ведите число {_}: ')
        if val.isnumeric():
           Flag = False
           result += val
        else:
           print('Ошибка: Введенные данные не содержат чило!\n')

print(f'\nРезультат: {result}')