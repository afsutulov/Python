#!/usr/bin/python3

import json

def zd2_ijson(txt):
    i = 0
    for _ in txt:
        if _["category"] == "Electronics": i += 1
    return i

def zd2_price(txt):
    for _ in txt:
        if _["price"] > 50: print(f"Товар: {_}")

def zd2_Find(txt):
    x = []
    for _ in txt:
        for y in _["reviews"]:
            print(y)
            if y["rating"] == 5: _["category"] = "Featured"
        x.append(json.dumps(_))
    return x

def zd3_FindSotr(txt, id):
    for _ in txt["employees"]:
        if id == 0: print(f'Имя: {_["name"]}')
        elif _["id"] == id: print(f'Данные сотрудника: {_}')

def zd3_FindSales(txt):
    x = []
    for _ in txt["employees"]:
        if _["department"] == "Sales": x.append(json.dumps(_))
    return x

def zd4_Find(txt, ind):
    for _ in txt["items"]:
        if _["id"] == ind: print(f"Элемент по заданному индексу: {_}")

def zd4_Sum(txt):
    i = 0
    for _ in txt["items"]:
        i += _["price"]
    return i

def zd4_Add(txt, ind, name, price):
    txt["items"].append(f'id": {ind}, "name": {name}, "price": {price}')
    return txt

def zd5_City(txt):
    return txt["person"]["address"]["city"]

def zd5_Phone(txt, phone):
    txt["person"]["contact"]["phone"] = phone
    with open("dz25.json", "w") as file: json.dump(txt, file)
    print(f"Данные с измененным номером телефона записаны в файл: dz25.json")

def zd5_Del(txt):
    del txt["person"]["contact"]
    return txt

def zd6_Load(path):
    with open(f"{path}dz26.json", "r") as file: data = json.load(file)
    return data["age"]

def zd6_Save(txt):
    txt["is_active"] = False
    with open(f"dz26.json", "w") as file: json.dump(txt, file)
    print("Измененные данные сохранены в файл: dz26.json")

print("ЗАДАНИЕ 1")
data = json.loads('{"userId": 1,"id": 1,"title": "delectus aut autem","completed": false}')
print(f'Значение title: {data["title"]}')
data["completed"] = True
print(f"Измененное значение: {data}")

print("\nЗАДАНИЕ 2")
data = json.loads('[{"id": 1,"name": "Product A","description": "This is a great product.","price": 19.99,"category": "Electronics","reviews": [{"rating": 5, "comment": "Excellent!"},{"rating": 4, "comment": "Good product."}]},{"id": 2,"name": "Product B","description": "A very useful tool.","price": 49.99,"category": "Tools","reviews": [{"rating": 3, "comment": "Okay."},{"rating": 5, "comment": "Highly recommended!"}]},{"id": 3,"name": "Product C","description": "The best in class.","price": 99.99,"category": "Electronics","reviews": [{"rating": 5, "comment": "Fantastic!"},{"rating": 5, "comment": "Amazing quality."}]},{"id": 4,"name": "Product D","description": "Another product","price": 15.50,"category": "Books","reviews": [{"rating": 4, "comment": "Good read"}]},{"id": 5,"name": "Product E","description": "Another product","price": 22.75,"category": "Books","reviews": [{"rating": 5, "comment": "Wonderful!"}]}]')
print(f"Количество товаров в категории Electronics: {zd2_ijson(data)}")
print("Товары дороже 50:")
zd2_price(data)
data = zd2_Find(data)
print(f"Новое значение:\n{data}")

print("\nЗАДАНИЕ 3")
data = json.loads('{"company": "Acme Corp","employees": [{"id": 101,"name": "Bob Johnson","department": "IT","skills": ["Python", "JavaScript"]},{"id": 102,"name": "Jane Williams","department": "Sales","skills": ["Salesforce", "Communication"],"address": { "city": "Paris", "zip": "75001" }}],"location": {"address": "456 Oak Ave","city": "Los Angeles","country": "USA"}}')
zd3_FindSotr(data, 0)
zd3_FindSotr(data, int(input("\nВведите id сотрудника: ")))
data = zd3_FindSales(data)
print(f"Только продаваны: {data}")

print("\nЗАДАНИЕ 4")
data = json.loads('{"items": [{"id": 1, "name": "Laptop", "price": 1200},{"id": 2, "name": "Mouse", "price": 25},{"id": 3, "name": "Keyboard", "price": 75}]}')
zd4_Find(data, int(input("Введите индекс: ")))
print(f"Сумма всех товаров: {zd4_Sum(data)}")
data = zd4_Add(data, 4, "Webcam", 50)
print(f"Новое значение: {data}")

print("\nЗАДАНИЕ 5")
data = json.loads('{"person": {"name": "Alice Smith","address": {"street": "123 Main St","city": "London","country": "UK"},"contact": {"email": "alice@example.com","phone": "+44 1234567890"}}}')
print(f"Город: {zd5_City(data)}")
zd5_Phone(data, input("Введите новый номер телефона: "))
data = zd5_Del(data)
print(f"Измененные данные: {data}")

print("\nЗАДАНИЕ 6")
print(f'Значение age: {zd6_Load("./")}')
zd6_Save(data)
