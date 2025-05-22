#!/usr/bin/python3

import json, os.path

# Функция ввода числа с проверкой
def Num(txt, n1, n2):
    _ = input(f'{txt}: ')
    if _.isnumeric() and n1 <= int(_) <=n2: return int(_)
    else: print(f'Ошибка ввода! Необходимо ввести число от {n1} до {n2}!\n'); return Num(txt, n1, n2)

# Функция вывода списка сотрудников
def Peoples():
    print(f'СПИСОК СОТРУДНИКОВ:\n{"-"*62}\n| {"№":^5}| {"ФАМИЛИЯ":^20}| {"ИМЯ":^20}| {"ВОЗРАСТ":^8}|\n{"-"*62}')
    if len(data) == 0: print(f'{"список пуст":^62}')
    for i, _ in enumerate(data): print(f'| {i + 1:^5}| {_["famaly"]:<20}| {_["name"]:<20}| {_["age"]:^8}|')
    print(f'{"-"*62}\n')

# Функция добавления пользователя
def AddPeople():
    print('\nДобавление сотрудника:')
    data.append({'famaly': input('\tВведите Фамилию сотрудника: '), 'name': input('\tВведите Имя сотрудника: '), 'age': Num('\tВведите возраст сотрудника', 18, 100)})

# Функцтя удаления пользователя
def DelPeople():
    print('\nУдаление сотрудника')
    data.pop(Num('Введите сотрудника, которого необходимо удалить',1, len(data)) - 1)

# Функция редактирования данных пользователя
def EditPeople():
    print('\nРедактирование данных сотрудника')
    _ = Num('Введите номер сотрудника для редактирования', 1, len(data)) - 1
    data[_]['famaly'] = input(f'\nПредыдущие фамилия: {data[_]["famaly"]}\nВведите новую Фаилию: ')
    data[_]['name'] = input(f'\nПредыдущие фамилия: {data[_]["name"]}\nВведите новую Фаилию: ')
    data[_]['age'] = input(f'\nПредыдущие фамилия: {data[_]["age"]}\nВведите новую Фаилию: ')

# Функция поиска сотрудников по фамилии
def SearchFamily():
    print('\nПОИСК СОТРУДНИКОВ ПО ФАМИЛИИ')
    f = input('Введите Фамилию для поиска: ')
    tmp = []
    for _ in data:
        if _['famaly'] == f: print(f'Фамилия: {_["famaly"]:<20}Имя: {_["name"]:<20}\tВозраст: {_["age"]}'); tmp.append(_)
    print()
    if len(tmp) != 0: SaveDataFile(tmp)

# Функция поиска сотрудников по возрасту
def SearchAge():
    print('\nПОИСК СОТРУДНИКОВ ПО ВОЗРАСТУ')
    f = Num('Введите возраст для поиска: ', 18, 100)
    tmp = []
    for _ in data:
        if _['age'] == f: print(f'Фамилия: {_["famaly"]:<20}Имя: {_["name"]:<20}Возраст: {_["age"]}'); tmp.append(_)
    print()
    if len(tmp) != 0: SaveDataFile(tmp)

# Функция поиска сотрудников по первой букве фамилии
def SearchFamS():
    print('\nПОИСК СОТРУДНИКОВ ПО ПЕРВОЙ БУКВЕ ФАМИЛИИ')
    f = ''
    while len(f) != 1: f = input('Введите первую букву фамилии: ')
    tmp = []
    for _ in data:
        if _['famaly'][0] == f: print(f'Фамилия: {_["famaly"]:<20}Имя: {_["name"]:<20}Возраст: {_["age"]}'); tmp.append(_)
    if len(tmp) != 0: SaveDataFile(tmp)

# Функция загрузкти данных из файла
def LoadFile(x):
    if os.path.exists(x):
        with open(x, 'r') as f: return json.load(f)
    else: print('Не удалось загрузить данные из файла {x}'); return []

# Функция сохранения результатов поиска в файл
def SaveDataFile(x):
    match Num(f'\n\nСохранить результаты поиска в файл (0 - нет, 1 - да)?', 0, 1):
        case 1: SaveFile(input('Введите имя файла для сохранения данных поиска: '), x)

# Функция сохранения данных в файл
def SaveFile(x, y):
    with open(x, 'w') as f: f.write(json.dumps(y))
    print(f'\nДанные сохранены в файл: {x}!\n')

# Тело программы
def main():
    global data
    data = LoadFile(input('Введите имя файла из которого необходимо загрузить сохраненные данные (при выходе данные автоматически сохраняются в dz2_result.json): '))
    while True:
        Peoples()
        match Num('\nДействия:\n\t1. Вывести список всех сотрудников\n\t2. Добавить сотрудника\n\t3. Редактировать данные сотрудника\n\t4. Удалить сотрудника\n\t5. Поиск сотрудников по фамилии\n\t6. Поиск сотрудников по возрасту\n\t7. Поиск сотрудников по первой букве\n\t8. Загрузить данные из файла\n\t9. Сохранить данные в файл\n\t0 - Выход\n\nВведите действие', 0, 9):
            case 0: SaveFile('dz2_result.json', data); break
            case 1: Peoples()
            case 2: AddPeople()
            case 3: EditPeople()
            case 4: DelPeople()
            case 5: SearchFamily()
            case 6: SearchAge()
            case 7: SearchFamS()
            case 8: data = LoadFile(input('Введите название файла: '));
            case 9: SaveFile('dz2_result.json', data)

if __name__ == '__main__': main()
