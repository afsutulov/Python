#!/usr/bin/python3

# Классы для Задания 1
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head: self.head = new_node; return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def exists(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def remove_all(self, data):
        if not self.head: print("Список пуст"); return
        found = False
        while self.head and self.head.data == data:
            self.head = self.head.next
            found = True
        current = self.head
        prev = None
        while current:
            if current.data == data:
                prev.next = current.next
                found = True
            else:
                prev = current
            current = current.next
        if found: print("Все вхождения числа удалены")
        else: print("Число не найдено в списке")

    def display(self, reverse=False):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        if reverse:
            elements.reverse()
        print(elements)

    def replace(self, old_data, new_data, replace_all=False):
        current = self.head
        found = False
        while current:
            if current.data == old_data:
                current.data = new_data
                found = True
                if not replace_all: print("Первое вхождение заменено"); return
            current = current.next
        if found: print("Все вхождения заменены")
        else: print("Число для замены не найдено")

def Num(txt, n1, n2):
    _ = input(f'{txt}: ')
    if _.isnumeric() and n1 <= int(_) <=n2: return int(_)
    else: print(f'Ошибка ввода! Необходимо ввести число от {n1} до {n2}!\n'); return Num(txt, n1, n2)

def zad1():
    print("ЗАДАНИЕ 1: ")
    linked_list = LinkedList()
    while True:
        _ = Num("Введите число (0 - завершение ввода)", 0, 100000)
        if _ == 0: break
        linked_list.append(_)
    while True:
        match Num("\nВыбыр:\n\t1. Добавить новое число в список\n\t2. Удалить все вхождения числа из списка\n\t3. Показать содержимое списка\n\t4. Проверить есть ли значение в списке\n\t5. Заменить значение в списке\n\t0. Выйти\nВаш выбор", 0, 5):
            case 0: break
            case 1: linked_list.append(Num("Введите число для добавления", 0, 100000))
            case 2: linked_list.remove_all(Num("Введите число для удаления", 0, 100000))
            case 3: 
                match Num("1. Показать с начала\n2. Показать с конца\nВаш выбор", 1, 2):
                    case 1: linked_list.display(True)
                    case 2: linked_list.display(False)
            case 4:
                if linked_list.exists(Num("Введите число для проверки", 0, 100000)): print("Число есть в списке")
                else: print("Числа нет в списке")
            case 5:
                old_num = Num("Введите число для замены", 0, 100000)
                new_num = Num("Введите новое число", 0, 100000)
                match Num("1. Заменить первое вхождение\n2. Заменить все\nВаш выбор", 1, 2):
                    case 1: linked_list.replace(old_num, new_num, False)
                    case 2: linked_list.replace(old_num, new_num, True)

# Класс для Задания 2
class StringStack:
    def __init__(self, max_size=0, flag=True):
        self.stack = []
        self.max_size = max_size
        self.flag = flag

    def push(self, string):
        if self.flag and self.is_full(): print("Стек заполнен. Нельзя добавить новую строку")
        else: self.stack.append(string); print("Строка добавлена в стек")

    def pop(self):
        if self.is_empty(): print("Стек пуст. Нечего удалить")
        else: removed = self.stack.pop(); print(f"Удалена строка: {removed}")

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) >= self.max_size

    def clear(self):
        self.stack.clear()
        print("Стек очищен")

    def peek(self):
        if self.is_empty(): print("Стек пуст.")
        else: print(f"Верхняя строка: {self.stack[-1]}")

def zad2(flag):
    if flag: string_stack = StringStack(Num("Введите максимальный размер стека", 0, 1000), flag)
    else: string_stack = StringStack(0, flag)
    while True:
        match Num("Выбор:\n\t1. Поместить строку в стек\n\t2. Вытолкнуть строку из стека\n\t3. Подсчитать количество строк в стеке\n\t4. Проверить, пуст ли стек\n\t5. Проверить, заполнен ли стек\n\t6. Очистить стек\n\t7. Получить верхнюю строку без удаления\n\t0. Выйти\nВаш выбор", 0, 7):
            case 0: break
            case 1: string_stack.push(input("Введите строку для добавления: "))
            case 2: string_stack.pop()
            case 3: print(f"Количество строк в стеке: {string_stack.size()}")
            case 4:
                if string_stack.is_empty(): print("Стек пуст")
                else: print("Стек не пуст")
            case 5:
                if string_stack.is_full(): print("Стек заполнен")
                else: print("Стек не заполнен")
            case 6: string_stack.clear()
            case 7: string_stack.peek()

if __name__ == "__main__":
    zad1()
    zad2(True)
    zad2(False) # Задание 3 - нефиксированный размер стека
