// YouTube Video: https://www.youtube.com/watch?v=XKdyN9kH4O0&t=0s&list=PL5tcWHG-UPH0jOCtEIpDNpbwOnhc6h9Om
// p.17 Pointers

package main

import "fmt"

func main(){
    val := 20

    fmt.Println(val)

    ptr := &val

    // print out the address where the value 20 is stored.
    fmt.Println(ptr)

    // print the value stored at the address (dereference)
    fmt.Println(*ptr)

    *ptr = 10

    fmt.Println(*ptr)
    fmt.Println(val)

    val = 50
    fmt.Println(*ptr)
}
