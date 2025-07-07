#!/usr/bin/python3

# Связанные списки
# Это последовательность эллеметов данных, которые связаны между собой ссылками
# Каждый элемент хранит в себе данные и ссылку в виде указалеля на другой элемент

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval # Значение первого элемента
        self.nextval = None # Указатель на next

class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self): # Обход списка (печать)
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    def AddBegining(self, newdataval): # Добавление в начало\
        NewNode = Node(newdataval)
        NewNode.nextval = self.headval
        self.headval = NewNode

    def AddEnd(self, newdataval): # Добавление в конец
        NewNode = Node(newdataval)
        if self.headval is None: self.headval = NewNode; return
        last = self.headval
        while (last.nextval is not None): # Проходим по всем ссылкам, пока не равны None
            last = last.nextval # Присваиваем значение следующего элемента
        last.nextval = NewNode # Добавляем новое значение

    def RemoveNode(self, RemoveKey):
        HeadVal = self.headval
        if (HeadVal is not None):
            if (HeadVal.dataval == RemoveKey):
                self.head = HedVal.next
                HeadVal = None
                return
        while (HeadVal is not None):
            if HeadVal.data == RemoveKey:
                break
            prev = HeadVal
            HradVal = HradVal.next
        if (HeadVal == None): return
        prev.next = HeadVal.next
        HeadVal = None

list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
list1.headval.nextval = e2
e2.nextval = e3

list1.listprint()
print()

list1.AddBegining("Fri")
list1.listprint()

print()
list1.AddEnd("Sun")
list1.listprint()


# СТЕК
# Хранит элементы данных таким образом, как куча тарелок хранятся одна за другой на кухне
# Такиим образом стек данных позволяет выполнять операции на одном конце, которые можно назвать вершиной стека (root)
# Реализация ФУНКЦИИ: "ПОСЛЕДНИЙ ПРИШЕЛ ПЕРВЫМ (LIFO)"
# Основные операции  - PUSH and POP
print("###")

class Stack:
    def __init__(self):
        self.stack = []

    def add(self, dataval): # Добавление элементов в стек
        if dataval not in self.stack: self.stack.append(dataval); return True
        else: return False

    def peek(self): # Вызовв вершины списка
        return self.stack[-1]

    def remove(self):
        if len(self.stack) <= 0: return "Стек пуст"
        return self.stack.pop()

    def printlist(self):
        return self.stack

ASTACK = Stack()
ASTACK.add("Mon")
ASTACK.add("Tue")
print(ASTACK.peek())
ASTACK.add("Wed")
ASTACK.add("Tru")
print(ASTACK.peek())
print(ASTACK.remove())
print(ASTACK.remove())
print()
print(ASTACK.printlist())


# ОЧЕРЕДЬ - ПЕРВЫЙ ПРИШЕЛ, ПЕРВЫЙ УШЕЛ (FFO)
# Структура очереди означает то же самое, как и очередь в нашей повседневной жизни
# Уникальность в том, как элементы добавляются и удаляются 

print("###")
class Queue:
    def __init__(self):
        self.queue = list()

    def Addtoq(self, dataval):
        if dataval is not self.queue: # Добавление в очередь
            self.queue.insert(0, dataval)
            return True
        return False

    def Size(self):
        return len(self.queue)

    def remove(self): # Удаление из очереди
        if len(self.queue) > 0: return self.queue.pop()
        return "Очередь пуста!"

TheQueue = Queue()
TheQueue.Addtoq("Moon")
TheQueue.Addtoq("Pen")
TheQueue.Addtoq("Men")
print(TheQueue.Size())
print(TheQueue.queue)
print(f"Удаление: {TheQueue.remove()}")
print(TheQueue.queue)


# ДЕРЕВЬЯ
# Как и списки деревья состоят из узлов. Широко известно бинарное дерево, каждый узел которого содержит ссылки на два других узла
# Эти ссылки указывают на левое и правое поддеревья. Как и узлы связанных списков узлы деревьев также содержат полезые данные.
# Вершину называют КОРНЕМ дерева. Узлы - ВЕТКАМИ. Элементы, не имеющие ссылок - ЛИСТЬЯ
# В зельутате образования, получается родительский узел, от него идут дочерние узлы, а узлы имеющие обзего родителя - сестринские узлы

print("###")

class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo # Данные любого типа
        self.left = left # Указатель на следующий элемент
        self.right= right # Указатель на следующий элемент

    def __str_(self):
        return str(self.cargo)

# Для того, чтобы построить дерево, нужно идти сверху вниз
def total(tree):
    if tree == None: return 0
    return total(tree.left) + total(tree.right) + tree.cargo

left = Tree(2)
right = Tree(3)
tree = Tree(1, left, right)
print(total(tree))
