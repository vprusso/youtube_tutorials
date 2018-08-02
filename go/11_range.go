// YouTube Video: https://www.youtube.com/watch?v=ne4cLmDrqgM&t=0s&list=PL5tcWHG-UPH0jOCtEIpDNpbwOnhc6h9Om
// p11. Range

package main

import "fmt"

func main() {
    // range is similar to range in Python:
    str_arr := []string{"a", "b", "c", "d"}
    for i, str := range str_arr {
        fmt.Println("idx", i)
        fmt.Println("str", str)
    }

    // can also range over key/value pairs in maps:
    m := map[string]int{"a": 1, "b": 2, "c": 3, "d" : 4}
    for k, v := range m {
        fmt.Println("key:", k, "value:", v)
    }

    // can also just range over the keys in maps:
    for k := range m {
        fmt.Println("key:", k)
    }

}
