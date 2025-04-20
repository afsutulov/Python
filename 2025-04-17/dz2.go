package main

import (
    "fmt"
    "unicode"
    "strconv"
    "strings"
)

// Функция ввоад числа с проверкой
func Num(txt string) int {
    var x string
    for {
        fmt.Print(txt, ": ")
        fmt.Scanln(&x)
        Flag := true
        for _, char := range x {
            if !unicode.IsDigit(char) { Flag = false; break }
        }
        if Flag { y, _ := strconv.Atoi(x); return y } else { fmt.Println("Ошибка: Введенные данные не содержат чило!\n") } 
    }
}

func main() {
   // Задание 1
   for {
       val := strconv.Itoa(Num("Введите шестизначное число"))
       if len(val) == 6 {
          if int(val[0]) * int(val[1]) * int(val[2]) == int(val[3]) * int(val[4]) * int(val[5]) {
             fmt.Println("Число счастливое!\n")
          } else {
             fmt.Println("Число несчастливое!\n")
          }
          break
       } else {
         fmt.Println("Ошибка: Введено не шестизначное число!\n")
       }
   }

   // Задание 2
   for {
       val := strconv.Itoa(Num("Введите шестизначное число"))
       if len(val) == 6 {
          fmt.Println(strings.ReplaceAll(string(val[5])+string(val[4])+string(val[2])+string(val[3])+string(val[1])+string(val[0]), " ", ""),"\n")
          break
       } else {
         fmt.Println("Ошибка: Введено не шестизначное число!\n")
       }
   }

   //  Задание 3
   for {
       val := Num("\nВведите номер месяца")
       switch val {
          case 1, 2, 12: fmt.Println("Winter")
          case 3, 4, 5: fmt.Println("Spring")
          case 6, 7, 8: fmt.Println("Summer")
          case 9, 10, 11: fmt.Println("Autumn")
          default: {
             fmt.Println("Ошибка: Введен некорректный месяц!")
             continue
          }
       }
       break
   }
}
