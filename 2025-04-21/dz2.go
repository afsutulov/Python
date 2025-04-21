package main

import (
    "fmt"
    "strconv"
)

// Функция ввоад числа с проверкой
func Num(txt string, size int) int {
    var x string
    for {
        fmt.Printf("%s: ", txt)
        fmt.Scanln(&x)
        if size == 0 || len(x) == size {
           y, err := strconv.Atoi(x)
           if err != nil { fmt.Println("Ошибка: Введенные данные не содержат чило!\n"); continue }
           return y
        } else { fmt.Printf("Ошибка: Число не %d значное!!\n", size) }
    }
}

func main() {
    var val = [3] int {0, 0}

    // Задание 1
    val[0] = Num("Введите размер стороны квадрата", 0)
    fmt.Println("Результат:")
    for i := 0; i < val[0]; i++ {
       for j :=0; j < val[0]; j++ {
           fmt.Print("*")
       }
       fmt.Println()
    }

    // Задание 2
    val[0] = Num("Введите ширину прямоугольника", 0)
    val[1] = Num("Введите высоту прямоугольника", 0)
    fmt.Println("Результат:")
    for i := 0; i < val[1]; i++ {
       for j := 0; j < val[0]; j++ {
           fmt.Print("*")
       }
       fmt.Println()
    }

    // Задание 3
    val[0] = Num("Введите размер стороны квадрата", 0)
    fmt.Println("Результат:")
    for i := 1; i <= val[0]; i++ {
       for j :=1; j <= val[0]; j++ {
           if i == 1 || i == val[0] || j == 1 || j == val[0] { fmt.Print("*") } else { fmt.Print(" ") }
       }
       fmt.Println()
    }

    // Задание 4
    val[0] = Num("Введите ширину прямоугольника", 0)
    val[1] = Num("Введите высоту прямоугольника", 0)
    fmt.Println("Результат:")
    for i := 1; i <= val[1]; i++ {
       for j := 1; j <= val[0]; j++ {
           if i == 1 || i == val[1] || j == 1 || j == val[0] { fmt.Print("*") } else { fmt.Print(" ") }
       }
       fmt.Println()
    }
}
