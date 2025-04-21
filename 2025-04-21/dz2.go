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
    for {
       val[0] = Num("Введите размер стороны квадрата (до 20)")
       if val[0] <= 20 { break } else { fmt.Println("Ошибка: размер должен быть до 20!\n") }
    }
    fmt.Println("Результат:")
    for i := 0; i < val[0]; i++ {
       for j :=0; j < val[0]; j++ {
           fmt.Printf("*")
       }
       fmt.Println()
    }

    // Задание 2
    val[0] = Num("Введите ширину прямоугольника)")
    val[1] = Num("Введите высоту прямоугольника)")
    fmt.Println("Результат:")
    for i := 0; i < val[1]; i++ {
       for j := 0; j < val[0]; j++ {
           fmt.Printf("*")
       }
       fmt.Println()
    }

    // Задание 3
    for {
       val[0] = Num("Введите размер стороны квадрата (до 20)")
       if val[0] <= 20 { break } else { fmt.Println("Ошибка: размер должен быть до 20!\n") }
    }
    fmt.Println("Результат:")
    for i := 1; i <= val[0]; i++ {
       for j :=1; j <= val[0]; j++ {
           if i == 1 || i == val[0] || j == 1 || j == val[0] { fmt.Printf("*") } else { fmt.Printf(" ") }
       }
       fmt.Println()
    }

    // Задание 4
    val[0] = Num("Введите ширину прямоугольника)")
    val[1] = Num("Введите высоту прямоугольника)")
    fmt.Println("Результат:")
    for i := 1; i <= val[1]; i++ {
       for j := 1; j <= val[0]; j++ {
           if i == 1 || i == val[1] || j == 1 || j == val[0] { fmt.Printf("*") } else { fmt.Printf(" ") }
       }
       fmt.Println()
    }

}