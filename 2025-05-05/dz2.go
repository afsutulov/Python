package main

import (
    "fmt"
    "math/rand"
    "strconv"
    "math"
)

var (
    mass = []int {}
    mass2 = []int {}
)

// Функция ввоад числа с проверкой
func Num(txt string, n1, n2 int) int {
    var p string
    fmt.Printf("%s: ", txt)
    fmt.Scanln(&p)
    y, err := strconv.Atoi(p)
    if err == nil && y >= n1 && y <= n2 { return y } else { fmt.Printf("Ошибка ввода! Необходимо ввести число от %d до %d!\n", n1, n2); return Num(txt, n1, n2)}
}

func Zad1(Mass []int) int64 {
    var x int64 
    x = 1
    for _, i := range Mass { x *= int64(i) }
    return x
}

func Zad2(Mass []int) int {
    x := Mass[0]
    for _, i := range Mass { if i < x { x = i } }
    return x
}

func Zad3(Mass []int) int {
    x := 0
    for _, i := range Mass {
       for y := 2; y < i / 2 + 1; y++ {
          if i % y == 0 { x += 1; break }
       }
    }
    return len(Mass) - x
}

func Zad4(Mass []int, x int) int {
    for _, i := range Mass {
       if i != x { mass2 = append(mass2, i) }
    }
    fmt.Println("РЕШЕНИЕ: Массив с удаленным элементом", x, ":",  mass2)
    return len(Mass) - len(mass2)
}

func Zad5(a, b []int) []int {
    for _, i := range b { a = append(a, i) }
    return a
}

func Zad6(Mass []int, x int) []int {
    mass2 := []int {}
    for _, i := range Mass {
       mass2 = append(mass2, int(math.Pow(float64(i), float64(x))))
    }
    return mass2
}

func main() {
    for len(mass) < 10 { mass = append(mass, rand.Intn(49) + 1) }
    fmt.Println("МАССИВ ДЛЯ РАБОТЫ:",  mass, "\n")

    // Задание 1
    fmt.Println("ЗАДАНИЕ 1: Напишите функцию, вычисляющую произведение элементов списка целых. Список передаётся в качестве параметра. Полученный результат возвращается из функции.")
    fmt.Println("РЕЗУЛЬТАТ: Произведение равно ", Zad1(mass))

    // Задание 2
    fmt.Println("\n\nЗАДАНИЕ 2: Напишите функцию для нахождения минимума в списке целых. Список передаётся в качестве параметра. Полученный результат возвращается из функции.")
    fmt.Println("РЕЗУЛЬТАТ: Минимум в массиве равен ", Zad2(mass))

    // Задание 3
    fmt.Println("\n\nЗАДАНИЕ 3: Напишите функцию, определяющую количество простых чисел в списке целых. Список передаётся в качестве параметра. Полученный результат возвращается из функции.")
    fmt.Println("РЕШЕНИЕ: Простых чисел в массиве ", Zad3(mass))

    // Задание 4
    fmt.Println("\n\nЗАДАНИЕ 4: Напишите функцию, удаляющую из списка целых некоторое заданное число. Из функции нужно вернуть количество удаленных элементов\n")
    fmt.Println("Количество удаленных элементов ", Zad4(mass, Num("Введите удаляемое число", 1, 100)))

    // Задание 5
    fmt.Println("\n\nЗАДАНИЕ 5: Напишите функцию, которая получает два списка в качестве параметра и возвращает список, содержащий элементы обоих списков:")
    fmt.Println("РЕШЕНИЕ: Объединенный список (первоначальный + список с удаленными элементами): ", Zad5(mass, mass2))

    // Задание 6
    fmt.Println("\n\nЗАДАНИЕ 6: Напишите функцию, высчитывающую степень каждого элемента списка целых. Значение для степени передаётся в качестве параметра, список тоже передаётся в качестве параметра. Функция возвращает новый список, содержащий полученные результаты.\n")
    fmt.Println("\nРЕЗУЛЬТАТ: Навый список ", Zad6(mass, Num("Введите степень", 2, 10)))
}
