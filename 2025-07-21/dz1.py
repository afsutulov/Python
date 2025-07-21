#!/usr/bin/python3

# Практика 1 - Singleton
#1. Базовый Singleton:
class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    def log(self, message):
        print(message)

def function_one():
    logger1 = Logger()
    logger1.log("Сообщение из function_one")
    print(f"ID logger1: {id(logger1)}")

def function_two():
    logger2 = Logger()
    logger2.log("Сообщение из function_two")
    print(f"ID logger2: {id(logger2)}")

class SomeClass:
    def do_something(self):
        logger3 = Logger()
        logger3.log("Сообщение из SomeClass")
        print(f"ID logger3: {id(logger3)}")

if __name__ == "__main__":
    print("1. Базовый Singleton:")
    function_one()
    function_two()
    some_instance = SomeClass()
    some_instance.do_something()


# 2. Singleton с параметрами:
class Logger:
    _instance = None
    _initialized = False

    def __new__(cls, filename=None):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    def __init__(self, filename=None):
        if not Logger._initialized:
            self._filename = filename
            Logger._initialized = True

    def log(self, message):
        print(message)

    def get_filename(self):
        return self._filename

if __name__ == "__main__":
    print("\n2. Singleton с параметрами:")
    logger1 = Logger(filename="log1.txt")
    print("Logger1 filename:", logger1.get_filename())
    logger2 = Logger(filename="log2.txt")
    print("Logger2 filename:", logger2.get_filename())
    print("logger1 is logger2:", logger1 is logger2)

#3. Singleton с многопоточностью (усложненный):
import threading, time

class DatabaseConnection:
    _instance = None
    _lock = threading.Lock()
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(DatabaseConnection, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        with DatabaseConnection._lock:
            if not DatabaseConnection._initialized:
                self.connection = self._connect_to_database()
                DatabaseConnection._initialized = True

    def _connect_to_database(self):
        # Эмуляция подключения (например, через sleep)
        time.sleep(0.1)
        return "DB_CONNECTION_OBJECT"

    def query(self, sql):
        print(f"[{threading.current_thread().name}] Выполняется запрос: {sql} на {self.connection}")

def access_database():
    db = DatabaseConnection()
    db.query("SELECT * FROM users")
    print(f"[{threading.current_thread().name}] ID экземпляра: {id(db)}")


if __name__ == "__main__":
    print("\n3. Singleton с многопоточностью (усложненный):")
    threads = []
    for i in range(5):
        t = threading.Thread(target=access_database, name=f"Thread-{i+1}")
        threads.append(t)
        t.start()
    for t in threads: t.join()


#4. Singleton с декоратором (альтернативный подход):
def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

@singleton
class Configuration:
    def __init__(self):
        self._settings = {}

    def set(self, key, value):
        self._settings[key] = value

    def get(self, key, default=None):
        return self._settings.get(key, default)

    def all_settings(self):
        return dict(self._settings)

if __name__ == "__main__":
    print("\n4. Singleton с декоратором (альтернативный подход):")
    # Создание первого экземпляра и установка настроек
    config1 = Configuration()
    config1.set("theme", "dark")
    config1.set("language", "en")
    # Попытка создать второй экземпляр
    config2 = Configuration()
    config2.set("timezone", "UTC")
    # Проверка, что config1 и config2 — это один и тот же объект
    print("config1 is config2:", config1 is config2)
    # Вывод всех настроек через config2
    print("All settings from config2:", config2.all_settings())
    # Проверка отдельных значений
    print("Theme from config1:", config1.get("theme"))
    print("Timezone from config1:", config1.get("timezone"))


#5. Singleton с использованием метакласса (самый сложный):
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Settings(metaclass=SingletonMeta):
    def __init__(self):
        self._config = {}

    def set(self, key, value):
        self._config[key] = value

    def get(self, key, default=None):
        return self._config.get(key, default)

    def all(self):
        return dict(self._config)

if __name__ == "__main__":
    print("\n5. Singleton с использованием метакласса (самый сложный):")
    # Создание первого экземпляра
    s1 = Settings()
    s1.set("debug", True)
    s1.set("log_level", "INFO")
    # Попытка создать второй экземпляр
    s2 = Settings()
    s2.set("timezone", "Europe/Moscow")
    # Проверка, что s1 и s2 — один и тот же объект
    print("s1 is s2:", s1 is s2)
    # Вывод всех настроек
    print("All settings from s2:", s2.all())
    print("Debug mode:", s1.get("debug"))
    print("Timezone:", s1.get("timezone"))


#6. Singleton с контекстным менеджером (для управления ресурсами):
class ResourceManager:
    _instance = None
    _resource = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(ResourceManager, cls).__new__(cls)
        return cls._instance

    def __init__(self, filename="resource.txt"):
        if not hasattr(self, "_initialized"):
            self._filename = filename
            self._initialized = True

    def __enter__(self):
        print(f"[ENTER] Открытие ресурса: {self._filename}")
        self._resource = open(self._filename, "w")
        return self._resource

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("[EXIT] Закрытие ресурса")
        if self._resource:
            self._resource.close()
            self._resource = None

if __name__ == "__main__":
    print("\n6. Singleton с контекстным менеджером (для управления ресурсами):")
    # Используем ResourceManager как контекстный менеджер
    with ResourceManager("my_log.txt") as f: f.write("Лог: ресурс открыт и используется\n")
    # Вне блока with: создаём другой "экземпляр"
    rm1 = ResourceManager("another.txt")
    rm2 = ResourceManager("ignored.txt")
    print("\nПроверка Singleton:")
    print("rm1 is rm2:", rm1 is rm2)
    print("Файл, указанный при первом создании:", rm1._filename)
    print("Файл, указанный при втором вызове (игнорируется):", rm2._filename)
