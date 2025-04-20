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
    var val = [3] int {0, 0, 0}

    // Задание 1
    fmt.Println("ЗАДАНИЕ1\nПользователь вводит с клавиатуры три числа. В зависимости от выбора пользователя программа выводит на экран сумму трёх чисел или произведение трёх чисел.\n\nРЕШЕНИЕ:")
    for i := 0; i < len(val); i++ {
        val[i] = Num("Ввведите число " + strconv.Itoa(i + 1))
    }
    fmt.Println("\nДействие:\n\t1: сумма трех чисел\n\t2: произведение трех чисел")
    nm := Num("Введите нужное действие")

    switch nm {
       case 1: fmt.Println("\nСумма трех чисел: ", val[0] + val[1] + val[2])
       case 2: fmt.Println("\nПроизведение трех чисел: ", val[0] * val[1] * val[2])
       default: fmt.Println("\nОшибка! Вы ввели неправильное действие!")
    }

    // Задание 2
    fmt.Println("\nЗАДАНИЕ2\nПользователь вводит с клавиатуры три числа. В зависимости от выбора пользователя программа выводит на экран максимум из трёх, минимум из трёх или среднеарифметическое трёх чисел\n\nРЕШЕНИЕ:")
    sum := 0
    for i := 0; i < len(val); i++ {
        val[i] = Num("Ввведите число " + strconv.Itoa(i + 1))
        sum += val[i]
    }
    // Сортируем массив от меньшего к большему
    for i := 0; i < len(val); i++ {
        for j := i; j < len(val); j++ {
            if val[i] > val[j] {
               x := val[i]
               val[i] = val[j]
               val[j] = x
            }
        }
    }
    fmt.Println("\nДействие:\n\t1: максимум из трех чисел\n\t2: минимум из трех чисел\n\t3: среднеарифметическое трех чисел")
    nm = Num("Введите нужное действие")
    switch nm {
       case 1: fmt.Println("\nМаксимальное из трех чисел: ", val[2])
       case 2: fmt.Println("\nМинимальное из трех чисел: ", val[0])
       case 3: fmt.Println("\nСреднеарифметическое из трех чисел: ", sum / 3)
       default: fmt.Println("\nОшибка! Вы ввели неправильное действие!")
    }

    // Задание 3
    fmt.Println("\nЗАДАНИЕ3\nПользователь вводит с клавиатуры количество метров. В зависимости от выбора пользователя программа переводит метры в мили, дюймы или ярды\n\nРЕШЕНИЕ:")
    val[0] = Num("Введите колличество метров")
    fmt.Println("\nПеревести {val[0]}м. в:\n\t1: мили\n\t2: дюймы\n\t3: ярды")
    nm = Num("Введите нужное действие")
    switch nm {
       case 1: fmt.Printf("\n%dм. в милях: %f\n", val[0], float64(val[0]) * 0.000621)
       case 2: fmt.Printf("\n%dм. в дюймах: %f\n", val[0], float64(val[0]) * 39.37)
       case 3: fmt.Printf("\n%dм. в ярдах: %f\n", val[0], float64(val[0]) * 1.09)
       default: fmt.Println("\nОшибка! Вы ввели неправильное действие!")
    }
}
