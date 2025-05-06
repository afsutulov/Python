package main

import (
    "fmt"
    "strings"
    "math/rand"
    "strconv"
    "time"
)

var (
    board = [9]string {" "," "," "," "," "," "," "," "," "} // игровая доска
    winList = [8][3] int {{0,1,2}, {3,4,5}, {6,7,8}, {0,3,6}, {1,4,7}, {2,5,8}, {0,4,8}, {2,4,6}} // Выигрышные комбинации
    player string = "X" // Ход игрока
    mass = []int {} // Массив заполняемый случайными цифрами
    mins = []int {} // Массив с суммами 10 последовательностей в массиве mass
)

// Функция ввоад числа с проверкой
func Num(txt string, n1, n2 int) int {
    var p string
    fmt.Printf("%s: ", txt)
    fmt.Scanln(&p)
    y, err := strconv.Atoi(p)
    if err == nil && y >= n1 && y <= n2 { return y } else { fmt.Printf("Ошибка ввода! Необходимо ввести число от %d до %d!\n", n1, n2); return Num(txt, n1, n2)}
}

func Zad1(n int) int {
    if n == 1 { return 1 } else { return n * Zad1(n - 1) }
}

func Zad2(a, b int) int {
    if a == b { return a } else { return a + Zad2(a + 1, b) }
}

func Zad3(x int) string {
    if x == 0 { return "" } else { return "*" + Zad3(x - 1) }
}

func Zad4() {
    for i := 0; i < 3; i++ {
        fmt.Printf("%s\t\t%s\n %s | %s | %s\t\t %d | %d | %d\n", strings.Repeat("-", 11), strings.Repeat("-", 11), board[i*3], board[i*3+1], board[i*3+2], i*3+1, i*3+2, i*3+3)
    }
    fmt.Printf("%s\t\t%s\n\nХОД ИГРОКА: %s\n", strings.Repeat("-", 11), strings.Repeat("-", 11), player)
}

func Sklad(x int) int {
    y := 0
    for i := x; i < x + 10; i++ { y += mass[i]}
    return y
}
func Zad5(x int) {
    if x == 90 {
       min := mins[0]
       pos := 0
       for y, i := range mins { if i < min { min = i; pos = y } }
       fmt.Println("\nРЕШЕНИЕ:\nМассив:", mass, "\nМинимальная сумма 10 последовательных цифр: ", min, "\nПозиция начала последовательности: ", pos)
    } else { mins = append(mins, Sklad(x)); Zad5(x + 1) }
}

func Zad6(year1, month1, day1, year2, month2, day2 int) int {
    date1 := time.Date(year1, time.Month(month1), day1, 0, 0, 0, 0, time.UTC)
    date2 := time.Date(year2, time.Month(month2), day2, 0, 0, 0, 0, time.UTC)
    p := date2.Sub(date1)
    return int(p.Hours() / 24)
}

func main() {
    // Задание 1
    fmt.Println("ЗАДАНИЕ 1: Написать рекурсивную функцию нахождения степени числа.\n\nРЕШЕНИЕ:")
    fmt.Printf("\nРЕЗУЛЬТАТ: %d\n", Zad1(Num("Введите число", 1, 100)))

    // Задание 2
    fmt.Println("\n\nЗАДАНИЕ 2: Написать рекурсивную функцию, которая вычисляет сумму всех чисел в диапазоне от a до b. Пользователь вводит a и b. Проиллюстрируйте работу функции примером..\n\nРЕШЕНИЕ:")
    fmt.Printf("\nРЕЗУЛЬТАТ: %d\n", Zad2(Num("Введите число a", 0, 1000), Num("Введите число b", 0, 1000)))

    // Задание 3
    fmt.Println("\n\nЗАДАНИЕ 3: Написать рекурсивную функцию, которая выводит N звезд в ряд, число N задает пользователь. Проиллюстрируйте работу функции примером..\n\nРЕШЕНИЕ:")
    fmt.Printf("\nРЕШЕНИЕ: %s\n", Zad3(Num("Введите число N", 1, 100)))

    // Задание 4
    fmt.Println("Консольная игра \"Крестики-Нолики\"!\n\n    ПОЛЕ   \t\t НУМЕРАЦИЯ")
    Flag := true
    for Flag {
       Zad4()
       board[Num("Выберите позицию для хода", 1, 9) - 1] = player
       for _, val := range winList {
           if board[val[0]] == board[val[1]] && board[val[0]] == board[val[2]] && board[val[0]] != " " { Zad4(); fmt.Printf("\n\nИГРА ОКОНЧЕНА!\nПобедил игрок: %s\n\n", player); Flag = false }
       }
       nch := true
       for _, val := range board { if val == " " { nch = false } }
       if nch { Zad4(); fmt.Println("\n\nИГРА ОКОНЧЕНА!\nУ вас ничья!\n\n"); Flag = false }
       if player == "X" { player = "0" } else { player = "X" }
    }

    // Задание 5
    rand.Seed(time.Now().UnixNano())
    for len(mass) < 100 { mass = append(mass, rand.Intn(100)) }
    fmt.Println("Массив:", mass)
    fmt.Println("\n\nЗАДАНИЕ 5: Напишите рекурсивную функцию, которая принимает список из 100 целых чисел, полученных случайным образом, и находит позицию, с которой начинается последовательность из 10 чисел, сумма которых минимальна.\n")
    Zad5(0)

    // Задание 6
    fmt.Println("\n\nЗАДАНИЕ 6: Написать функцию, которая принимает две даты (т.е. функция принимает шесть параметров) и вычисляет разность в днях между этими датами.\n\nРЕШЕНИЕ:")
    fmt.Println("\nРЕЗУЛЬТАТ: Разница", Zad6(Num("Введите год 1", 1970, 2030), Num("Введите месяц 1", 1, 12), Num("Введите месяц 1", 1, 31), Num("Введите год 2", 1970, 2030), Num("Введите месяц 2", 1, 12), Num("Введите месяц 2", 1, 31)), "дней")
}
