#!/usr/bin/python3

#6. Приспособленец (Flyweight)
class CharacterStyle:
    def __init__(self, font, size, color):
        self.font = font
        self.size = size
        self.color = color

    def __str__(self):
        return f'Font: {self.font}, Size: {self.size}, Color: {self.color}'

class CharacterStyleFactory:
    _styles = {}

    @classmethod
    def get_style(cls, font, size, color):
        key = (font, size, color)
        if key not in cls._styles: cls._styles[key] = CharacterStyle(font, size, color)
        return cls._styles[key]

class TextEditor:
    def __init__(self):
        self.text = ""
        self.styles = []

    def set_text(self, text):
        self.text = text
        self.styles = [None] * len(text)

    def __str__(self):
        return self.text

    def apply_style(self, position, style_key):
        self.styles[position] = style_key

    def render(self):
        output = []
        for char, style in zip(self.text, self.styles):
            if style is None: output.append(f'{char}')
            else: output.append(f'[{style}] {char}')
        for _ in output: print(_)


#5. Фасад (Facade)
class InventorySystem:
    def check_availability(self, product_id):
        print(f"Проверяю наличие продукта: {product_id}")
        return True

class PaymentSystem:
    def process_payment(self, amount):
        print(f"Обрабатываю платеж на сумму: {amount}$")
        return True

class ShippingSystem:
    def ship_product(self, address):
        print(f"Отправляю продукт по адресу: {address}")
        return True

class NotificationSystem:
    def send_notification(self, email):
        print(f"Уведомляю клиента по электронной почте: {email}")
        return True

class OrderFacade:
    def __init__(self):
        self.inventory_system = InventorySystem()
        self.payment_system = PaymentSystem()
        self.shipping_system = ShippingSystem()
        self.notification_system = NotificationSystem()

    def place_order(self, product_id, amount, delivery_address, customer_email):
        available = self.inventory_system.check_availability(product_id)
        if not available:
            print("Извините, товар временно отсутствует.")
            return False

        payment_success = self.payment_system.process_payment(amount)
        if not payment_success:
            print("Ошибка обработки платежа.")
            return False

        shipping_success = self.shipping_system.ship_product(delivery_address)
        if not shipping_success:
            print("Возникла проблема с доставкой.")
            return False

        notification_sent = self.notification_system.send_notification(customer_email)
        if not notification_sent:
            print("Проблемы с уведомлением.")
            return False

        print("Заказ успешно размещён.")
        return True


#4. Декоратор (Decorator)
from abc import ABC, abstractmethod
class Coffee(ABC):
    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def description(self):
        pass

class SimpleCoffee(Coffee):
    def cost(self):
        return 10

    def description(self):
        return "Простой кофе"

class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost()

    def description(self):
        return self.coffee.description()

class Milk(CoffeeDecorator):
    def cost(self):
        return self.coffee.cost() + 2

    def description(self):
        return self.coffee.description() + ", с молоком"

class Sugar(CoffeeDecorator):
    def cost(self):
        return self.coffee.cost() + 1

    def description(self):
        return self.coffee.description() + ", с сахаром"

class Chocolate(CoffeeDecorator):
    def cost(self):
        return self.coffee.cost() + 3

    def description(self):
        return self.coffee.description() + ", с шоколадом"


#3. Компоновщик (Composite)
class OrganizationComponent(ABC):
    @abstractmethod
    def display_details(self, indentation=""):
        pass

class Employee(OrganizationComponent):
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def display_details(self, indentation=""):
        print(f"{indentation}{self.name} ({self.position})")

class Department(OrganizationComponent):
    def __init__(self, name):
        self.name = name
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def remove_component(self, component):
        self.components.remove(component)

    def display_details(self, indentation=""):
        print(indentation + self.name)
        for component in self.components: component.display_details(indentation + "  ")


#2. Мост (Bridge)
class Renderer(ABC):
    @abstractmethod
    def render_circle(self, x, y, radius):
        pass

class VectorRenderer(Renderer):
    def render_circle(self, x, y, radius):
        print(f"Векторное изображение круга радиусом {radius} в координатах ({x}, {y}).")

class RasterRenderer(Renderer):
    def render_circle(self, x, y, radius):
        print(f"Растровое изображение круга радиусом {radius} в координатах ({x}, {y}).")

class Shape(ABC):
    def __init__(self, renderer):
        self.renderer = renderer

    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def __init__(self, x, y, radius, renderer):
        super().__init__(renderer)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        self.renderer.render_circle(self.x, self.y, self.radius)


#1. Адаптер (Adapter)
import json
class LegacyLogger:
    def log_message(self, message):
        print(f"[Legacy Log]: {message}")

class NewMonitor:
    def send_json_log(self, json_data):
        print(f"[New Monitor]: Получил JSON лог: {json_data}")

class LoggerAdapter:
    def __init__(self, legacy_logger, new_monitor):
        self.legacy_logger = legacy_logger
        self.new_monitor = new_monitor

    def log_and_send(self, message):
        self.legacy_logger.log_message(message)
        json_data = {"type": "info", "message": message}
        self.new_monitor.send_json_log(json.dumps(json_data, ensure_ascii=False))

if __name__ == "__main__":
    print("ЗАДАНИЕ 6: Приспособленец (Flyweight)")
    factory = CharacterStyleFactory()
    editor = TextEditor()
    editor.set_text("Всем привет!")
    print(f"Начальный текст: {editor}\nОтформатированный текст (задан шрифт каждой букве):")
    for _ in range(len(editor.text)):
        if _ % 2 == 0: style = factory.get_style("Arial", 18, "Blue")
        else: style = factory.get_style("Times New Roman", 24, "Red")
        editor.apply_style(_, style)
    editor.render()

    print("\nЗАДАНИЕ 5: Фасад (Facade)")
    facade = OrderFacade()
    result = facade.place_order(
        product_id="ABC123",
        amount=50.0,
        delivery_address="г. Пермь, ул. Революции 13",
        customer_email="example@example.com"
    )
    if result: print("Ваш заказ принят и обрабатывается")
    else: print("К сожалению, возникли проблемы с вашим заказом")

    print("\nЗАДАНИЕ 4: Декоратор (Decorator)")
    simple_coffee = SimpleCoffee()
    print(f"{simple_coffee.description()}: ${simple_coffee.cost()}")
    milk_and_sugar_coffee = Milk(Sugar(simple_coffee))
    print(f"{milk_and_sugar_coffee.description()}: ${milk_and_sugar_coffee.cost()}")
    chocolate_milk_and_sugar_coffee = Chocolate(Milk(Sugar(simple_coffee)))
    print(f"{chocolate_milk_and_sugar_coffee.description()}: ${chocolate_milk_and_sugar_coffee.cost()}")

    print("\nЗАДАНИЕ 3: Компоновщик (Composite)")
    ceo = Employee("Иван Петров", "CEO")
    cto = Employee("Сергей Иванов", "CTO")
    developer = Employee("Алексей Смирнов", "Разработчик")
    qa_engineer = Employee("Ольга Кузнецова", "QA-инженер")
    it_department = Department("IT-отдел")
    it_department.add_component(developer)
    it_department.add_component(qa_engineer)
    hr_department = Department("HR-отдел")
    hr_manager = Employee("Елена Васильева", "Менеджер HR")
    hr_department.add_component(hr_manager)
    company = Department("Компания ТОР")
    company.add_component(it_department)
    company.add_component(hr_department)
    company.add_component(cto)
    company.add_component(ceo)
    company.display_details()

    print("\nЗАДАНИЕ 2: Мост (Bridge)")
    vector_renderer = VectorRenderer()
    raster_renderer = RasterRenderer()
    circle_vector = Circle(x=10, y=10, radius=5, renderer=vector_renderer)
    circle_raster = Circle(x=10, y=10, radius=5, renderer=raster_renderer)
    circle_vector.draw()
    circle_raster.draw()

    print("\nЗАДАНИЕ 1: Адаптер (Adapter)")
    old_logger = LegacyLogger()
    monitor = NewMonitor()
    adapter = LoggerAdapter(old_logger, monitor)
    adapter.log_and_send("Тестовое сообщение")
