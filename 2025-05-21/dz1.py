#!/usr/bin/python3

import os.path

#Задание 1
mass = []
with open('slova.txt', 'r') as f:
    for _ in f: mass.append(_.strip())
with open('text.txt', 'r') as f: data = f.read()
for _ in mass: data = data.replace(_, "")
with open('dz1_result1.txt', 'w') as f: f.write(data)

#Задание 2
print('ЗАДАНИЕ 2:')
mass1 = []
mass2 = []
with open('transl.txt', 'r') as f:
    for _ in f:
        t = _.replace('\n', '').split(':')
        mass1.append(t[0])
        mass2.append(t[1])
txt = input('Введите стркоу: ')
txt2 = ''
for x in range(len(txt)):
    if txt[x].isalpha(): txt2 += mass2[mass1.index(txt[x].lower())]
    else: txt2 += txt[x]
print(f'Результат: {txt2}\n\n')

#Задание 3
mass = []
while True:
    _ = input('Введите название файла, либо введите quit для выхода: ')
    if _ == 'quit': break
    mass.append(_)
with open('dz1_result3.txt', 'w') as f1:
    for _ in mass:
        if os.path.exists(_):
            with open(_, 'r') as f2:
                data = f2.read()
                f1.write(data)

#Задание 4
print('ЗАДАНИЕ 4:')
mass = []
while True:
    _ = input('Введите название файла, либо введите quit для выхода: ')
    if _ == 'quit': break
    mass.append(_)
res = []
for _ in mass:
    if os.path.exists(_):
        res.append('')
        with open(_, 'r') as f2:
            data = f2.read()
            for x in data:
                if not x in res[len(res)-1]: res[len(res)-1] += x
res2 = ''
if len(res) == 0: exit
if len(res) == 1: res2 = res[0]
else:
    for i in res[0]:
        Flag = True
        for _ in range(1, len(res)):
            if not i in res[_]: Flag = False
        if Flag: res2 += i
with open('dz1_result4.txt', 'w') as f: f.write(res2)

