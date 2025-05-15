package main

import (
    "fmt"
    "math/rand"
    "strings"
)

// Функция ввоад числа с проверкой
func Num(txt string) string {
    var p string
    fmt.Printf("%s: ", txt)
    fmt.Scanln(&p)
    return p
}

// Поиск индекса совпадений
func indx(mass []string, x string, Flag bool) int {
    y := 0
    for _, val := range mass { if (Flag && val == x) || (!Flag && strings.Contains(val, x)) { y += 1 } }
    return y
}

func main() {
    // Задание 1
    x := []string{"apple", "pear", "banana", "orange", "lemon", "lime", "grapefruit", "pineapple", "mango", "peach", "plum", "cherry", "strawberry", "raspberry", "blueberry", "blackberry", "grape", "watermelon", "melon", "bananamango", "strawberry-banana"}
    fmt.Println("\nЗАДАНИЕ 1: Пользователь вводит с клавиатуры название фрукта. Необходимо вывести на экран количество раз, сколько фрукт встречается в кортеже в качестве элемента.\n\nРЕШЕНИЕ:")
    fmt.Printf("Фрукты: %s\n\n", x)
    y := Num("Введите название фрукта")
    fmt.Printf("Количество раз: %d\n", indx(x, y, true))

    // Задание 2
    fmt.Println("\n\nЗАДАНИЕ 2: Добавьте к заданию 1 подсчет количества раз, когда название фрукта является частью элемента\n\nРЕШЕНИЕ:")
    fmt.Printf("Количество раз: %d\n", indx(x, y, false))

    // Задание 3
    x = nil
    x = []string{"Ford", "Renault", "Toyota", "Honda", "Hyundai", "Kia", "Ford", "Lexus", "Nissan", "Opel", "Peugeot", "Volvo", "Hyundai", "Honda", "Renault", "Škoda", "SsangYong", "Renault", "Toyota", "Subaru", "Mitsubishi", "Toyota", "Volkswagen", "Volvo", "Renault"}
    fmt.Println("\n\nЗАДАНИЕ 3: Есть кортеж с названиями производителей автомобилей (название производителя может встречаться от 0 до N раз). Пользователь вводит с клавиатуры название производителя и слово для замены. Необходимо заменить в кортеже все элементы с этим названием на слово для замены. Совпадение по названию должно быть полным.\n\nРЕШЕНИЕ:")
    fmt.Printf("Производители авто: %s\n\n", x)
    a := Num("Введите название производителя")
    b := Num("Введите на что нужно заменить")
    for i := 0; i < len(x); i ++ { if x[i] == a { x[i] = b } }
    fmt.Printf("\nРезультат: %s\n", x)

    // Задание 4
    fmt.Println("\n\nЗАДАНИЕ 4: Есть кортеж с целыми числами. Нужно вывести статистику по количеству цифр в элементах кортежа.\n\nРЕШЕНИЕ:")
    z := []int {}
    for len(z) < 30 { z = append(z, rand.Intn(1000)) }
    fmt.Printf("Кортеж с целыми числами: %d\n", z)
    c := []int{0, 0, 0}
    for _, val := range z {
        if val < 10 { c[0] += 1 } else if val < 100 { c[1] += 1 } else { c[2] += 1 }
    }
    fmt.Printf("Результат:\n\tОдна цифра: %d\n\tДве цифры: %d\n\tТри цифры: %d\n", c[0], c[1], c[2])
}
