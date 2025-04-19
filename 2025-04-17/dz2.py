#!/usr/bin/python3

# Функция ввода числа с проверкой
def Num(txt):
    Flag = True
    while Flag:
        _ = input(f'{txt}: ')
        if _.isnumeric():
           Flag = False
           return int(_)
        else:
           print('Ошибка: Введенные данные не содержат чило!\n')


# Задание 1

val = str(Num('Введите шестизначное число'))

if len(val) == 6:
  if int(val[0]) * int(val[1]) * int(val[2]) == int(val[3]) * int(val[4]) * int(val[5]):
     print('Число счастливое!')
  else:
     print('Число несчастливое!')
else:
  print('Введено не шестизначное число!')


# Задание 2

val = str(Num('\nВведите шестизначное число'))

if len(val) == 6:
   print(f'Результат: {val[5]}{val[4]}{val[2]}{val[3]}{val[1]}{val[0]}')
else:
  print('Введено не шестизначное число!')


# Задание 3

val = Num('\nВведите номер месяца')

match val:
    case 1: print(f'Winter')
    case 2: print(f'Winter')
    case 3: print(f'Spring')
    case 4: print(f'Spring')
    case 5: print(f'Spring')
    case 6: print(f'Summer')
    case 7: print(f'Summer')
    case 8: print(f'Summer')
    case 9: print(f'Autumn')
    case 10: print(f'Autumn')
    case 11: print(f'Autumn')
    case 12: print(f'Winter')
    case _: print(f'Введен некорректный месяц!')

