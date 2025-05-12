package main

import (
    "fmt"
    "math/rand"
    "strconv"
    "sort"
)

// Функция ввоад числа с проверкой
func Num(txt string, n1, n2 int) int {
    var p string
    fmt.Printf("%s: ", txt)
    fmt.Scanln(&p)
    y, err := strconv.Atoi(p)
    if err == nil && y >= n1 && y <= n2 { return y } else { fmt.Printf("Ошибка ввода! Необходимо ввести число от %d до %d!\n", n1, n2); return Num(txt, n1, n2)}
}

// Поиск индекса совпадений
func indx(mass []int, x int) []int {
    y := []int {}
    for i, val := range mass { if val == x { y = append(y, i) } }
    return y
}

func Dublicate(mass []int) []int {
    seen := make(map[int]bool)
    result := []int{}
    for _, val := range mass {
       if !seen[val] { seen[val] = true; result = append(result, val) }
    }
    return result
}

func ObshiyKod(mass []int) {
    switch Num("\nВарианты:\n\t1 - отсортировать по возрастанию\n\t2 - отсортировать по убыванию\nВыберите дейстие", 1, 2) {
       case 1: sort.Ints(mass)
       case 2: sort.Sort(sort.Reverse(sort.IntSlice(mass)))
    }
    fmt.Printf("\nОтсортированный список: %d\n", mass)
    fmt.Printf("Индексы совпадений: %d\n", indx(mass, Num("Введите число для поиска", 0, 10)))
}

func main() {
    // Задание 1
    fmt.Println("ЗАДАНИЕ 1: Есть четыре списка целых. Необходимо их объединить в пятом списке. Полученный результат в зависимости от выбора пользователя отсортировать по убыванию или возрастанию. Найти значение, введенное пользователем, с использованием линейного поиска.\n\nРЕШЕНИЕ:")
    mass := []int {}
    for i := 0; i < 4; i++ {
        x := []int {}
        for len(x) < 10 { x = append(x, rand.Intn(11)) }
        fmt.Printf("Список\t%d: %d\n",i + 1, x)
        mass = append(mass, x...)
    }
    fmt.Printf("Объединенный список: %d\n", mass)
    ObshiyKod(mass)

    // Задание 2
    fmt.Println("\nЗАДАНИЕ 2: Есть четыре списка целых. Необходимо объединить в пятом списке только те элементы, которые уникальны для каждого списка. Полученный результат в зависимости от выбора пользователя отсортировать по убыванию или возрастанию. Найти значение, введенное пользователем\n\nРЕШЕНИЕ:")
    mass = nil
    for i := 0; i < 4; i++ {
        x := []int {}
        for len(x) < 10 { x = append(x, rand.Intn(11)) }
        fmt.Printf("Список\t %d: %d\tУникальные значения: %d\n", i + 1, x, Dublicate(x))
        mass = append(mass, Dublicate(x)...)
    }
    fmt.Printf("Объединенный список: %d\n", mass)
    ObshiyKod(mass)
}