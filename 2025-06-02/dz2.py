#!/usr/bin/python3

import math

# Классы для задания 1 и 2
class Figura:
    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2

    def Square(self):
        return self.l1 * self.l2

    def __int__(self):
        return int(self.Square())

class Pryamug(Figura):
    def __str__(self):
        return "Прямоугольник"

class Krug(Figura):
    def __init__(self, l1):
        self.l1 = l1

    def Square(self):
        return math.pi * self.l1 ** 2

    def __str__(self):
        return "Круг"

class Treug(Figura):
    def Sqyare(self):
        return self.l1 * self.l2 / 2

    def __str__(self):
        return "Треугольник"

class Trap(Figura):
    def __init__(self, l1, l2, l3):
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3

    def Square(self):
        return 1/2 * (self.l1 + self.l2) * self.l3

    def __str__(self):
        return "Трапеция"

# Задание 3
class Shape:
    def __init__(self):
        self.figa = ""

    def Num(self, txt, n1, n2):
        self.txt = txt
        self.n1 = n1
        self.n2 = n2
        _ = input(f'{self.txt}: ')
        if _.isnumeric() and self.n1 <= int(_) <= self.n2: return int(_)
        else: print(f'Ошибка ввода! Необходимо ввести число от {n1} до {n2}!\n'); return self.Num(txt, n1, n2)

    def Menu(self):
        while True:
            match self.Num("Действия:\n\t1. Показать фигуру\n\t2. Сохранить фигуру в файл\n\t3. Загрузить фигуру из файла\n\t4. Нарисовать квадрат\n\t5. Нарисовать прямоугольник\n\t6. Нарисовать окружность\n\t7. Нарисовать эллипс\n\t0. Выход\nВыберите действие", 0, 7):
                case 1: self.Show()
                case 2: self.Save()
                case 3: self.Load()
                case 4: self.figa = Square().Add(True)
                case 5: self.figa = Rectangle().Add(False)
                case 6: self.figa = Circle().Add()
                case 7: self.figa = Ellipse().Add()
                case 0: break

    def Show(self):
        print(self.figa)

    def Save(self):
        with open('dz2.txt', 'w') as f: f.write(self.figa)
        print("Фигура сохранена в файл: dz2.txt!\n")

    def Load(self):
        with open("dz2.txt", 'r') as f: self.figa += f.read()
        print("Фигура загружена из файла: dz2.txt!\n")

class Square(Shape):
    def __init__(self):
        Shape.__init__(self)

    def Add(self, flag):
        x0 = self.Num("Введите координату X левого верхнего угла (1-20)", 1, 20)
        y0 = self.Num("Введите координату Y левого верхнего угла (1-20)", 1, 20)
        if flag: w = h = self.Num("Введите длинну стороны квадрата (1-50)", 1, 50)
        else:
            w = self.Num("Введите ширину прямоугольника (1-50)", 1, 50)
            h = self.Num("Введите высоту прямоугольника (1-50)", 1, 50)
        width = x0 + w
        height = y0 + h
        figa = ""
        for x in range(height):
            for y in range(width):
                if (x == x0 and y >= y0) or (y == y0 and x >= x0) or (x == height - 1 and y >= y0) or (y == width - 1 and x >= x0): figa += "*"
                else: figa += " "
            figa += "\n"
        return figa

class Rectangle(Square):
    pass

class Circle(Shape):
    def __init__(self):
        Shape.__init__(self)

    def Add(self):
        center_x = self.Num("Введите координату X центра круга (1-20)", 1, 20)
        center_y = self.Num("Введите координату Y центра круга (1-20)", 1, 20)
        radius = self.Num("Введите радиус (1-20)", 1, 20)
        width = center_x + radius * 2
        height = center_y + radius * 2
        figa = ""
        for y in range(height):
            for x in range(width):
                dist = math.sqrt((x - center_x)**2 + (y - center_y)**2)
                if abs(dist - radius) < 0.5: figa += "*"
                else: figa += " "
            figa += "\n"
        return figa

class Ellipse(Shape):
    def __init__(self):
        Shape.__init__(self)

    def Add(self):
        x0 = self.Num("Введите координату X левого верхнего угла (1-20)", 1, 20)
        y0 = self.Num("Введите координату Y левого верхнего угла (1-20)", 1, 20)
        w = self.Num("Введите ширину прямугольника вокруг эллипса (1-70)", 1, 70)
        h = self.Num("Введите высоту прямугольника вокруг эллипса (1-30)", 1, 30)
        cx = x0 + w / 2
        cy = y0 + h / 2
        a = w / 2
        b = h / 2
        width = x0 + w + 2
        height = y0 + h + 2
        figa = ""
        for y in range(height):
            for x in range(width):
                dy = (y - cy) * (a / b)
                dx = x - cx
                if abs(dx**2 / a**2 + dy**2 / a**2 - 1) < 0.1: figa += "*"
                else: figa += " "
            figa += "\n"
        return figa

def main():
    print(f"ЗАДАНИЕ 1:\n\tПлощадь прямоугольника: {Pryamug(10, 10).Square()}\n\tПлощадь круга: {Krug(10).Square()}\n\tПлощадь прямоугольного треугольника: {Treug(10, 10).Square()}\n\tПлощадь трапеции: {Trap(10, 5,5).Square()}\n")
    print(f"ЗАДАНИЕ 2:\n\tФигура: {Pryamug(10,10)}\n\tПлощадь: {int(Pryamug(10,10))}\n\n\tФигура: {Krug(10)}\n\tПлощадь: {int(Krug(10))}\n\n\tФигура: {Treug(10,10)}\n\tПлощадь: {int(Treug(10,10))}\n\n\tФигура: {Trap(10, 5, 5)}\n\tПлощадь: {int(Trap(10, 5, 5))}\n")
    print("ЗАДАНИЕ 3")
    Shape().Menu()

if __name__ == "__main__": main()
