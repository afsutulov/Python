package main

import (
    "fmt"
    "math/rand"
    "strconv"
)

// Функция ввоад числа с проверкой
func Num(txt string, n1, n2 int) int {
    var p string
    fmt.Printf("%s: ", txt)
    fmt.Scanln(&p)
    y, err := strconv.Atoi(p)
    if err == nil && y >= n1 && y <= n2 { return y } else { fmt.Printf("Ошибка ввода! Необходимо ввести число от %d до %d!\n", n1, n2); return Num(txt, n1, n2)}
}

// Поиск индекса совпадений
func indx(mass []int, x int) []int {
    y := []int {}
    for i, val := range mass { if val == x { y = append(y, i) } }
    return y
}

func main() {
    // Задание 1
    fmt.Println("ЗАДАНИЕ 1: Есть список из 10 элементов, заполненный случайными числами. Необходимо найти число, введенное пользователем. Используйте алгоритм линейного поиска.\n\nРЕШЕНИЕ:")
    mass := []int {}
    for len(mass) < 10 { mass = append(mass, rand.Intn(11)) }
    fmt.Printf("Список: %d\n", mass)
    fmt.Printf("Индексы совпадений: %d\n", indx(mass, Num("Введите число для поиска", 0, 10)))

    // Задание 2
    fmt.Println("\nЗАДАНИЕ 2: Есть список из 10 элементов, заполненный случайными числами. Необходимо найти число, введенное пользователем. Используйте алгоритм линейного поиска.\n\nРЕШЕНИЕ:")
    mass = nil
    for len(mass) < 10 { mass = append(mass, rand.Intn(11)) }
    fmt.Printf("Список: %d\n", mass)
    fmt.Printf("Индексы совпадений: %d\n", indx(mass, Num("Введите число для поиска", 0, 10)))
}