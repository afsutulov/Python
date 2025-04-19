#!/usr/bin/python3

# Пользователь с клавиатуры вводит четырёхзначное число. Необходимо перевернуть число и отобразить результат.

Flag = True
while Flag:
    val = input(f'Ведите число: ')
    if val.isnumeric():
       Flag = False
    else:
       print('Ошибка: Введенные данные не содержат чило!\n')

result = ""
for _ in val:
    result = _ + result

print(f'\nРезультат: {result}')
