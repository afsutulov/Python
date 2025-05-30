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
code = {'a':'а', 'b':'б', 'c':'с', 'd':'д', 'e':'е','f':'ф','g':'г','h':'х','i':'и','j':'ж','k':'к','l':'л','m':'м','n':'н','o':'о','p':'п','q':'ку','r':'ар','s':'с',
        't':'т','u':'ю','v':'в','w':'в','x':'кс','y':'е','z':'з','а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ё':'e','ж':'j','з':'z','и':'i','й':'i','к':'k','л':'l',
        'м':'m','н':'n','о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'h','ц':'ste','ч':'che','ш':'sh','щ':'sh','ь':'','ы':'i','ъ':'','э':'ie','ю':'yu','я':'ya'}
_= input('Введите название файла для транслитерации: ')
if os.path.exists(_):
    with open(_, 'r') as f: data = f.read().lower()
res = ''
for _ in range(len(data)):
    if data[_].isalpha(): res += code[data[_]]
    else: res += data[_]
with open('dz1_result2.txt', 'w') as f: f.write(res)

#Задание 3
print('ЗАДАНИЕ 3:')
data = ''
while True:
    _ = input('Введите название файла, либо введите quit для выхода: ')
    if _ == 'quit': break
    if os.path.exists(_):
        with open(_, 'r') as f: data += f.read()
with open('dz1_result3.txt', 'w') as f: f.write(data)

#Задание 4
print('\nЗАДАНИЕ 4:')
res = {}
while True:
    _ = input('Введите название файла, либо введите quit для выхода: ')
    if _ == 'quit': break
    if os.path.exists(_):
        with open(_, 'r') as f2:
            if res == {}: res = set(f2.read())
            else: res = res.intersection(set(f2.read()))
with open('dz1_result4.txt', 'w') as f: f.write(''.join(res))
