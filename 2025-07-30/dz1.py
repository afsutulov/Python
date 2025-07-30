#!/usr/bin/python3

from abc import ABC, abstractmethod

# 1. Factory Method
class Document(ABC):
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def close(self):
        pass

class PdfDocument(Document):
    def open(self):
        print("PDF-документ открыт")

    def close(self):
        print("PDF-документ закрыт")

class HtmlDocument(Document):
    def open(self):
        print("HTML-документ открыт")

    def close(self):
        print("HTML-документ закрыт")

class DocumentFactory(ABC):
    @abstractmethod
    def create_document(self):
        pass

class PdfDocumentFactory(DocumentFactory):
    def create_document(self):
        return PdfDocument()

class HtmlDocumentFactory(DocumentFactory):
    def create_document(self):
        return HtmlDocument()

def FactoryMethod():
    pdf_factory = PdfDocumentFactory()
    html_factory = HtmlDocumentFactory()
    pdf_doc = pdf_factory.create_document()
    html_doc = html_factory.create_document()
    pdf_doc.open()
    html_doc.open()
    pdf_doc.close()
    html_doc.close()

# 2. Abstract Factory
class Button(ABC):
    @abstractmethod
    def render(self):
        pass

class TextBox(ABC):
    @abstractmethod
    def render(self):
        pass

class WindowsButton(Button):
    def render(self):
        print("Отрисована кнопка в стиле Windows")

class WindowsTextBox(TextBox):
    def render(self):
        print("Отрисовано текстовое поле в стиле Windows")

class MacButton(Button):
    def render(self):
        print("Отрисована кнопка в стиле macOS")

class MacTextBox(TextBox):
    def render(self):
        print("Отрисовано текстовое поле в стиле macOS")

class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_textbox(self):
        pass

class WindowsGUIFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_textbox(self):
        return WindowsTextBox()

class MacGUIFactory(GUIFactory):
    def create_button(self):
        return MacButton()

    def create_textbox(self):
        return MacTextBox()

def AbstractFactory(factory):
    button = factory.create_button()
    textbox = factory.create_textbox()
    button.render()
    textbox.render()

#3. Builder
class Pizza:
    def __init__(self):
        self.dough = None
        self.sauce = None
        self.topping = []

    def set_dough(self, dough):
        self.dough = dough

    def set_sauce(self, sauce):
        self.sauce = sauce

    def add_topping(self, topping):
        self.topping.append(topping)

    def __repr__(self):
        return f"\tСостав:\n\t\tТесто: {self.dough}\n\t\tСоус: {self.sauce}\n\t\tНачинка: {', '.join(self.topping)}"

class PizzaBuilder(ABC):
    def __init__(self):
        self.pizza = Pizza()

    @abstractmethod
    def build_dough(self):
        pass

    @abstractmethod
    def build_sauce(self):
        pass

    @abstractmethod
    def build_topping(self):
        pass

    def get_pizza(self):
        return self.pizza

class MargheritaBuilder(PizzaBuilder):
    def build_dough(self):
        self.pizza.set_dough("Тонкая тесто")

    def build_sauce(self):
        self.pizza.set_sauce("Томатный соус")

    def build_topping(self):
        self.pizza.add_topping("Сыр")
        self.pizza.add_topping("Свежий базилик")

class SpicyPizzaBuilder(PizzaBuilder):
    def build_dough(self):
        self.pizza.set_dough("Толстое тесто")

    def build_sauce(self):
        self.pizza.set_sauce("Острый соус чили")

    def build_topping(self):
        self.pizza.add_topping("Перец халапеньо")
        self.pizza.add_topping("Колбаса")

class Waiter:
    def construct_pizza(self, builder):
        builder.build_dough()
        builder.build_sauce()
        builder.build_topping()
        return builder.get_pizza()

#4. Prototype
import copy
class Shape:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def clone(self):
        return copy.deepcopy(self)

    def info(self):
        return f"{type(self).__name__}: X={self.x}, Y={self.y}, Цвет={self.color}"

class Rectangle(Shape):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, color)
        self.width = width
        self.height = height

    def info(self):
        base_info = super().info()
        return f"{base_info}, Ширина={self.width}, Высота={self.height}"

class Circle(Shape):
    def __init__(self, x, y, radius, color):
        super().__init__(x, y, color)
        self.radius = radius

    def info(self):
        base_info = super().info()
        return f"{base_info}, Радиус={self.radius}"

#5. Object Pool
import threading

class ReusableObject:
    def __init__(self, object_id):
        self.id = object_id
        self.in_use = False

    def use(self):
        print(f"Используется объект {self.id}")

    def free(self):
        print(f"Освобождается объект {self.id}")

class ObjectPool:
    def __init__(self, initial_size=5):
        self.pool = []
        self.lock = threading.Lock()
        self.next_id = 1

        # Инициализируем пул объектами
        for _ in range(initial_size):
            obj = ReusableObject(self.next_id)
            self.pool.append(obj)
            self.next_id += 1

    def acquire(self):
        with self.lock:
            if len(self.pool) > 0:
                obj = self.pool.pop(0)
                obj.in_use = True
                return obj
            else:
                new_obj = ReusableObject(self.next_id)
                self.next_id += 1
                new_obj.in_use = True
                return new_obj

    def release(self, obj):
        with self.lock:
            obj.free()
            obj.in_use = False
            self.pool.append(obj)

def worker(pool, num_iterations):
    for _ in range(num_iterations):
        obj = pool.acquire()
        obj.use()
        pool.release(obj)

if __name__ == "__main__":
    print("ЗАДАНИЕ 1: Factroy Methon")
    FactoryMethod()

    print("\nЗАДАНИЕ 2: Factroy Methon")
    windows_factory = WindowsGUIFactory()
    mac_factory = MacGUIFactory()
    print("Создание элементов интерфейса в стиле Windows:")
    AbstractFactory(windows_factory)
    print("\nСоздание элементов интерфейса в стиле macOS:")
    AbstractFactory(mac_factory)

    print("\nЗАДАНИЕ 3: Builder")
    waiter = Waiter()
    margherita_builder = MargheritaBuilder()
    pizza_margherita = waiter.construct_pizza(margherita_builder)
    print(f"ПИЦА МАРГАРИТА\n{pizza_margherita}")
    spicy_builder = SpicyPizzaBuilder()
    pizza_spicy = waiter.construct_pizza(spicy_builder)
    print(f"ОСТРАЯ ПИЦА\n{pizza_spicy}")

    print("\nЗАДАНИЕ 4: Prototype")
    rectangle_proto = Rectangle(x=10, y=20, width=50, height=30, color="Синий")
    circle_proto = Circle(x=15, y=25, radius=10, color="Красный")
    # Клонируем прямоугольник
    cloned_rectangle = rectangle_proto.clone()
    cloned_rectangle.x += 100
    cloned_rectangle.color = "Зеленый"
    # Клонируем круг
    cloned_circle = circle_proto.clone()
    cloned_circle.radius *= 2
    cloned_circle.color = "Желтый"
    # Проверяем независимость клонов
    print(rectangle_proto.info())
    print(cloned_rectangle.info())
    print(circle_proto.info())
    print(cloned_circle.info())

    print("\nЗАДАНИЕ 5: Object Poole")
    pool = ObjectPool(initial_size=3)
    threads = [
        threading.Thread(target=worker, args=(pool, 5)),
        threading.Thread(target=worker, args=(pool, 7)),
        threading.Thread(target=worker, args=(pool, 3))
    ]
    for thread in threads: thread.start()
    for thread in threads: thread.join()
    print("Все потоки завершены")
