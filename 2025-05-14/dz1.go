package main

import (
    "fmt"
    "math/rand"
)

var (
    mass = [][]int{{rand.Intn(11),rand.Intn(11),rand.Intn(11),rand.Intn(11),rand.Intn(11),rand.Intn(11),rand.Intn(11),rand.Intn(11),rand.Intn(11),rand.Intn(11)},
                   {rand.Intn(11),rand.Intn(11),rand.Intn(11),rand.Intn(11),rand.Intn(11),rand.Intn(11),rand.Intn(11),rand.Intn(11),rand.Intn(11),rand.Intn(11)},
                   {rand.Intn(11),rand.Intn(11),rand.Intn(11),rand.Intn(11),rand.Intn(11),rand.Intn(11),rand.Intn(11),rand.Intn(11),rand.Intn(11),rand.Intn(11)}}
)

func intersection(first, second []int) []int {
    out := []int{}
    bucket := map[int]bool{}
    for _, i := range first {
        for _, j := range second {
            if i == j && !bucket[i] {
                out = append(out, i)
                bucket[i] = true
            }
        }
    }
    return out
}

func Dublicate(mass []int) []int {
    seen := make(map[int]bool)
    result := []int{}
    for _, val := range mass {
       if !seen[val] { seen[val] = true; result = append(result, val) }
    }
    return result
}

func main() {
    fmt.Println("НАЧАЛЬНЫЕ ДАННЫЕ:")
    for i := 0; i < len(mass); i++ { fmt.Printf("Кортеж %d: %d\n", i, mass[i]) }

    // Задание 1
    fmt.Println("\nЗАДАНИЕ 1: Есть три кортежа целых чисел необходимо найти элементы, которые есть во всех кортежах.\n\nРЕШЕНИЕ:")
    fmt.Println(intersection(intersection(mass[0], mass[1]), mass[2]))

    // Задание 2
    fmt.Println("\nЗАДАНИЕ 2: Есть три кортежа целых чисел необходимо найти элементы, которые уникальны для каждого списка.\n\nРЕШЕНИЕ:")
    for i := 0; i < len(mass); i++ { fmt.Printf("Уникальные значения: %d\n", Dublicate(mass[i])) }

    // Задание 3
    fmt.Println("\nЗАДАНИЕ 3: Есть три кортежа целых чисел необходимо найти элементы, которые есть в каждом из кортежей и находятся в каждом из кортежей на той же позиции.\n\nРЕШЕНИЕ:")
    Flag := true
    for i := 0; i < len(mass[0]); i++ {
        if mass[0][i] == mass[1][i] && mass[0][i] == mass[2][i] { fmt.Printf("Индекс: %d\tЗначение: %d", i, mass[0][i]); Flag = false }
    }
    if Flag { fmt.Println("Таких элементов нет") }
}
