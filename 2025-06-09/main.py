#!/usr/bin/python3

# Лямбда - функции это функции, которые используют следующий синтаксис:
# lambda parametes: expression
# parametes - перечень параметров, через запятую
# expression - действие с этими параметрами
# нельзя использовать циклы, условные операторы, return

# Пример 1
#s = lambda x: "1" if x == 1 else "Lambda"
#print(s(5))


# Пример 2
#def area(h, a):
#    return h*a

#a = area(5, 10)
#print(a)

#b = lambda h, a: h * a
#print(b(5, 10))

# Пример 3. Сортировка по ключу

#elements = [(a, 12, "Mg"), (1, 11, "Na"), (1, 3, "Li"), (2, 4, "Be")]

#sorted(elements)
#print(elements)

#elements.sort(key=lambda e: (e[1], e[2]))
#print(elements)

#elements.sort(key=lambda e: e[1:3])
#print(elements)

# Пример 4. Словари со значением по умолчанию

#import collections

#minus_one_dict = collections.defaultdict(lambda: -1)
#point_zero_dict = collections.defaultdict(lambda: (0, 0))
#message_dict = collections.defaultdict(lambda: "No message")
#print(minus_one_dict[0], point_zero_dict[1, 2], message_dict[3], sep="\n")

#class ObjectCreator(object):
#    pass

#my_object = ObjectCreator()
#print(my_object)
#print(ObjectCreator)

# Присваиваем объект переменной, копируем его, добавляем или изменяем атрибуты, передача значения функции

#def coose_class(name):
#    if name == "foo":
#        class Foo(object):
#            pass
#        return Foo
#    else:
#        class Bar(object):
#            pass
#        return Bar

#myClass = coose_class("foo")
#print(myClass)


# Метакласс - создание класса для автоматического изменения атирибутов класса в момент создания
# Используется в работе с API, когда нужно создавать класс, исходя из данных контекста
# Вызываются в момент создания элементов __metaclass__

#def upper_attr(future_class_name, future_param_class, future_class_parents):
#    attrs = ((name, value) for name, value in future_param_class.items() if not name.startswith("  "))
#    uppercase.attr = dict((name.upper(), value) for name, value in attrs)
#    return type(future_vlass_name, future_class_parents, uppercase_attr)

#class Foo:
#    bar = "bip"
#    __metaclass__ = upper_attr
    # Метод __new___ вызывается перед __init__
    # Этот метод создает объект и возвразает его, в то время как __init__ просто инициализирует объект, переданный в качестве аргумента
    # Обычно мы не используем __new__, если только не хотим проконтролировать процесс создания объектв класса

#print(hasattr(Foo, "bar"))
#print(hasattr(Foo, "BAR"))

#f = Foo()
#print(f.bar)

#class Person:
#    __type = "Person"
#    @staticmethod # Вызов функции, вне зависимости от объекта от этого класса
#    def print_type():
#        print(Person.__type)

#Person.print_type()

#person = Person()
#person.print_type()

class Message:
    def __init__(self, sender, recipient):
        self.sender = sender
        self.recipient = recipient

    def showHeader(self):
        print(f"Отправитель: {self.sender}\nПолучатель: {self.recipient}")

class TextMessage(Message):
    def __init__(self, sender, recipient, text):
        Message.__init__(self, sender, recipient)
        self.text = text

    def send(self):
        print()
        self.showHeader()
        print(f"Текст сообщения: {self.text}")

class StickerMessage(Message):
    def __init__(self, sender, recipient, sticker, count = 0):
        Message.__init__(self, sender, recipient)
        self.sticker = sticker
        self.count = count

    def Print(self):
        self.count += 1
        print(f"{self.sticker}\tСколько раз: {self.count}")

a = Message("Ваня", "Петя")
a.showHeader()

b = TextMessage("Вася", "Жирав", "text")
b.send()

c = StickerMessage("Петруччо", "Гагарин", "ಠ_ಠ")
c.Print()
c.Print()
c.Print()

d = StickerMessage("Пися", "Жопе", "1_1")
d.Print()
c.Print()
d.Print()

import statistics

class SimpleStatics:
    def __init__(self, list):
        self.list = list

    def __str__(self):
        return(str(self.list))

    def mean(self):
        print(f"Среднее арифметическое: {sum(self.list)/len(self.list)}")

    def median(self):
        print(f"Медиана: {statistics.median(self.list)}")

    def mode(self):
        print(f"Мод: {statistics.mode(self.list)}")

    def Range(self):
        print(f"Выборочная дисперсия: {statistics.variance(self.list)}")

    def standart_deviation(self):
        print(f"Выборочное стандартное отклонение: {statistics.stdev(self.list)}")

class FrequencyDisribution:
    def __init__(self, list):
        self.list = list
        self.x = self.y = 0

    def calculate_frequencies(self):
        for _ in list(set(self.list)):
            print(f"{_}: {self.list.count(_)}")
            if self.list.count(_) > self.x: self.x = self.list.count(_); self.y = _

    def display_frequency_table(self):
        print(f"Список: {self.list}")

    def get_most_frequent(self):
        print(f"чаще всего встречающийся элемент: {self.y}")

a = SimpleStatics([3, 5, 6, 7, 8, 5])
print(f"Список: {a}")
a.mean()
a.median()
a.mode()
a.Range()
a.standart_deviation()

b = FrequencyDisribution([3, 5, 6, 7, 8, 5])
b.calculate_frequencies()
b.display_frequency_table()
b.get_most_frequent()

