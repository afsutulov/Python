#!/usr/bin/python3

# Пользователь вводит с клавиатуры число, состоящее из четырех цифр. Требуется найти произведение цифр.

Flag = True
while Flag:
    val = input(f'Ведите число: ')
    if val.isnumeric():
       Flag = False
    else:
       print('Ошибка: Введенные данные не содержат чило!\n')

result = 1
for _ in val:
    result *= int(_)

print(f'\nРезультат: {result}')
