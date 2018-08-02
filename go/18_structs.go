// YouTube Video: https://www.youtube.com/watch?v=fR2r67nQUHQ&t=0s&list=PL5tcWHG-UPH0jOCtEIpDNpbwOnhc6h9Om
// p.18 Structs

package main

import "fmt"

type employee struct {
    first_name string
    last_name string
    id int
}

func main(){

    // Printing result of employee
    fmt.Println(employee{first_name: "Homer", last_name: "Simpson", id: 1})

    // No need to explicitly specify the field:
    fmt.Println(employee{"Whalen", "Smithers", 2})

    // If a field is omitted, it is zero-valued
    // (for string that's an empty string, for int that's 0)
    fmt.Println(employee{first_name: "Frank", last_name: "Grimes"})

    // Store an employee object into a variable:
    emp := employee{first_name: "Montgomery", last_name: "Burns", id: 4}

    // Can access the fields of an employee object:
    fmt.Println(emp.first_name)
    fmt.Println(emp.last_name)
    fmt.Println(emp.id)

    // Can define a pointer to a struct
    emp_ptr := &emp
    fmt.Println(emp_ptr.first_name)

    // Updating the field first name in the struct via pointer.
    emp_ptr.first_name = "Marge"
    fmt.Println(emp_ptr.first_name)
    fmt.Println(emp.first_name)

}
