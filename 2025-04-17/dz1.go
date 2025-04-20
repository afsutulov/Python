package main

import (
    "fmt"
    "unicode"
    "strconv"
    "math"
)

// Функция ввоад числа с проверкой
func Num(txt string) int {
    var x string
    for {
        fmt.Print(txt, ": ")
        fmt.Scanln(&x)
        Flag := true
        for _, char := range x {
            if !unicode.IsDigit(char) { Flag = false; break }
        }
        if Flag { y, _ := strconv.Atoi(x); return y } else { fmt.Println("Ошибка: Введенные данные не содержат чило!\n") }
    }
}

func main() {
    var val = [3] int {0, 0, 0}

    //  Задание 1
    val[0] = Num("Введите время в секундах с начала дня")
    fmt.Println("\nДействие:\n\t1: сколько часов до полуночи\n\t2: сколько минут до полуночи\n\t3: сколько секунд дополуночи")
    nm := Num("Введите нужное действие")
    switch nm {
       case 1: fmt.Println("\nРезультат: ", 24 - val[0] / 60 / 60)
       case 2: fmt.Println("\nРезультат: ", 1440 - val[0] / 60)
       case 3: fmt.Println("\nРезультат: ", 86400 - val[0])
       default: fmt.Println("\nОшибка! Вы ввели неправильное действие!")
    }

    // Задание 2
    val[0] = Num("\nВведите диаметр окружности")
    fmt.Println("\nДействие:\n\t1: посчитать площадь\n\t2: посчитать диаметр")
    nm = Num("Введите нужное действие")
    switch nm {
       case 1: fmt.Println("\nРезультат:", 3.14 * float64(math.Pow(float64(val[0] / 2), 2)))
       case 2: fmt.Println("\nРезультат: ", 3.14 * float64(val[0]))
       default: fmt.Println("\nОшибка! Вы ввели неправильное действие!")
    }

    // Задание 3
    val[0] = Num("\nСтоимость одной игровой приставки")
    val[1] = Num("Количество приставок")
    val[2] = Num("Процент скидки")
    fmt.Println("\nДействие:\n\t1: посчитать общую сумму заказа\n\t2: посчитать стоимость одной приставки с учетом скидки")
    nm = Num("Введите нужное действие")
    switch nm {
       case 1: fmt.Println("\nРезультат: ", val[0] * val[1] - val[0] * val[1] * val[2] / 100)
       case 2: fmt.Println("\nРезультат: ", val[0] - val[0] * val[2] / 100)
       default: fmt.Println("\nОшибка! Вы ввели неправильное действие!")
    }

    // Задание 4
    val[0] = Num("\nРазмер файла в гигабайтах")
    val[0] = 8589934592 * val[0]
    val[1] = Num("Скорость интернет соединения в битах в секунду")
    fmt.Println("\nПосчитать скорость скачивание в:\n\t1: часах\n\t2: минутах\n\t3: секундах")
    nm = Num("Введите нужное действие")
    switch nm {
       case 1: fmt.Println("\nРезультат: ", val[0] / val[1] / 60 / 60)
       case 2: fmt.Println("\nРезультат: ", val[0] / val[1] / 60)
       case 3: fmt.Println("\nРезультат: ", val[0] / val[1])
       default: fmt.Println("\nОшибка! Вы ввели неправильное действие!")
    }

    // Задание 5
    val[0] = Num("\nВведите количество часов")
    if val[0] >=0 && val[0] < 6 {
       fmt.Println("Good Night")
    } else if val[0] >=6 && val[0] < 13 {
       fmt.Println("Good Morning")
    } else if val[0] >=13 && val[0] < 17 {
       fmt.Println("Good Day")
    } else if val[0] >=17 && val[0] < 24 {
       fmt.Println("Good Evening")
    } else {
       fmt.Println("Ups!")
    }
}
