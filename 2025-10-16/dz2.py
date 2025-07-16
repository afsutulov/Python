#!/usr/bin/python3

import json, datetime

def zd7_Load(path):
    with open(path, "r") as file: data = json.load(file)
    return data


print("ЗАДАНИЕ 7")
data = zd7_Load("dz27.json")
some_date = datetime.datetime.fromisoformat(data["created_at"])
print(f"Объект datetime: {some_date}")
if data["is_active"] == True: print("Да, проверил. True")
i = 0
for _ in data["data"]:
    i += _["value"]
print(f"Сумма всех value: {i}")
if data["metadata"] == None: data["metadata"] = "No metadata"
print(data["metadata"])
if data["settings"]["threshold"] > 0.7: print("Да, threshold больше 0.7")
else: print("Нет, threshold меньше или равно 0.7")


print("\nЗАДАНИЕ 8")

def zd8_Func(txt):
    return {"fruits": txt}

def zd8_Save(txt):
    with open("dz28.json", "w") as f: json.dump(txt, f, indent=4)
    print("Данные сохранены в файл dz28.json")

data = ["apple", "banana", "cherry"]
zd8_Save(zd8_Func(data))


print("\nЗАДАНИЕ 9")
data = zd7_Load("dz29.json")
print(data)


print("\nЗАДАНИЕ 11")
data = json.loads('[{"name": "Alice", "score": 85, "city": "London"},{"name": "Bob", "score": 92, "city": "Paris"},{"name": "Charlie", "score": 78, "city": "New York"}]')
txt = "name,score,city\n"
for _ in data:
    txt += f'{_["name"]};{_["score"]};{_["city"]}\n'
txt = txt.rstrip()
print(f"Результат перевода JSON в CSV:\n{txt}\n")
date = {}
for _ in txt.split("\n"):
    if _ == "name,score,city": continue
    x = _.split(";")
    data.append({"name": x[0], "score": x[1], "city": x[2]})
print(f"Результат перевода CSV в JSON:\n{data}")


print("\nЗАДАНИЕ 12")
x = ["Alice", "30", "London"]
y = ["Bob", "25", "Paris"]
data = "["
for i in range(len(x)):
    data += "{" + f'"{x[i]}": "{y[i]}"' + "}\n"
data += "]"
print(data)
data = json.loads(data)
print(data)

