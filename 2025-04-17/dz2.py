#!/usr/bin/python3

# Функция ввода числа с проверкой
def Num(txt):
    while True:
        _ = input(f'{txt}: ')
        if _.isnumeric(): return int(_)
        else: print('Ошибка: Введенные данные не содержат чило!\n')


# Задание 1
while True:
   val = str(Num('Введите шестизначное число'))
   if len(val) == 6:
      if int(val[0]) * int(val[1]) * int(val[2]) == int(val[3]) * int(val[4]) * int(val[5]): print('Число счастливое!')
      else: print('Число несчастливое!')
      break
   else:
      print('Ошибка: Введено не шестизначное число!\n')


# Задание 2
while True:
   val = str(Num('\nВведите шестизначное число'))
   if len(val) == 6:
      print(f'Результат: {val[5]}{val[4]}{val[2]}{val[3]}{val[1]}{val[0]}')
      break
   else:
      print('Ошибка: Введено не шестизначное число!\n')


# Задание 3
while True:
   val = Num('\nВведите номер месяца')
   match val:
      case 1 | 2 | 12: print('Winter')
      case 3 | 4 | 5: print('Spring')
      case 6 | 7 | 8: print('Summer')
      case 9 | 10 | 11: print('Autumn')
      case _: 
         print(f'Ошибка: Введен некорректный месяц!')
         continue
   break
