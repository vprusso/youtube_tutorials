// YouTube Video: https://www.youtube.com/watch?v=PzvcYZ2hy6A&t=0s&list=PL5tcWHG-UPH0jOCtEIpDNpbwOnhc6h9Om
// p.9 Slices
package main

import "fmt"

func main() {
    s := make([]int, 3)

    // Similar to array:
    s[0] = 1
    s[1] = 2
    s[2] = 3
    fmt.Println(s)

    fmt.Println(s[0])
    fmt.Println(len(s))

    // append function is unique to slices
    s = append(s, 4)
    s = append(s, 5, 6)
    fmt.Println(s)

    // slice syntax
    fmt.Println(s[1:3])

    fmt.Println(s[:3])

    fmt.Println(s[1:])

    // concise slice definition:
    t := []int{100, 200, 300}
    fmt.Println(t)

    //x := s
    //x[0] = 500
    //fmt.Println(x)
    //fmt.Println(s)

    // Use copy to prevent from changing both x and s
    x := make([]int, len(s))
    copy(x, s)

    x[0] = 500
    fmt.Println(x)
    fmt.Println(s)

    // 2-D slices (similar to arrays, although lengths can vary.
    ss := make([][]int, 3)
    for i := 0; i < 3; i++ {
        inner_len := i + 1
        ss[i] = make([]int, inner_len)
        for j := 0; j < inner_len; j++ {
            ss[i][j] = i + j
        }
    }
    fmt.Println(ss)


}

