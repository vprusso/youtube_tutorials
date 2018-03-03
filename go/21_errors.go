// p.21 Errors

package main

import (
    "errors"
    "fmt"
)

func errorExample(arg string) (string, error) {
    if arg == "No" {
        return "", errors.New("Input No is not valid")
    }
    return "Input " + arg + " is valid", nil
}

// Custom types as errors (use built-in Error() function)
type argError struct {
    arg string
    prob string
}

func (e *argError) Error() string {
    return fmt.Printf("%s - %s", e.arg, e.prob)
}

func customErrorExample(arg string) (string, error) {
    if arg == "No" {
        return "", &argError{arg, "Input No is not valid"}
    }
    return "Input " + arg + " is valid", nil
}


func main(){
}
