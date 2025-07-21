#!/usr/bin/python3

#1. Простой декоратор функции:
def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@uppercase_decorator
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    print("1. Простой декоратор функции:")
    print(greet("John"))


#2. Декоратор с параметрами:
import random

def repeat(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(num_times):
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator

@repeat(3)
def get_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    print("\n2. Декоратор с параметрами:")
    print(get_random_number())


#3. Декоратор класса:
class MyClass:
    pass

def new_method(self):
    print("Новый метод успешно добавлен!")

def add_method(method):
    def decorator(cls):
        setattr(cls, method.__name__, method)
        return cls
    return decorator

@add_method(new_method)
class MyClass:
    pass

if __name__ == "__main__":
    print("\n3. Декоратор класса:")
    obj = MyClass()
    obj.new_method()


#4. Декоратор с сохранением метаданных:
import time, functools

def timer_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Функция {func.__name__} выполнена за {end - start:.4f} секунд.")
        return result
    return wrapper

@timer_decorator
def my_function(a: int, b: int) -> int:
    time.sleep(0.1)
    return a + b

if __name__ == "__main__":
    print("\n4. Декоратор с сохранением метаданных:")
    result = my_function(3, 4)
    print("Результат: {result}\nПроверка метаданных")
    print("\tИмя функции:", my_function.__name__)
    print("\tDocstring:", my_function.__doc__)
    print("\tАннотации:", my_function.__annotations__)


#5. Декоратор для проверки аргументов функции:
import inspect

def validate_arguments(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()

        for name, value in bound_args.arguments.items():
            expected_type = func.__annotations__.get(name)
            if expected_type and not isinstance(value, expected_type):
                return    f"Аргумент '{name}' должен быть типа {expected_type.__name__}, а получил {type(value).__name__}"
        return func(*args, **kwargs)
    return wrapper

@validate_arguments
def calculate_sum(a: int, b: int) -> int:
    return a + b

if __name__ == "__main__":
    print("\n5. Декоратор для проверки аргументов функции:")
    print("Верный вызов:")
    print(calculate_sum(1, 2))
    print("\nНеверный вызов:")
    print(calculate_sum(1, "2"))


#6. Цепочка декораторов:
def add_exclamation(func):
    def wrapper():
        return func() + "!"
    return wrapper

def add_question(func):
    def wrapper():
        return func() + "?"
    return wrapper

@add_question
@add_exclamation
def my_string():
    return "Это строка"

if __name__ == "__main__":
    print("\n6. Цепочка декораторов:")
    result = my_string()
    print(result)


#7. Декоратор как класс:
class LogCalls:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        arg_strs = [repr(a) for a in args]
        kwarg_strs = [f"{k}={v!r}" for k, v in kwargs.items()]
        all_args = ", ".join(arg_strs + kwarg_strs)
        print(f"Вызов {self.func.__name__}({all_args})")
        return self.func(*args, **kwargs)

@LogCalls
def greet(name, punctuation="!"):
    return f"Hello, {name}{punctuation}"

if __name__ == "__main__":
    print("\n7. Декоратор как класс:")
    print(greet("Alice"))
    print(greet("Bob", punctuation="?"))


#8. Паттерн Wrapper для расширения функциональности объекта:
class TextInput:
    def __init__(self, text: str):
        self._text = text

    def get_value(self) -> str:
        return self._text

class HtmlEncodeDecorator:
    def __init__(self, component):
        self._component = component

    def get_value(self) -> str:
        text = self._component.get_value()
        return (
            text.replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
        )

class TrimDecorator:
    def __init__(self, component):
        self._component = component

    def get_value(self) -> str:
        text = self._component.get_value()
        return text.strip()

if __name__ == "__main__":
    print("\n8. Паттерн Wrapper для расширения функциональности объекта:")
    raw_input = TextInput("   <b>Hello & welcome>   ")
    decorated_input = HtmlEncodeDecorator(TrimDecorator(raw_input))
    result = decorated_input.get_value()
    print(result)

