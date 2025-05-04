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
    fmt.Printf("\"Don't compare yourself with anyone in this world…\nif you do so, you are insulting yourself\"\n%52s", "Bill Gates")
}

func Zad2(x, y int) {
    if x > y { x, y = y, x }
    fmt.Printf("Результат")
    for i := x; i < y + 1; i++ { if i % 2 == 0 { fmt.Printf(" %d", i) } }
}

func Zad3(x int, txt string, Flag bool) {
    for i := 0; i < x; i++ {
        for j :=0; j < x; j++ {
            if Flag || i == 0 || j == 0 || i == x - 1 || j == x - 1 { fmt.Printf(txt) } else { fmt.Printf(" ") }
        }
        fmt.Println("")
    }
}

func Zad4(ind [5]int) int {
    tmp := ind[0]
    for i := 1; i < len(ind); i++ { if ind[i] < tmp { tmp = ind[i]} }
    return tmp
}

func Zad5(x, y int) int {
    if x > y { x, y = y, x }
    pro := 1
    for i := x; i < y +1; i++ { pro *= i }
    return pro
}

func  Zad6(txt string) int {
    return len(txt)
}

func Zad7(txt string) bool {
    res := ""
    for _, i:= range txt { res = string(i) + res }
    return res == txt
}

func main() {
    // Задание 1
    print("ЗАДАНИЕ 1:\n")
    Zad1()

    // Задание 2
    fmt.Println("\n\nЗАДАНИЕ 2: Напишите функцию, которая принимает два числа в качестве параметра и отображает все четные числа между ними.\nРЕЩЕНИЕ:")
    Zad2(Num("Введите число 1"), Num("Введите число 2"))

    // Задание 3
    fmt.Println("\n\nЗАДАНИЕ 3: Напишите функцию, которая отображает пустой или заполненный квадрат из некоторого символа. Функция принимает в качестве параметров: длину стороны квадрата, символ и переменную логического типа\nРЕЩЕНИЕ:")
    x := 0
    for {
       x = Num("Введите символ (число 0-9")
       if x < 10 { break }
    }
    Zad3(Num("Введите длинну стороны"), strconv.Itoa(x), Num("Введите 1 если квадрат заполненный либо любую другую цифру если пустой") == 1)

    // Задание 4
    fmt.Println("\n\nЗАДАНИЕ 4: Напишите функцию, которая возвращает минимальное из пяти чисел. Числа передаются в качестве параметров\nРЕЩЕНИЕ:")
    fmt.Println("\nМинимальное число: ", Zad4([5]int{Num("Введите число 1"), Num("Введите число 2"), Num("Введите число 3"), Num("Введите число 4"), Num("Введите число 5")}))

    // Задание 5
    fmt.Println("\n\nЗАДАНИЕ 5: Напишите функцию, которая возвращает произведение чисел в указанном диапазоне. Границы диапазона передаются в качестве параметров.\nРЕЩЕНИЕ:")
    fmt.Println("\nПроизведение чисел:", Zad5(Num("Введите границу диапазона 1"), Num("Введите границу диапазона 2")))

    // Задание 6
    fmt.Println("\n\nЗАДАНИЕ 6: Напишите функцию, которая считает количество цифр в числе. Число передаётся в качестве параметра. Из функции нужно вернуть полученное количество цифр.\nРЕЩЕНИЕ:")
    fmt.Println("\nКоличество цифр:", Zad6(strconv.Itoa(Num("Введите число"))))

    //  Задание 7
    fmt.Println("\n\nЗАДАНИЕ 7: Напишите функцию, которая проверяет является ли число палиндромом. Число передаётся в качестве параметра. Если число палиндром нужно вернуть из функции true, иначе false.\nРЕЩЕНИЕ:")
    fmt.Println("\nРезультат:", Zad7(strconv.Itoa(Num("Введите число"))))
}