#!/usr/bin/python3

# Функция ввода числа с проверкой
def Num(txt):
    while True:
        _ = input(f'{txt}: ')
        if _.isnumeric(): return int(_)
        else: print('Ошибка: Введенные данные не содержат чило!\n')

val = [0, 0]

# Задание 1
while True:
   val[0] = Num('Введите размер стороны квадрата (до 20)')
   if val[0] <= 20: break
   else: print('Ошибка: размер должен быть до 20!\n')

print('Результат:')
for _ in range(val[0]):
   print('*' * val[0])

# Задание 2
val[0] = Num('Введите ширину прямоугольника)')
val[1] = Num('Введите высоту прямоугольника)')

print('Результат:')
for _ in range(val[1]):
   print('*' * val[0])

# Задание 3
while True:
   val[0] = Num('\nВведите размер стороны квадрата (до 20)')
   if val[0] <= 20: break
   else: print('Ошибка: размер должен быть до 20!\n')

print('Результат:')
for _ in range(val[0]):
   if _ == 0 or _ == val[0] -1: print('*' * val[0])
   else:
      for i in range(val[0]):
          if i == 0 or i == val[0] -1: print('*', end = '')
          else: print(' ', end = '')
      print('')


# Задание 4
val[0] = Num('Введите ширину прямоугольника)')
val[1] = Num('Введите высоту прямоугольника)')

print('Результат:')
for _ in range(val[1]):
   if _ == 0 or _ == val[1] -1: print('*' * val[0])
   else:
      for i in range(val[0]):
          if i == 0 or i == val[0] -1: print('*', end = '')
          else: print(' ', end = '')
      print('')

