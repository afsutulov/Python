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
        if self.exists(data):
            print("Число уже есть в списке.")
            return

        new_node = Node(data)
        if not self.head:
            self.head = new_node
            print("Число добавлено.")
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        print("Число добавлено.")

    def exists(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def remove_all(self, data):
        if not self.head:
            print("Список пуст.")
            return

        found = False

        # Удаляем элементы из начала списка
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

        if found: print("Все вхождения числа удалены.")
        else: print("Число не найдено в списке.")

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
                if not replace_all:
                    print("Первое вхождение заменено.")
                    return
            current = current.next

        if found: print("Все вхождения заменены.")
        else: print("Число для замены не найдено.")

def zad1():
    nums_input = input("Введите набор чисел через пробел: ")
    nums = list(map(int, nums_input.split()))
    linked_list = LinkedList()

    for num in nums:
        linked_list.append(num)

    while True:
        print("\nМеню:")
        print("1. Добавить новое число в список")
        print("2. Удалить все вхождения числа из списка")
        print("3. Показать содержимое списка")
        print("4. Проверить есть ли значение в списке")
        print("5. Заменить значение в списке")
        print("6. Выйти")

        choice = input("Выберите пункт меню (1-6): ")

        if choice == "1":
            num = int(input("Введите число для добавления: "))
            linked_list.append(num)

        elif choice == "2":
            num = int(input("Введите число для удаления: "))
            linked_list.remove_all(num)

        elif choice == "3":
            direction = input("Показать с начала или с конца? (введите 'начало' или 'конец'): ")
            reverse = direction.lower() == "конец"
            linked_list.display(reverse)

        elif choice == "4":
            num = int(input("Введите число для проверки: "))
            if linked_list.exists(num):
                print("Число есть в списке.")
            else:
                print("Числа нет в списке.")

        elif choice == "5":
            old_num = int(input("Введите число для замены: "))
            new_num = int(input("Введите новое число: "))
            mode = input("Заменить первое вхождение или все? (введите 'первое' или 'все'): ")
            replace_all = mode.lower() == "все"
            linked_list.replace(old_num, new_num, replace_all)

        elif choice == "6":
            print("Выход из программы.")
            break

        else:
            print("Неверный пункт меню. Попробуйте снова.")

if __name__ == "__main__":
    zad1()
