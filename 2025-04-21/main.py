#!/usr/bin/python3

import random
import datetime

# Функция ввода числа с проверкой
def Num(txt):
    while True:
        _ = input(f'{txt}: ')
        if _.isnumeric(): return int(_)
        else: print('Ошибка: Введенные данные не содержат чило!\n')

val = [0, 0, 0]

# Задание 1
while True:
   val[0] = Num('Введите число')
   if val[0] < 10: break
   else: print('Введите число меньше 10\n')

for _ in range(10):
    print(f'{val[0]} * {_} = {val[0] * _}')
print('\n\n')

# Задание 2
val[0] = Num('Введите сумму в рублях')
print('\nКонвертировать:\n\t1: Доллары США\n\t2: Евро\n\t3: Казахстанские Тенге')
go = Num('Введите нужное действие')
match go:
   case 1: print(f'Сумма в Долларах США: { val[0] * 85}\n')
   case 2: print(f'Сумма в Евро: { val[0] * 105}\n')
   case 3: print(f'Сумма в Казахстанских Тенге:{ val[0] * 5,15}\n')
   case _: print('Ошибка! Вы ввели неправильное действие!\n')

# Задание 3
while True:
    val[0] = Num('Введите нижнюю границу диапазона')
    val[1] = Num('Введите верхнюю границу диапазона')
    val[2] = Num('Введите число')
    if val[2] >= val[0] and val[2] <= val[1]: break
    else: print('Введены некорректные данные, повторите попытку\n')

for _ in range(val[0], val[1] + 1):
   if _ == val[2]: print(f'!{_}!', end = '')
   else:  print(_, end = '')

# Задание 4
print('\n\nДобро пожаловать в игру Угадай число')
print('Пытаешься угадать число от 1 до 500. Я даю тебе подсказку')
print('*' * 11)
print('\n')

random_value = random.randint(1, 500)
i = 0
user_time = datetime.datetime.now()

while True:
   val = Num('Введите предполагаемое число')
   if val == 0: break
   i += 1
   if val == random_value:
      print('Вы угадали число! Поздравляю!\n')
      break
   elif val < random_value:
      print('Ваше число меньше загаданного\n')
   elif val > random_value:
      print('Ваше число больше загаданного\n')

print('*' * 11)
print(f'Статистика:\n\tПопыток: {i}\n\tВремя: {datetime.datetime.now() - user_time}')
