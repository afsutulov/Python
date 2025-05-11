package main

import (
    "fmt"
    "math/rand"
    "strconv"
)

// Функция ввоад числа с проверкой
func Num(txt string, n1, n2 int) int {
    var p string
    fmt.Printf("%s: ", txt)
    fmt.Scanln(&p)
    y, err := strconv.Atoi(p)
    if err == nil && y >= n1 && y <= n2 { return y } else { fmt.Printf("Ошибка ввода! Необходимо ввести число от %d до %d!\n", n1, n2); return Num(txt, n1, n2)}
}

func Summ(a []int) int {
    i :=0
    for _, j := range a  { i += j }
    return i
}

func Sort(a []int, x int) []int {
    for i := 0; i <  x; i++ {
       for j := i; j < x; j ++ { if a[i] > a[j] { a[i], a[j] = a[j], a[i] } }
    }
    return a
}

func main () {
    mass := []int {}
    // Задание 1
    for len(mass) < 30 { mass = append(mass, rand.Intn(200) - 100) }
    fmt.Println("ЗАДАНИЕ 1: Необходимо отсортировать первые две трети списка в порядке возрастания, если среднее арифметическое всех элементов больше нуля; иначе — лишь первую треть. Остальную часть списка не сортировать, а расположить в обратном порядке.\n\nРЕШЕНИЕ:")
    fmt.Printf("Первоначальный список (%d, элементов): %d\n", len(mass), mass)
    if Summ(mass) / len(mass) > 0 { fmt.Printf("Средняя арифметическое: %d\nСписок с отсортированными элементами от 0 до %d: %d\n", Summ(mass)/len(mass), len(mass) / 3 * 2 - 1, Sort(mass, len(mass) / 3 * 2))
    } else { fmt.Printf("Средняя арифметическое: %d\nСписок с отсортированными элементами от 0 до %d: %d\n", Summ(mass)/len(mass), len(mass) / 3 - 1, Sort(mass, len(mass) / 3))}

    // Задание 2
    mass = nil
    fmt.Println("\n\nЗАДАНИЕ 2: Написать программу «успеваемость». Пользователь вводит 10 оценок студента. Оценки от 1 до 12. Реализовать меню для пользователя:\n - Вывод оценок (вывод содержимого списка);\n - Пересдача экзамена (пользователь вводит номер элемента списка и новую оценку);\n - Выходит ли стипендия (стипендия выходит, если средний бал не ниже 10.7);\n - Вывод отсортированного списка оценок: по возрастанию или убыванию.\n\nРЕШЕНИЕ:")
    for len(mass) < 10 { mass = append(mass, Num(fmt.Sprintf("Введите оценку %d", len(mass) + 1), 1, 12)) }
    fmt.Printf("Оценки: %d\n", mass)
    mass[Num("Какую оценку заменить (1  - 10)", 1, 10) -1] = Num("Введите новую оценку", 1, 12)
    fmt.Printf("Новые Оценки: %d\nСредний бал: %.2f. ", mass, float32(Summ(mass)) / float32(len(mass)))
    if float32(Summ(mass)) / float32(len(mass)) > 10.7 { fmt.Println("Стипендия будет!") } else { fmt.Println("Стипендии не будет :(") }
    fmt.Printf("Отсортированные оценки: %d\n", Sort(mass, len(mass)))

    // Задание 3
    mass = nil
    for len(mass) < 30 { mass = append(mass, rand.Intn(200) - 100) }
    fmt.Println("\n\nЗАДАНИЕ 3: Написать программу, реализующую сортировку списка методом усовершенствованной сортировки пузырьковым методом. Усовершенствование состоит в том, чтобы анализировать количество перестановок на каждом шагу, если это количество равно нулю, то продолжать сортировку нет смысла — список отсортирован.\n\nРЕШЕНИЕ:")
    fmt.Printf("Первоначальный список: %d\n", mass)
    i := 1
    for  i != 0 {
       i = 0
      for j :=0; j < len(mass) - 1; j++ { if mass[j] > mass[j+1] { mass[j], mass[j + 1] = mass[j + 1], mass[j]; i += 1 } }
    }
    fmt.Printf("Отсортированный список: %d\n", mass)
}