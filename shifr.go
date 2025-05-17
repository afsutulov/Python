package main

import (
    "os"
    "io/ioutil"
)

func main() {
    key := map[int]int{ 0: 3, 1: 6, 2: 8, 3: 0, 4: 7, 5: 9, 6: 1, 7: 4, 8: 2, 9: 5 }
    args := os.Args
    if len(args) != 2 { return }
    data, err := ioutil.ReadFile(args[1])
    if err != nil { return }
    for i := 0; i < len(data); i ++ {
       if i % 10 < key[i % 10] && i / 10 * 10 + key[i % 10] < len(data){ data[i], data[i / 10 * 10 + key[i % 10]] = data[i / 10 * 10  + key[i % 10]], data[i] }
       data[i] = 255 - data[i]
    }
    err = ioutil.WriteFile(args[1], data, 0644)
}
