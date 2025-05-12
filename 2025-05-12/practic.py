#!/usr/bin/python3

import random

# Есть стомпа алладий различного раидуса. Единственная операция проводимая с ними - между двумя любыми алладьями просовываем ломатку и меняем ломатку алладиев на обратный

def pancakes_sort(mass):
    print(mass)
    global oper
    if len(mass) <= 1: return mass
    oper += 1
    return pancakes_sort([x for x in mass if x > mass[len(mass) // 2]]) + [x for x in mass if x == mass[len(mass) // 2]] + pancakes_sort([x for x in mass if x < mass[len(mass) // 2]])

pancakes = [3, 1, 4, 5, 9, 6, 4, 3, 6, 2, 4, 7]
oper = 0
print(f'Результат: {pancakes_sort(pancakes)}\nКоличество операций: {oper}')
