package main

import (
    "fmt"
    "unicode"
    "strconv"
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
    var val = [2] int {0, 0}

    // Задание 1
    fmt.Println("ЗАДАНИЕ1\nПользователь вводит с клавиатуры число. Необходимо проверить его на четность и нечетность. Если число четное требуется вывести на экран число и надпись Even number. Если число нечетное выведите на экран число и надпись Odd number.\n\nРЕШЕНИЕ:")
    val[0] = Num("Введите число")
    if val[0] % 2 == 0 { fmt.Println("Even number\n") } else { fmt.Println("Odd number\n") }

    // Задание 2
    fmt.Println("\nЗАДАНИЕ2\nПользователь вводит с клавиатуры число. Необходимо проверить его на кратность 7. Если число кратно требуется вывести на экран число и надпись Number is multiple 7. Если число не кратно выведите на экран число и надпись Number is not multiple 7.\n\nРЕШЕНИЕ:")
    val[0] = Num("Введите число")
    if val[0] % 7 == 0 { fmt.Println("Number is multiple 7\n") } else { fmt.Println("Number is not multiple 7\n") }

    // Задание 3
    fmt.Println("\nЗАДАНИЕ3\nПользователь вводит с клавиатуры два числа. Необходимо найти максимум из двух чисел и показать его на экран.\n\nРЕШЕНИЕ:")
    for i :=0; i < len(val); i++ {
        val[i] = Num("Введите число " + string(i + 1))
    }
    if val[0] > val[1] { fmt.Printf("Максимум: %d\n\n", val[0]) } else { fmt.Printf("Максимум: %d\n\n", val[1]) }

    // Задание 4
    fmt.Println("\nЗАДАНИЕ4\nПользователь вводит с клавиатуры два числа. Необходимо найти минимум из двух чисел и показать его на экран.\n\nРЕШЕНИЕ:")
    for i := 0; i < len(val); i++ {
        val[i] = Num("Введите число " + string(i + 1))
    }
    if val[0] < val[1] { fmt.Printf("Минимум: %d\n\n", val[0]) } else { fmt.Printf("Минимум: %d\n\n", val[1]) }

    // Задание 5
    fmt.Println("\nЗАДАНИЕ5\nПользователь вводит с клавиатуры два числа. В зависимости от выбора пользователя нужно показать сумму двух чисел, разницу двух чисел, среднеарифметическое или произведение двух чисел.\n\nРЕШЕНИЕ:")
    for i :=0; i < len(val); i++ {
        val[i] = Num("Введите число " + string(i + 1))
    }
    fmt.Println("\nДействие:\n\t1: сумма чисел\n\t2: разность чисел\n\t3: cреднеарифметическое чисел\n\t4: произведение чисел")
    nm := Num("Введите нужное действие")
    switch nm {
       case 1: fmt.Println("Сумма чисел: ", val[0] + val[1])
       case 2: fmt.Println("Разность чисел: ", val[0] - val[1])
       case 3: fmt.Println("Среднеарифметическое чисел: ", float64(val[0] + val[1]) / 2)
       case 4: fmt.Println("Произведение чисел: ", val[0] * val[1])
       default: fmt.Println("Ошибка! Вы ввели неправильное действие!")
    }
}
