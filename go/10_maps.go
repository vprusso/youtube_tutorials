// YouTube Video: https://www.youtube.com/watch?v=XQre3ILIVH0&t=0s&list=PL5tcWHG-UPH0jOCtEIpDNpbwOnhc6h9Om
// p.10 Maps
package main

import "fmt"

func main() {
    // maps are similar to Python dictionary

    // specify key/value pair
    m := make(map[string]int)

    m["a"] = 0
    m["b"] = 1

    fmt.Println(m)

    // Printing value of specific key:
    fmt.Println(m["a"])

    // len() function is overloaded to work with maps:
    fmt.Println(len(m))

    // remove key/value pair can be done with delete:
    delete(m, "a")
    fmt.Println(m)

    // another way to initialize a map if you know the values/keys
    // ahead of time.
    m2 := map[string]int{"val1": 1, "val2": 2}
    fmt.Println(m2)

    // the value and whether the value is present is returned here 
    val, is_val_present := m["b"]
    fmt.Println(val)
    fmt.Println(is_val_present)

    // one can use the "_" placeholder is the value is not needed. 
    _, is_val_present_val3 := m2["val3"]
    fmt.Println(is_val_present_val3)


}
