// YouTube Video: https://www.youtube.com/watch?v=lLoYEft9tFk&t=0s&list=PL5tcWHG-UPH0jOCtEIpDNpbwOnhc6h9Om
// p14. Variadic Functions
package main

import "fmt"

func mult(nums ...int)int {
    accum_mult := 1
    for _, num := range nums {
        // accum_mult = accum_mult * num
        // shorthand:
        accum_mult *= num
    }
    return accum_mult
}

func main() {
    // function that takes an arbitrary number of args.

    // Println is an example:
    fmt.Println("this", "is", "an", "example", "of", "a", "variadic", "function")

    // Call mult function with as many variables as necessary
    fmt.Println(mult(1,2,3,4,5))

    // Variadic functions can also be applied to slices:
    nums := []int{1, 2, 3, 4}
    fmt.Println(mult(nums...))
}
