#!/usr/bin/python3

import json, datetime, re
import xml.etree.ElementTree as ET

print("ЗАДАНИЕ 7")
def zd7_Load(path):
    with open(path, "r") as file: data = json.load(file)
    return data

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
def convert_date(text):
    def replace(match):
        return f"{match.group(2)}/{match.group(3)}/{match.group(1)}"
    pattern = r'(\d{4})-(\d{2})-(\d{2})'
    return re.sub(pattern, replace, text)

data = zd7_Load("dz29.json")
data["text"] = convert_date(data["text"])
with open(f"dz29_new.json", "w") as f: json.dump(data, f, indent=4)
print("Данные с измененным форматом даты сохранены в файл dz9_new.json")


print("\nЗАДАНИЕ 10")
def convert_to_xml(books):
    root = ET.Element("books")
    for book in books:
        book_elem = ET.SubElement(root, "book")
        title_elem = ET.SubElement(book_elem, "title")
        title_elem.text = book["title"]
        author_elem = ET.SubElement(book_elem, "author")
        author_elem.text = book["author"]
        year_elem = ET.SubElement(book_elem, "year")
        year_elem.text = str(book["year"])
    return root

data = zd7_Load("dz210.json")
tree = ET.ElementTree(convert_to_xml(data))
tree.write("dz210.xml", encoding="utf-8", xml_declaration=True)
print("Данные сохранены в файл dz210.xml")

print("\nЗАДАНИЕ 11")
y = ["name", "score", "city"]
data = json.loads('[{"name": "Alice", "score": 85, "city": "London"},{"name": "Bob", "score": 92, "city": "Paris"},{"name": "Charlie", "score": 78, "city": "New York"}]')
txt = f"{y[0]},{y[1]},{y[2]}\n"
for _ in data:
    txt += f'{_[y[0]]};{_[y[1]]};{_[y[2]]}\n'
txt = txt.rstrip()
print(f"Результат перевода JSON в CSV:\n{txt}\n") # Заебался я сохранять в файлы. Достаточно просто на экран вывести?
date = {}
for _ in txt.split("\n"):
    if _ == f"{y[0]},{y[1]},{y[2]}": continue
    x = _.split(";")
    data.append({y[0]: x[0], y[1]: x[1], y[2]: x[2]})
print(f"Результат перевода CSV в JSON:\n{json.dumps(data, indent=4)}") # Тоже саое - сконвертировал. Вывел. Сколко можно сохранять в файлы? :)


print("\nЗАДАНИЕ 12")
x = ["Name", "Age", "City"]
y = [["Alice", "30", "London"], ["Bob", "25", "Paris"]]
data = "["
for _ in y: data += "{" + f'"{x[0]}": "{_[0]}", "{x[1]}": "{_[1]}", "{x[2]}": "{_[2]}"' + "},"
data = data.rstrip(",\n") + "]"
data = json.loads(data)
with open(f"dz212.json", "w") as f: json.dump(data, f, indent=4)
print("Данные сохранены в файл dz212.json")
