package main

import (
    "fmt"
    "unicode"
    "strconv"
    "math/rand"
    "time"
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
       val[0] = Num("Введите число")
       if val[0] < 10 { break } else { fmt.Print("Введите число меньше 10\n") }
    }

    for i := 1; i <= val[0]; i++ {
        fmt.Println(val[0], "*", i, "=", val[0] * i)
    }

    // Задание 2
    val[0] = Num("\nВведите сумму в рублях")
    fmt.Println("\nКонвертировать:\n\t1: Доллары США\n\t2: Евро\n\t3: Казахстанские Тенге")
    nm := Num("Введите нужное действие")
    switch nm {
       case 1: fmt.Printf("Сумма в Долларах США: %d\n", val[0] * 85)
       case 2: fmt.Printf("Сумма в Евро: %d\n", val[0] * 105)
       case 3: fmt.Printf("Сумма в Казахстанских Тенге: %d\n", val[0] * 5,15)
       default: fmt.Println("Ошибка! Вы ввели неправильное действие!\n")
    }

    // Задание 3
    for {
       val[0] = Num("\nВведите нижнюю границу диапазона")
       val[1] = Num("Введите верхнюю границу диапазона")
       val[2] = Num("Введите число")
       if val[2] >= val[0] && val[2] <= val[1] { break } else { fmt.Println("Введены некорректные данные, повторите попытку\n") }
    }
    for i := val[0]; i <= val[1]; i++ {
        if i == val[2] { fmt.Printf(" !%d!", i) } else { fmt.Printf(" %d", i) }
    }
    fmt.Println(".")

    // Задание 5
    fmt.Println("\nВ игре нужно угадать число от 1 до 500")
    rnd := rand.Intn(500) + 1
    i := 0
    cur_time := time.Now()
    for {
       val[0] = Num("Введите предполагаемое число")
       if val[0] == 0 { break }
       i++
       if val[0] == rnd {
          fmt.Printf("Вы угадали число %d! Поздравляю!\n", rnd)
          break
       } else if val[0] < rnd {
          fmt.Println("Ваше число меньше загаданного\n")
       } else if val[0] > rnd {
          fmt.Println("Ваше число больше загаданного\n")
       }
    }
    fmt.Printf("Статистика:\n\tПопыток: %d\n\tВремя: %s", i, time.Since(cur_time))
}
