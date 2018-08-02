// YouTube Video: https://www.youtube.com/watch?v=oYVbA9YthlA&t=0s&list=PL5tcWHG-UPH0jOCtEIpDNpbwOnhc6h9Om
// p.8 Arrays

package main

import "fmt"

func main() {
    var int_arr [5]int

    fmt.Println(int_arr)

    var bool_arr[10]bool

    fmt.Println(bool_arr)

    int_arr[0] = 5
    int_arr[1] = 10

    fmt.Println(int_arr)

    fmt.Println(int_arr[0])

    a := [5]int{1, 2, 3, 4, 5}
    fmt.Println(a)

    fmt.Println(len(a))
    fmt.Println(len(bool_arr))

    var aa[5][5]int
    count := 0
    for i := 0; i < 5; i++ {
        for j := 0; j < 5; j++ {
            aa[i][j] = count
            count = count + 1
        }
    }
    fmt.Println(aa)
}
