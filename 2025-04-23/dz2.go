package main

import (
    "fmt"
    "strings"
    "bufio"
    "os"
)

// Функция ввоад числа с проверкой
func Num(txt string) string {
    fmt.Printf("%s: ", txt)
    in := bufio.NewReader(os.Stdin)
    line, _ := in.ReadString('\n')
    return strings.Trim(line, "\n")
}

func Reverse(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}

func main() {
    // Задание 1
    fmt.Println("ЗАДАНИЕ1: Пользователь вводит с клавиатуры строку. Проверьте является ли введенная строка палиндромом. Палин слева направо и справа налево.\n\nРЕШЕНИЕ:")
    txt := strings.ReplaceAll(strings.ToLower(Num("Введите строку")), " ", "")
    fmt.Println(strings.ReplaceAll(strings.ReplaceAll(fmt.Sprintf("РЕЗУЛЬТАТ: Слово %t палиндромом\n", txt == Reverse(txt)), "true", "является"), "false", "не является"))

    // Задание 2
    fmt.Println("\n\nЗАДАНИЕ2: Пользователь вводит с клавиатуры некоторый текст, после чего пользователь вводит список зарезервированных слов. Необходимо найти в тексте все зарезервированные слова и изменить их регистр на верхний. Вывести на экран измененный текст.\n\nРЕШЕНИЕ:")
    txt = Num("Введите строку")
    for {
       t := Num("Введите зарезервированное слово. Для завершения нажмите Enter")
       if t == "" { break }
       txt = strings.ReplaceAll(txt, t, strings.ToUpper(t))
    }
    fmt.Printf("\nРЕЗУЛЬТАТ: %s\n", txt)

    // Задание 3
    fmt.Println("\n\nЗАДАНИЕ3: Есть некоторый текст. Посчитайте в этом тексте количество предложений и выведите на экран полученный результат.\n\nРЕШЕНИЕ:")
    txt = Num("Введние текст")
    if !strings.HasSuffix(txt, ".") { txt += "." }
    fmt.Printf("\n\nРЕЗУЛЬТАТ: %d\n", strings.Count(txt, "."))
}
