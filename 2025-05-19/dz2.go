package main

import (
    "fmt"
    "math"
    "os"
    "strings"
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

func main() {
    // Задание 1
    mass := strings.Split(FileRead("text.txt"), "\n")
    mass2 := strings.Split(FileRead("text2.txt"), "\n")
    fmt.Println("ЗАДАНИЕ 1:\n")
    for i := 0; i < int(math.Max(float64(len(mass)), float64(len(mass2)))); i++ {
        if i >= len(mass) { fmt.Printf("text2.txt\tСтрока: %d:\n%s\n\n", i + 1, mass2[i]); continue }
        if i >= len(mass2) { fmt.Printf("text.txt\tСтрока: %d:\n%s\n\n", i + 1, mass[i]); continue }
        if mass[i] != mass2[i] { fmt.Printf("text.txt:\tСтрока: %d\n%s\n\ntext2.txt:\tСтрока: %d\n%s\n\n", i + 1, mass[i], i + 1, mass2[i]) }
    }

    // Задаине 2
    data := FileRead("text.txt")
    znach := []int{0, 0, 0}
    glass := "aeiouyауоиэыяюеё"
    soglass := "bcdfghjklmnpqrstvxxzбвгджзйклмнпрстфхцчшщ"
    sifra :="0123456789"
    for i := 0; i < len(data); i ++ {
        if strings.Contains(glass, strings.ToLower(string(data[i]))) { znach[0] += 1 }
        if strings.Contains(soglass, strings.ToLower(string(data[i]))) { znach[1] += 1 }
        if strings.Contains(sifra, string(data[i])) { znach[2] += 1 }
    }
    x := len(strings.Split(data, "\n"))
    f, _ := os.Create("dz2_result2.txt")
    defer f.Close()
    f.WriteString(fmt.Sprintf("Количество символов: %d\nКоличество строк: %d\nКоличество гласных: %d\nКоличество согласных: %d\nКоличество цифр: %d", len(data), x, znach[0], znach[1], znach[2]))

    // Задание 3
    mass = strings.Split(FileRead("text.txt"), "\n")
    mass = mass[:len(mass) - 1]
    f, _ = os.Create("dz2_result3.txt")
    defer f.Close()
    for _, line := range mass {
        f.WriteString(line + "\n")
    }

    // Задание 4
    mass = strings.Split(FileRead("text.txt"), "\n")
    i := len(mass[0])
    for y := 0; y < len(mass); y++ { if len(mass[y]) > i { i = len(mass[y]) } }
    fmt.Printf("ЗАДАНИЕ 4:\nДлинна самой длинной строки: %d\n\n", i)

    // Задание 5
    data = FileRead("text.txt")
    fmt.Println("ЗАДАНИЕ 5:")
    fmt.Printf("Встречается: %d раз\n\n", strings.Count(data, Num("Введите заданное слово")))

    // Задаие 6
    fmt.Println("ЗАДАНИЕ 6:")
    f, _ = os.Create("text.txt")
    defer f.Close()
    f.WriteString(strings.ReplaceAll(data, Num("Введите слово для замены"), Num("Введите на что заменить")))
}