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
    var val = [3] int {0, 0, 0}

    // Задание 1
    fmt.Println("ЗАДАНИЕ1\nПользователь вводит с клавиатуры три числа. В зависимости от выбора пользователя программа выводит на экран сумму трёх чисел или произведение трёх чисел.\n\nРЕШЕНИЕ:")
    for i := 0; i < len(val); i++ { val[i] = Num("Ввведите число " + strconv.Itoa(i + 1), 0) }
    fmt.Println("\nДействие:\n\t1: сумма трех чисел\n\t2: произведение трех чисел")
    for {
       nm := Num("Введите нужное действие", 1)
       switch nm {
          case 1: fmt.Printf("\nСумма трех чисел: %d\n", val[0] + val[1] + val[2])
          case 2: fmt.Printf("\nПроизведение трех чисел: %d\n", val[0] * val[1] * val[2])
          default: fmt.Println("Ошибка! Вы ввели неправильное действие!\n"); continue
       }
       break
    }

    // Задание 2
    fmt.Println("\n\nЗАДАНИЕ2\nПользователь вводит с клавиатуры три числа. В зависимости от выбора пользователя программа выводит на экран максимум из трёх, минимум из трёх или среднеарифметическое трёх чисел\n\nРЕШЕНИЕ:")
    sum := 0
    for i := 0; i < len(val); i++ { val[i] = Num("Ввведите число " + strconv.Itoa(i + 1), 0); sum += val[i] }

    // Сортируем массив от меньшего к большему
    for i := 0; i < len(val); i++ {
        for j := i; j < len(val); j++ {
            if val[i] > val[j] { x := val[i]; val[i] = val[j]; val[j] = x }
        }
    }

    fmt.Println("\n\nДействие:\n\t1: максимум из трех чисел\n\t2: минимум из трех чисел\n\t3: среднеарифметическое трех чисел")
    for {
       nm := Num("Введите нужное действие", 1)
       switch nm {
          case 1: fmt.Printf("\nМаксимальное из трех чисел: %d\n", val[2])
          case 2: fmt.Printf("\nМинимальное из трех чисел: %d\n", val[0])
          case 3: fmt.Printf("Среднеарифметическое из трех чисел: %f\n", float64(sum) / 3)
          default: fmt.Println("Ошибка! Вы ввели неправильное действие!\n"); continue
       }
       break
    }

    // Задание 3
    fmt.Println("\n\nЗАДАНИЕ3\nПользователь вводит с клавиатуры количество метров. В зависимости от выбора пользователя программа переводит метры в мили, дюймы или ярды\n\nРЕШЕНИЕ:")
    val[0] = Num("Введите колличество метров", 0)
    fmt.Println("\nПеревести {val[0]}м. в:\n\t1: мили\n\t2: дюймы\n\t3: ярды")
    for {
       nm := Num("Введите нужное действие", 1)
       switch nm {
          case 1: fmt.Printf("\n%dм. в милях: %f\n", val[0], float64(val[0]) * 0.000621)
          case 2: fmt.Printf("\n%dм. в дюймах: %f\n", val[0], float64(val[0]) * 39.37)
          case 3: fmt.Printf("\n%dм. в ярдах: %f\n", val[0], float64(val[0]) * 1.09)
          default: fmt.Println("Ошибка! Вы ввели неправильное действие!\n"); continue
       }
       break
    }
}
