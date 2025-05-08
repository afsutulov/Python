package main

import (
    "fmt"
    "math/rand"
    "strconv"
)

var (
    idcode	= []int {}
    phone	= []int {}
    kniga	= []string {"Укурки", "Пермские нарколыги", "Курим шмаль", "Мысли наркомана", "Курить или не курить", "Дурь в башке", "Лучше бы пил", "Горе от ЗОЖ", "Пил и буду пить", "Шмаль forever!"}
    god		=[]int {}
)

// Функция ввоад числа с проверкой
func Num(txt string, n1, n2 int) int {
    var p string
    fmt.Printf("%s: ", txt)
    fmt.Scanln(&p)
    y, err := strconv.Atoi(p)
    if err == nil && y >= n1 && y <= n2 { return y } else { fmt.Printf("Ошибка ввода! Необходимо ввести число от %d до %d!\n", n1, n2); return Num(txt, n1, n2)}
}

func Zad1() {
    fmt.Println("\n\tСправочник:")
    for i := 0; i < len(idcode); i++ { fmt.Printf("ID = %-4dPHONE = %d\n", idcode[i], phone[i]) }
}

func Sort1(Flag bool) {
    for i := 0; i < len(idcode); i++ {
       for j := 0; j < len(idcode); j++ {
          if Flag { if idcode[i] < idcode[j] { idcode[i], idcode[j] = idcode[j], idcode[i]; phone[i], phone[j] = phone[j], phone[i] }
          } else { if phone[i] < phone[j] { idcode[i], idcode[j] = idcode[j], idcode[i]; phone[i], phone[j] = phone[j], phone[i] } }
       }
    }
}

func Zad2() {
    fmt.Println("\n\tКниги:")
    for i := 0; i < len(kniga); i++ { fmt.Printf("%-20s\tГод: %d\n", kniga[i], god[i]) }
}

func Sort2(Flag bool) {
    for i := 0; i < len(kniga); i++ {
       for j := 0; j < len(god); j++ {
          if Flag { if kniga[i] < kniga[j] { kniga[i], kniga[j] = kniga[j], kniga[i]; god[i], god[j] = god[j], god[i] }
          } else { if god[i] < god[j] { kniga[i], kniga[j] = kniga[j], kniga[i]; god[i], god[j] = god[j], god[i] } }
       }
    }
}

func main() {
    // Задание 1
    for len(idcode) < 10 { idcode = append(idcode, rand.Intn(98) + 1) }
    for len(phone) < 10 { phone = append(phone, rand.Intn(1000) + 600000) }
    fmt.Println("ЗАДАНИЕ 1: Написать программу «справочник». Создать два списка целых. Один список хранит идентификационные коды, второй — телефонные номера. Реализовать меню для пользователя:\n - отсортировать по идентификационным кодам;\n - Отсортировать по номерам телефона;\n - Вывести список пользователей с кодами и телефонами;\n - Выход.\n\nРЕШЕНИЕ:")
    Zad1()
    switch Num("\nВарианты:\n\t1 - отсортировать по ID\n\t2 - отсортировать по PHONE\n\t3 - Вывести изначальный список\n\t0 - Выход\nВыберите дейстие", 0, 3) {
       case 1: Sort1(true); Zad1()
       case 2: Sort1(false); Zad1()
       case 3: Zad1()
    }

    // Задание 2
    fmt.Println("\n\nЗАДАНИЕ 2: Написать программу «книги». Создать два списка с данными. Один список храни название книг, второй - годы выпуска. Реализовать меню для пользователя:\n - Отсортировать по названию книг;\n - Отсортировать по годам выпуска;\n - Вывести список книг с названиями и годами выпуска;\n - Выход\n\nРЕШЕНИЕ:")
    for len(god) < 10 { god = append(god, rand.Intn(54) + 1970) }
    Zad2()
    switch Num("\nВарианты:\n\t1 - отсортировать по названию\n\t2 - отсортировать по году\n\t3 - Вывести изначальный список\n\t0 - Выход\nВыберите дейстие", 0, 3) {
       case 1: Sort2(true); Zad2()
       case 2: Sort2(false); Zad2()
       case 3: Zad2()
    }
}