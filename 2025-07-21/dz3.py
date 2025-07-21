#!/usr/bin/python3

#1. Простой итератор для списка:
class MyList:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.data):
            value = self.data[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration

if __name__ == "__main__":
    print("1. Простой итератор для списка:")
    my_list = MyList([1, 2, 3])
    for item in my_list: print(f"\t{item}")


#2. Итератор для генерации чисел Фибоначчи:
class FibonacciIterator:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        value = self.a
        self.a, self.b = self.b, self.a + self.b
        return value

if __name__ == "__main__":
    print("\n2. Итератор для генерации чисел Фибоначчи:")
    fib_iter = FibonacciIterator()
    for i in range(10): print(f"\t{next(fib_iter)}")


#3. Итератор для обхода бинарного дерева (усложненный):
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root: Node):
        self.root = root

    def add_node(self, node: Node, direction: str, path=None):
        current = self.root
        if path:
            for d in path if isinstance(path, list) else [path]:
                if d == "left":
                    current = current.left
                elif d == "right":
                    current = current.right
        if direction == "left":
            current.left = node
        elif direction == "right":
            current.right = node

    def __iter__(self):
        return self._in_order_traversal(self.root)

    def _in_order_traversal(self, node):
        if node:
            yield from self._in_order_traversal(node.left)
            yield node
            yield from self._in_order_traversal(node.right)

if __name__ == "__main__":
    print("\n3. Итератор для обхода бинарного дерева (усложненный):")
    # Создание дерева
    tree = BinaryTree(Node(1))
    tree.add_node(Node(2), "left")
    tree.add_node(Node(3), "right")
    tree.add_node(Node(4), "left", "left")
    # Обход дерева (in-order)
    for node in tree: print(f"\t{node.value}")


#4. Итератор для чтения строк из файла (ленивое чтение):
class FileLineIterator:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.file is None:
            self.file = open(self.filename, "r")

        line = self.file.readline()
        if line == "":
            self.file.close()
            raise StopIteration
        return line

if __name__ == "__main__":
    print("\n4. Итератор для чтения строк из файла (ленивое чтение):")
    file_iter = FileLineIterator("my_file.txt")
    for line in file_iter: print(line.strip())


#5. Итератор с фильтрацией (комбинирование с паттерном Strategy):
class EvenFilter:
    def apply(self, value):
        return value % 2 == 0

class OddFilter:
    def apply(self, value):
        return value % 2 != 0

class GreaterThanFilter:
    def __init__(self, threshold):
        self.threshold = threshold

    def apply(self, value):
        return value > self.threshold

class DataIterator:
    def __init__(self, data, filter_strategy):
        self.data = data
        self.filter_strategy = filter_strategy
        self.index = 0

    def __iter__(self):
        self.index = 0  # сброс на начало
        return self

    def __next__(self):
        while self.index < len(self.data):
            value = self.data[self.index]
            self.index += 1
            if self.filter_strategy.apply(value):
                return value
        raise StopIteration

if __name__ == "__main__":
    print("\n5. Итератор с фильтрацией (комбинирование с паттерном Strategy):")
    data = [1, 2, 3, 4, 5, 6]
    # Фильтрация четных чисел
    print("Четные:")
    even_iter = DataIterator(data, EvenFilter())
    for num in even_iter: print(num)
    # Фильтрация чисел больше 3
    print("\nБольше 3:")
    greater_than_iter = DataIterator(data, GreaterThanFilter(3))
    for num in greater_than_iter: print(num)


#6. Итератор, комбинированный с другим паттерном (например, Factory или Decorator):
import json

class Product:
    def __init__(self, product_id, name, price):
        self.id = product_id
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} (ID: {self.id}) — ${self.price:.2f}"

class ProductFactory:
    def create_product(self, product_data):
        return Product(
            product_id=product_data["id"],
            name=product_data["name"],
            price=product_data["price"]
        )

    def create_products_from_json(self, json_str):
        data = json.loads(json_str)
        return [self.create_product(item) for item in data]

class ProductIterator:
    def __init__(self, products):
        self.products = products
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.products):
            product = self.products[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration

class DiscountProductIterator:
    def __init__(self, product_iterator, discount_percent):
        self.product_iterator = product_iterator
        self.discount = discount_percent / 100

    def __iter__(self):
        return self

    def __next__(self):
        product = next(self.product_iterator)
        discounted_price = product.price * (1 - self.discount)
        return Product(product.id, product.name, discounted_price)
if __name__ == "__main__":
    print("\n6. Итератор, комбинированный с другим паттерном (например, Factory или Decorator):")
    # Пример JSON-данных
    json_data = '''
    [
        {"id": 1, "name": "Laptop", "price": 1500},
        {"id": 2, "name": "Smartphone", "price": 800},
        {"id": 3, "name": "Tablet", "price": 400}
    ]
    '''
    # Создание продуктов через фабрику
    factory = ProductFactory()
    products = factory.create_products_from_json(json_data)
    # Обычный итератор
    print("== Без скидки ==")
    product_iter = ProductIterator(products)
    for p in product_iter: print(p)
    # Скидочный итератор (например, 20%)
    print("\n== Со скидкой 20% ==")
    discount_iter = DiscountProductIterator(ProductIterator(products), discount_percent=20)
    for p in discount_iter: print(p)
