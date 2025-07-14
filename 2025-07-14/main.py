#!/usr/bin/python3

# Упаковка данных JSON
# JSON - JavaScrript Object Notation - файл, который иисользуется для передачи данных между сервером и веб-приложением.

import json

#empty = '{"name": "Nikita", "depart": "frilance", "company": "sberbank"}' # Строка формата JSON
#empty_dict = json.loads(empty) # Распаковка строки в object json

#print(empty_dict)
#print(empty_dict['depart'])
#print(type(empty_dict))

# Работа с файлом
#f = open("student.json")
#data = json.load(f)
#for i in data: print(i)
#f.close()

# Для конвертации из объекта Python в JSON используют функции: json.dump() и json.dumps()

dictionary = {"name": "sasha", "dep": "HR", "com": "gfg"}
json_object = json.dumps(dictionary) # Преобразования из словаря в строку JSON
print(type(json_object))
print(json_object)

with open("dict.txt", "w") as file: json.dump(dictionary, file)

# Форматирование JSON

json_data = '[{"studentif": 1, "name": "Alex", "subjects": ["Python", "Data Structures", "JavaScript"]},' \
            '{"studentif": 2, "name": "Sasha", "subjects": ["Java", "C++"]}]'

data = json.loads(json_data)
json_formattes_str = json.dumps(data, indent=4, sort_keys=True)
print(json_formattes_str)

