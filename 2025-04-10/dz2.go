package main

import (
    "fmt"
    "strconv"
)

// Функция ввоад числа с проверкой
func Num(txt string) int {
    var x string
    for {
        fmt.Printf("%s: ", txt)
        fmt.Scanln(&x)
        y, err := strconv.Atoi(x)
        if err != nil { fmt.Println("Ошибка: Введенные данные не содержат чило!\n"); continue }
        return y
    }
}

func main() {
    var val = [2] int {0, 0}

    // Задание 1
    fmt.Printf("ЗАДАНИЕ1\n%20sNothing\n%20swill work\n%20sunless you do\n\n", "", "", "")

    // Задание 2
    fmt.Printf("\nЗАДАНИЕ2\n%6s\"Anyone who\n%8sstops\n%11slearning is old,\n%14swhether at twenty or eighty\",\n%38sHenry Ford\n\n", "", "", "", "", "")

    // Задание 3
    fmt.Println("\nЗАДАНИЕ3: Пользователь вводит с клавиатуры два числа. Необходимо найти сумму чисел, разницу чисел, произведение числе.\n")
    val[0] = Num("Введите число 1")
    val[1] = Num("Введите число 2")
    fmt.Printf("\nРЕЗУЛЬТАТ\n\tСумма чисел: %d\n\tРазница чисел: %d\n\tПроизведение чисел: %d\n\n", val[0] + val[1], val[0] - val[1], val[0] * val[1])

    // Задание 4
    fmt.Println("\nЗАДАНИЕ4: Пользователь вводит с клавиатуры два числа. Первое число — это значение, второе число процент, который нобходимо посчитать.\n")
    val[0] = Num("Введите значеине")
    val[1] = Num("Введите процент")
    fmt.Printf("\nРЕЗУЛЬТАТ: %f\n\n", float64(val[0]) * float64(val[1]) / 100)

    // Задание 5
    fmt.Println("\nЗАДАНТЕ 5: Напишите программу, вычисляющую площадь прямоугольника.\n")
    val[0] = Num("Введите ширину прямоугольника")
    val[1] = Num("Введите высоту прямоугольника")
    fmt.Printf("\nПлощадь прямоугольника: %d", val[0] * val[1])
}
