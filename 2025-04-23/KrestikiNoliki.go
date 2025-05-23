package main

import (
    "fmt"
    "strconv"
    "strings"
    "os"
)

var (
    board = [9]string {" "," "," "," "," "," "," "," "," "} // игровая доска
    winList = [8][3] int {{0,1,2}, {3,4,5}, {6,7,8}, {0,3,6}, {1,4,7}, {2,5,8}, {0,4,8}, {2,4,6}} // Выигрышные комбинации
    player string = "X" // Ход игрока
)

// Функция ввоад числа с проверкой
func Num(txt string) int {
    var x string
    fmt.Printf("%s: ", txt)
    fmt.Scanln(&x)
    y, err := strconv.Atoi(x)
    if err == nil && y > 0 && y < 10 && board[y - 1] == " " { return y } else { fmt.Println("Ошибка ввода! Нужно ввести незанятую позицию от 1 до 9!\n"); return Num(txt) }
}

// Вывод игрового поля
func Doska() {
    fmt.Println("\033[H\033[2JКонсольная игра \"Крестики-Нолики\"!\n\n    ПОЛЕ   \t\t НУМЕРАЦИЯ")
    for i := 0; i < 3; i++ {
        fmt.Printf("%s\t\t%s\n %s | %s | %s\t\t %d | %d | %d\n", strings.Repeat("-", 11), strings.Repeat("-", 11), board[i*3], board[i*3+1], board[i*3+2], i*3+1, i*3+2, i*3+3)
    }
    fmt.Printf("%s\t\t%s\n\nХОД ИГРОКА: %s\n", strings.Repeat("-", 11), strings.Repeat("-", 11), player)
}

// Игровой процесс
func main() {
    for {
       Doska()
       board[Num("Выберите позицию для хода") - 1] = player
       for _, val := range winList {
           if board[val[0]] == board[val[1]] && board[val[0]] == board[val[2]] && board[val[0]] != " " { Doska(); fmt.Printf("\n\nИГРА ОКОНЧЕНА!\nПобедил игрок: %s\n\n", player); os.Exit(0) }
       }
       nch := true
       for _, val := range board { if val == " " { nch = false } }
       if nch { Doska(); fmt.Println("\n\nИГРА ОКОНЧЕНА!\nУ вас ничья!\n\n"); break }
       if player == "X" { player = "0" } else { player = "X" }
    }
}
