package main

import (
    "fmt"
    "strconv"
)

// Функция ввоад числа с проверкой
func Num(txt string) int {
    var x string
    fmt.Printf("%s: ", txt)
    fmt.Scanln(&x)
    y, err := strconv.Atoi(x)
    if err == nil { return y } else { fmt.Println("Ошибка ввода! Необходимо ввести число!\n"); return Num(txt) }
}

func Zad1() {
    fmt.Printf("\"Don't let the noise of others' opinions\ndrown out your own inner voice.\n%38s\"", "Steve Jobs")
}

func Zad2(x, y int) {
    if x > y { x, y = y, x }
    fmt.Printf("Результат")
    for i := x; i < y + 1; i++ { if i % 2 != 0 { fmt.Printf(" %d", i) } }
}

func Zad3(x int, txt string, Flag bool) {
    for i := 0; i < x; i++ {
        fmt.Printf(txt)
        if Flag { fmt.Println("") }
    }
}

func Zad4(ind [4]int) int {
    tmp := ind[0]
    for i := 1; i < len(ind); i++ { if ind[i] > tmp { tmp = ind[i]} }
    return tmp
}

func Zad5(x, y int) int {
    if x > y { x, y = y, x }
    pro := 0
    for i := x; i < y +1; i++ { pro += i }
    return pro
}

func  Zad6(a int) bool {
    for i := 2; i < a; i++ { if a % i == 0 { return false } }
    return true
}

func Zad7(x string) bool {
    sum1 := 0
    sum2 := 0
    for i :=0; i < 3; i ++ {
        a1, _ := strconv.Atoi(string(x[i]))
        a2, _ := strconv.Atoi(string(x[i + 3]))
        sum1 += a1
        sum2 += a2
    }
    return sum1 == sum2
}

func main() {
    // Задание 1
    fmt.Println("ЗАДАНИЕ 1:\n")
    Zad1()

    //  Задание 2
    fmt.Println("\n\nЗАДАНИЕ 2: Напишите функцию, которая принимает два числа в качестве параметра и отображает все нечетные числа между ними.\nРЕЩЕНИЕ:")
    Zad2(Num("Введите число 1"), Num("Введите число 2"))

    // Задание 3
    fmt.Println("\n\nЗАДАНИЕ 3: Напишите функцию, которая отображает горизонтальную или вертикальную линию из некоторого символа. Функция принимает в качестве параметра: длину линии, направление, символ\nРЕЩЕНИЕ:")
    x := 0
    for {
       x = Num("Введите символ (число 0-9")
       if x < 10 { break }
    }
    Zad3(Num("Введите длинну стороны"), strconv.Itoa(x), Num("Введите 1 если направление ВЕРТИКАЛЬНОЕ, либо любую другую цифру если направление ГОРИЗОНТАЛЬНОЕ") == 1)

    // Задание 4
    fmt.Println("\n\nЗАДАНИЕ 4: Напишите функцию, которая возвращает максимальное из четырех чисел. Числа передаются в качестве параметров\nРЕЩЕНИЕ:")
    fmt.Println("\nМинимальное число: ", Zad4([4]int{Num("Введите число 1"), Num("Введите число 2"), Num("Введите число 3"), Num("Введите число 4")}))

    // Задание 5
    fmt.Println("\n\nЗАДАНИЕ 5: Напишите функцию, которая возвращает сумму чисел в указанном диапазоне. Границы диапазона передаются в качестве параметров.\nРЕЩЕНИЕ:")
    fmt.Println("\nСумма чисел:", Zad5(Num("Введите границу диапазона 1"), Num("Введите границу диапазона 2")))

    // Задание 6
    fmt.Println("\n\nЗАДАНИЕ 6: Напишите функцию, которая проверяет является ли число простым. Число передаётся в качестве параметра. Если число простое нужно вернуть из метода true, иначе false.\nРЕЩЕНИЕ:")
    fmt.Println("\nРезультат:", Zad6(Num("Введите число")))

    // Задание 7
    fmt.Println("\n\nЗАДАНИЕ 7: Напишите функцию, которая проверяет является ли шестизначное число «счастливым». Число передаётвернуть из функции true, иначе false.\nРЕЩЕНИЕ:")
    y := ""
    for {
       y = strconv.Itoa(Num("Введите шестизначное число"))
       if len(y) == 6 { break }
    }
    fmt.Println("\nРезультат:", Zad7(y))
}