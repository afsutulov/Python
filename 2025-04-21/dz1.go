package main

import (
    "fmt"
    "strconv"
    "math/rand"
    "time"
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
    var val = [3] int {0, 0, 0}

    // Задание 1
    for {
       val[0] = Num("Введите число до 10", 1)
       if val[0] < 10 { break } else { fmt.Print("Введите число меньше 10\n") }
    }

    for i := 1; i <= val[0]; i++ {
        fmt.Println(val[0], "*", i, "=", val[0] * i)
    }

    // Задание 2
    val[0] = Num("\nВведите сумму в рублях", 0)
    fmt.Println("\nКонвертировать:\n\t1: Доллары США\n\t2: Евро\n\t3: Казахстанские Тенге")
    nm := Num("Введите нужное действие", 1)
    switch nm {
       case 1: fmt.Printf("Сумма в Долларах США: %d\n", val[0] * 85)
       case 2: fmt.Printf("Сумма в Евро: %d\n", val[0] * 105)
       case 3: fmt.Printf("Сумма в Казахстанских Тенге: %d\n", int(float64(val[0]) * 5.15))
       default: fmt.Println("Ошибка! Вы ввели неправильное действие!\n")
    }

    // Задание 3
    for {
       val[0] = Num("\nВведите нижнюю границу диапазона", 1)
       val[1] = Num("Введите верхнюю границу диапазона", 1)
       val[2] = Num("Введите число", 1)
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
       val[0] = Num("\nВведите предполагаемое число", 0)
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
