#!/usr/bin/python3

'''
Паттерны проектирования
Паттерн, это общее решение, многократно используемое в решении проблем , которые часто встречаются в технических проектах, задачах, процессах
Простым языком - паттерн это чертеж.
Классификация:
1. Пораждающий паттерны - преставляют возможность создания контролируемым образом инициализацции и конфигурации объектов, классов и типов данных, исходя из пребумых критериев
2. Структурные паттерны - помогают организовать структуры связанных классов, объектов, типов данных, давая более функциональные возможности
4. Поведенческие паттерны - направлены на выделение общих моделей взаимодействия между объектами

Паттерн 1: Синглтон(одиночка)
'''
'''
Пример неправильного использования (SRP)
class Logger:
    @staticmethod
    def get_instance():
        if "_instance" in Logger.__dict__:
            Logger._instance = Logger()
        return Logger._instance

    def write_log(self, path):
        pass


if __name__ == "__main__":
    s1 = Logger.get_instance()
    s2 = Logger.get_instance()
'''

from threading import Lock, Thread

class Singleton(type):
  _instances = {}
  _lock: Lock = Lock()

  def __call__(cls, *args, **kwargs):
      if cls not in cls._instances:
          instance = super().__call__(*args, **kwargs)
          cls._instances[cls] = instance
      return cls._instances[cls]

class Logger(metaclass=Singleton):
  def __init__(self, name):
      self.name = name

  def write_log(self, path):
      pass

def test_logger(name):
    logger = Logger(name)
    print(logger)

if __name__ == "__main__":
  #logger1 = Logger()
  #logger2 = Logger()
  #print(logger1,'\n', logger2)
  #assert logger1 is logger2
  proccess1 = Thread(target=test_logger, args=("FOO",))
  proccess2 = Thread(target=test_logger, args=("BAR",))
  proccess2.start()
  proccess1.start()

'''
Особенности:
1. Красс имеет только один экземпляр
2. Вы получаете глобальную точку доступа к этому экземпляру
3. Синглтон инициализирует только при первом запросе
4. Маскирует плохой дизайн до определенного времени.
Одна из причин, почему многие считают сингтон антипаттерном.
'''

'''
Паттерн 2: Декоратр
Это структурный паттерн, цель которого - предоставление новых функциональных возможностей классам и объектам во время выполнения кода.
Чаще всего декоратор представляет из себя абстрактный класс, принимающий в констркуторе объект, функционального которого мы хотим расширить.
'''

from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod

    def operation(self):
        pass

class ConcreteComponent(Component):
        def operation(self):
            return "ConcerteComponent)"

class Decorator(Component):
        def __init__(self, component):
            self.component = component

        def opetion(self):
            pass

class ConcreateDecorationA(Decorator):
        def operation(self):
            return f"ConcreateDecoration({self.component.operation()})"

class ConcreateDecorationB(Decorator):
        def operation(self):
            return f"ConcreateDecoration({self.component.operation()})"

if __name__ == "__main__":
    concreteComponent = ConcreteComponent()
    print(concreteComponent)
    decoratorA = ConcreateDecorationA(concreteComponent)
    decoratorB = ConcreateDecorationB(concreteComponent)
    print(decoratorB.operation())

'''
Возможности декоратора:
1. Расширение поведения объекта без создания подкласса
2. Добавление или удаление обязанностей объекта во время выполнения работы программы
3. Объединение нескольких моделей поведения, путем применения к ообъекту нескольких декораторов
4. Разделение монолитного класса, который реализует множество вариантов на более мелкие классы
5. Применение одной конкретной обертки из центра стека
6. Реализация декоратора, при исключении его зависимости от порядка, в котором обертки уложены в стек
'''

# Практический пример использования декоратора - зранение кэша функции для рекурсии

import sys

def memoize(f):
    cach = dict()
    def wrapper(x):
        if x not in cach: cach[x] = f(x)
        return cach[x]
    return wrapper

@memoize
def fib(n):
    if n <= 1: return n
    else: return fib(n-1) + fib(n-2)

if __name__ == "__main__":
    sys.setrecursionlimit(2000)
    print(fib(750))


'''
Паттерн 3 - Итератор
Это поведенческий паттерн. Его цель - позволить вам обходить элементы коллекции, не раскрывая ее базовое представление.
Чтобы его реализовать, можно воспользоваться двумя вариантами:
1. Реализовать в классе специальые методы __iter__ __next__
2, Пспользовать генераторы
Пример: создание пользовательской коллекции с итератором алфамитного порядка
'''

from collections.abc import Iterator, Iterable

class AlphabeticalObderIterator(Iterator):
    _position: int = None
    _reverse: bool = False

    def __init__(self, collection, reverse = False):
        self._colection = sorted(collection)
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        try:
            value = self._colection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()
        return value

class WordsCollection(Iterable):
    def __init__(self, collection):
        self._collection = collection

    def __iter__(self):
        return AlphabeticalObderIterator(self._collection)

    def get_reverse_iterator(self):
        return AlphabeticalObderIterator(self._collection, True)

if __name__ == "__main__":
    wordsCollection = WordsCollection(["Thurd", "First", "Second"])
    print(list(wordsCollection))
    print(list(wordsCollection.get_reverse_iterator()))


# Работа с генератором

def prime_generator():
    yield 2
    primes = [2]
    to_check = 3
    while True:
        sqrt = to_check ** 0.5
        is_prime = True
        for prime in primes:
            if prime > sqrt: break
            if to_check % prime == 0: is_prime = False; break
        if is_prime:
            primes.append(to_check)
            yield to_check
        to_check += 2

generator = prime_generator()
print([next(generator) for i in range(20)])
