#!/usr/bin/python3

import random
import datetime

# Функция ввода числа с проверкой
def Num(txt, indx):
    while True:
        _ = input(f'{txt}: ')
        if _.isnumeric():
           if indx == 0 or len(_) == indx: return int(_)
           else: print(f'Ошибка: Введенные не {indx} чило!\n')
        else: print('Ошибка: Введенные данные не содержат чило!\n')

val = [0, 0, 0]

# Задание 1
val[0] = Num('Введите число', 1)
for _ in range(10):
    print(f'{val[0]} * {_ + 1} = {val[0] * (_ + 1)}')
print('\n')

# Задание 2
val[0] = Num('Введите сумму в рублях', 0)
print('\nКонвертировать:\n\t1: Доллары США\n\t2: Евро\n\t3: Казахстанские Тенге')
go = Num('Введите нужное действие', 1)
match go:
   case 1: print(f'Сумма в Долларах США: { val[0] * 85}\n')
   case 2: print(f'Сумма в Евро: { val[0] * 105}\n')
   case 3: print(f'Сумма в Казахстанских Тенге:{ val[0] * 5,15}\n')
   case _: print('Ошибка! Вы ввели неправильное действие!\n')

# Задание 3
while True:
    val[0] = Num('Введите нижнюю границу диапазона', 1)
    val[1] = Num('Введите верхнюю границу диапазона', 1)
    val[2] = Num('Введите число', 1)
    if val[2] >= val[0] and val[2] <= val[1]: break
    else: print('Введены некорректные данные, повторите попытку\n')

for _ in range(val[0], val[1] + 1):
   if _ == val[2]: print(f' !{_}!', end = '')
   else:  print(f' {_}', end = '')
print('.')

# Задание 4
print("\nВ игре нужно угадать число от 1 до 500")

rnd = random.randint(1, 500)
i = 0
usertime = datetime.datetime.now()

while True:
   val[0] = Num('Введите предполагаемое число', 0)
   if val[0] == 0: break
   i += 1
   if val[0] == rnd:
      print(f'\n!!!ВЫ УГАДАЛИ ЧИСЛО {val[0]}! ПОЗДРАВЛЯЕМ!!!\n')
      break
   elif val[0] < rnd:
      print('Ваше число меньше загаданного\n')
   elif val[0] > rnd:
      print('Ваше число больше загаданного\n')

print(f'Статистика:\n\tПопыток: {i}\n\tВремя: {datetime.datetime.now() - usertime}')
