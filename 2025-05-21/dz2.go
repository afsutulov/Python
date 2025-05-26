package main

import (
    "fmt"
    "strconv"
    "encoding/json"
    "io/ioutil"
    "os"
)

type Data struct {
    famaly string
    name string
    age int
}

var data []Data

// Функция ввоад числа с проверкой
func Num(txt string, n1, n2 int) int {
    var p string
    fmt.Printf("%s: ", txt)
    fmt.Scanln(&p)
    y, err := strconv.Atoi(p)
    if err == nil && y >= n1 && y <= n2 { return y } else { fmt.Printf("Ошибка ввода! Необходимо ввести число от %d до %d!\n", n1, n2); return Num(txt, n1, n2)}
}

// Функция ввоад числа с проверкой
func NumT(txt string) string {
    var p string
    fmt.Printf("%s: ", txt)
    fmt.Scanln(&p)
    return p
}

// Функция вывода списка сотрудников
func Peoples() {
    fmt.Printf("СПИСОК СОТРУДНИКОВ:\n--------------------------------------------------------------\n|   №  |       ФАМИЛИЯ       |         ИМЯ        | ВОЗРАСТ |\n--------------------------------------------------------------")
    if len(data) == 0 { fmt.Println("список пуст") }
    for i, x := range data { fmt.Printf("| %5d| %-20s| %-20s| %-8d|", i, x.famaly, x.name, x.age) }
    fmt.Println("--------------------------------------------------------------\n")
}

// Функция добавления пользователя
func AddPeople() {
    fmt.Println("\nДОБАВЛЕНИЕ СОТРУДНИКА")
    data = append(data, Data{famaly: NumT("\tВведите Фамилию сотрудника: "), name: NumT("\tВведите Имя сотрудника: "), age: Num("\tВведите возраст сотрудника", 18, 100)})
}

// Функцтя удаления пользователя
func DelPeople() {
    fmt.Println("\nУДАЛЕНИЕ СОТРУДНИКА")
//    data.pop(Num("Введите сотрудника, которого необходимо удалить",1, len(data)) - 1)
}

// Функция редактирования данных пользователя
func EditPeople() {
    fmt.Println("\nРЕДАКТИРОВАНИЕ ДАННЫХ СОТРУДНИКА")
//    i := Num("Введите номер сотрудника для редактирования", 1, len(data)) - 1
//    data[i].famaly = NumT(fmt.Sprintf("\nПредыдущие фамилия: %s\nВведите новую Фаилию: ", data[i]["famaly"]))
//    data[i].name = NumT(fmt.Sprintf("\nПредыдущие фамилия: %s\nВведите новую Фаилию: ", data[i]["name"]))
//    data[i].age = NumT(fmt.Sprintf("\nПредыдущие фамилия: %d\nВведите новую Фаилию", data[i]["age"]))
}

// Функция поиска сотрудников по фамилии
func SearchFamily() {
    fmt.Println("\nПОИСК СОТРУДНИКОВ ПО ФАМИЛИИ")
    f := NumT("Введите Фамилию для поиска: ")
//    var tmp Data
    for _, x := range data {
//        if x.famaly == f { fmt.Printf("Фамилия: %-20sИмя: %-20s\tВозраст: %d\n", x.famaly, x.name, x.age); tmp = append(tmp, x) }
        if x.famaly == f { fmt.Printf("Фамилия: %-20sИмя: %-20s\tВозраст: %d\n", x.famaly, x.name, x.age) }
    }
//    if len(tmp) != 0 { SaveDataFile(tmp) }
}

// Функция поиска сотрудников по возрасту
func SearchAge() {
    fmt.Println("\nПОИСК СОТРУДНИКОВ ПО ВОЗРАСТУ")
    f := Num("Введите возраст для поиска: ", 18, 100)
//    var tmp Data
    for _, x := range data {
//        if x.age == f { fmt.Printf("Фамилия: %-20sИмя: %-20s\tВозраст: %d\n", x.famaly, x.name, x.age); tmp = append(tmp, x) }
        if x.age == f { fmt.Printf("Фамилия: %-20sИмя: %-20s\tВозраст: %d\n", x.famaly, x.name, x.age) }
    }
//    if len(tmp) != 0 { SaveDataFile(tmp) }
}

// Функция поиска сотрудников по первой букве фамилии
func SearchFamS() {
    fmt.Println("\nПОИСК СОТРУДНИКОВ ПО ПЕРВОЙ БУКВЕ ФАМИЛИИ")
    f := ""
    for len(f) != 1 { f = NumT("Введите первую букву фамилии: ") }
//    var tmp Data
    for _, x := range data {
//        if x.famaly[0] == f { fmt.Printf("Фамилия: %-20sИмя: %-20s\tВозраст: %d\n", x.famaly, x.name, x.age); tmp = append(tmp, x) }
        if x.famaly[0:1] == f { fmt.Printf("Фамилия: %-20sИмя: %-20s\tВозраст: %d\n", x.famaly, x.name, x.age) }
    }
//    if len(tmp) != 0 { SaveDataFile(tmp) }
}

// Функция загрузкти данных из файла
func LoadFile(x string) []Data {
    file, err := os.Open(x)
    if err != nil { fmt.Println("Не удалось загрузить данные из файла ", x); return }
    defer file.Close()
    d, _ := ioutil.ReadAll(file)
//    type Personal struct {
//        famaly string `json:"famaly"`
//        name string `json:"name"`
//        age int `json:"age"`
//    }
//    var personal Personal
    var personal Data
    _ = json.Unmarshal(d, &personal)
    return personal
}

// Функция сохранения результатов поиска в файл
func SaveDataFile(x string) {
    switch Num("\n\nСохранить результаты поиска в файл (0 - нет, 1 - да)?", 0, 1) {
        case 1: SaveFile(NumT("Введите имя файла для сохранения данных поиска"), x)
    }
}

// Функция сохранения данных в файл
func SaveFile(x string, y Data) {
    jsonData, _ := json.Marshal(y)
    _ = ioutil.WriteFile(x, jsonData, 0644)
    fmt.Printf("\nДанные сохранены в файл: %s!\n", x)
}

// Тело программы
func main() {
    data = LoadFile(NumT("Введите имя файла из которого необходимо загрузить сохраненные данные (при выходе данные автоматически сохраняются в dz2_result.json): "))
    for {
        Peoples()
        switch Num("\nДействия:\n\t1. Вывести список всех сотрудников\n\t2. Добавить сотрудника\n\t3. Редактировать данные сотрудника\n\t4. Удалить сотрудника\n\t5. Поиск сотрудников по фамилии\n\t6. Поиск сотрудников по возрасту\n\t7. Поиск сотрудников по первой букве\n\t8. Загрузить данные из файла\n\t9. Сохранить данные в файл\n\t0 - Выход\n\nВведите действие", 0, 9) {
            case 0: SaveFile("dz2_result.json", data); break
            case 1: Peoples()
            case 2: AddPeople()
            case 3: EditPeople()
            case 4: DelPeople()
            case 5: SearchFamily()
            case 6: SearchAge()
            case 7: SearchFamS()
            case 8: data = LoadFile(NumT("Введите название файла: "));
            case 9: SaveFile("dz2_result.json", data)
        }
    }
}