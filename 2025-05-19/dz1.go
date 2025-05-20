package main

import (
    "fmt"
    "os"
    "strings"
    "slices"
)

func FileRead(name string) string {
    readFile, _ := os.ReadFile(name)
    return string(readFile)
}

// Функция ввоад числа с проверкой
func Num(txt string) string {
    var p string
    fmt.Printf("%s: ", txt)
    fmt.Scanln(&p)
    return p
}

func Revers(arr []string) []string {
    reversed := []string{}
    for i := 0; i < len(arr); i++ {
        reversed = append(reversed, arr[len(arr)-1-i])
    }
    return reversed
}

func main() {
    // Задание 1
    data := FileRead("text.txt")
    f, _ := os.Create("dz1_result1.txt")
    defer f.Close()
    for _, x := range strings.Split(data, "\n") {
        for _, y := range strings.Split(x, " ") {
            if len(y) > 6 { f.WriteString(y + "\n") }
        }
    }

    // Задание 2
    f, _ = os.Create("dz1_result2.txt")
    defer f.Close()
    for _, x := range strings.Split(data, "\n") { f.WriteString(x + "\n") }

    // Задание 3
    mass := Revers(strings.Split(data, "\n"))
    f, _ = os.Create("dz1_result3.txt")
    defer f.Close()
    for _, x := range mass { f.WriteString(x + "\n") }

    // Задание 4
    Flag := true
    for i :=0; i < len(mass); i++ {
        if strings.Contains(mass[i], ",") && Flag { mass = slices.Insert(mass, i, "************"); Flag = false }
    }
    if Flag { mass = append(mass, "************") }
    mass = Revers(mass)
    f, _ = os.Create("dz1_result4.txt")
    defer f.Close()
    for _, x := range mass { f.WriteString(x + "\n") }

    // Задание 5
    mass = Revers(strings.Split(data, "\n"))
    fmt.Println("Задание: 5")
    s := Num("Введите символ")
    i := 0
    for _, x := range mass {
        for _, y := range strings.Split(x, " ") {
            if strings.HasPrefix(y, s) { i += 1 }
        }
    }
    fmt.Printf("Резульатат: %d\n", i)

    // Задание 6
    f, _ = os.Create("dz1_result6.txt")
    defer f.Close()
    f.WriteString(strings.ReplaceAll(data, "*", "&"))

    // Задание 7
    mass = []string{"Mama mils ramu", "Uma turman", "Na pole tanki grohotali", "Ura!!!", "Ya ne narkoman" }
    f, _ = os.Create("dz1_result7.txt")
    defer f.Close()
    for _, x := range mass { f.WriteString(x + "\n") }

    // Задание 8
    f, _ = os.Create("dz1_result8.txt")
    defer f.Close()
    for _, x := range mass { f.WriteString(x + "\n") }

    // Задание 9
    fmt.Printf("\nЗадание 9\nКоличество символов: %d\n", len(data))

    // Задание 10
    fmt.Printf("\nЗадание 10\nКоличество символов: %d\n", len(strings.Split(data, "\n")))
}