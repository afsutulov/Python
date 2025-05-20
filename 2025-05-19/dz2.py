#!/usr/bin/python3

def FileRead(name):
    ms = []
    with open(name, 'r') as f:
        for _ in f: ms.append(_.strip())
    return ms

# Задание 1
mass = FileRead('text.txt')
mass2= FileRead('text2.txt')
print('ЗАДАНИЕ 1:\n')
for _ in range(max(len(mass), len(mass2))):
    if _ >= len(mass): print(f'text2.txt\tСтрока: {_ + 1}:\n{mass2[_]}\n\n'); continue
    if _ >= len(mass2): print(f'text.txt\tСтрока: {_ + 1}:\n{mass[_]}\n\n'); continue
    if mass[_] != mass2[_]: print(f'text.txt:\tСтрока: {_ + 1}\n{mass[_]}\n\ntext2.txt:\tСтрока: {_ + 1}\n{mass2[_]}\n\n')

# Задаине 2
with open('text.txt', 'r') as f: data = f.read()
mass = [0] * 3
glass = 'aeiouyауоиэыяюеё'
soglass = 'bcdfghjklmnpqrstvxxzбвгджзйклмнпрстфхцчшщ'
for _ in data:
    if _.lower() in glass: mass[0] += 1
    if _.lower() in soglass: mass[1] += 1
    if _.isdigit(): mass[2] += 1
with open('dz2_result2.txt', 'w') as f:
    x = len(data.split('\n'))
    f.write(f'Количество символов: {len(data)}\nКоличество строк: {x}\nКоличество гласных: {mass[0]}\nКоличество согласных: {mass[1]}\nКоличество цифр: {mass[2]}')

# Задание 3
mass = FileRead('text.txt')
with open('dz2_result3.txt', 'w') as f:
    for _ in range(len(mass) - 1): f.write(f'{mass[_]}\n')

# Задание 4
i = len(mass[0])
for _ in mass:
    if len(_) > i: i = len(_)
print(f'ЗАДАНИЕ 4:\nДлинна самой длинной строки: {i}\n\n')

# Задание 5
with open('text.txt', 'r') as f: data = f.read()
print('ЗАДАНИЕ 5:')
print(f'Встречается: {data.count(input("Введите заданное слово: "))} раз\n')

# Задаие 6
print('ЗАДАНИЕ 6:')
with open('text.txt', 'w') as f: f.write(data.replace(input('Введите слово для замены: '), input('Введите на что заменить: ')))
