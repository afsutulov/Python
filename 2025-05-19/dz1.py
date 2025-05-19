#!/usr/bin/python3

# Задание 1
#with open('text.txt', 'w') as f: f.write('banana mango me the math mango-banana guava-ti-python')
with open('text.txt', 'r') as f: buffer = f.read()
with open('dz_result1.txt', 'w') as f:
    for _ in buffer.split(' '):
        if len(_) > 6: f.writelines(f'{_}\n')

# Задание 2
mass = []
with open('text.txt', 'r') as f:
    for _ in f: mass.append(_.strip())
with open('dz_result2.txt', 'w') as f:
    for _ in mass: f.writelines(f'{_}\n')

# Задание 3
mass.reverse()
with open('dz_result3.txt', 'w') as f:
    for _ in mass: f.writelines(f'{_}\n')

# Задание 4
Flag = True
for _ in range(len(mass)):
    if ',' in mass[_] and Flag: mass.insert(_, '*' * 12); Flag = False
if Flag: mass.append('*' * 12)
mass.reverse()
with open('dz_result4.txt', 'w') as f:
    for _ in mass: f.write(f'{_}\n')

# Задание 5
s = input('Введите символ: ')
i = 0
for _ in mass:
    for l in _.split(' '):
       if l[0] == s: i += 1
print(f'Задание 5: Резульатат: {i}\n')

# Задание 6
with open('dz_result6.txt', 'w') as f:
    for _ in mass:
        if _ != '*' * 12: f.write(f'{_.replace("*", "&")}\n')

# Задание 7
mass = {'Mama mils ramu', 'Uma turman', 'Na pole tanki grohotali', 'Ura!!!', 'Ya ne narkoman'}
with open('dz_result7.txt', 'w') as f:
    for _ in mass: f.write(f'{_}\n')

# Задание 8
with open('dz_result7.txt', 'w') as f:
    for _ in mass: f.write(f'{_}\n')

# Задание 9
with open('text.txt', 'r') as f: buffer = f.read()
print(f'Задание 9: {len(buffer)}')

# Задание 9
with open('text.txt', 'r') as f: buffer = f.read()
print(f'Задание 9: {len(buffer)}')

# Задание 10
mass = []
with open('text.txt', 'r') as f:
    for _ in f: mass.append(_.strip())
print(f'Задание 10: {len(mass)}')
