package main

import (
    "fmt"
    "strconv"
    "strings"
    "os"
)

func GetOperation() string {
    var op string
    valid_ops := []string{"line", "circle", "fill", "curve"}

    fmt.Println("Operações disponíveis:")
    fmt.Println("\t'line' - desenhar reta")
    fmt.Println("\t'circle' - desenhar circunferencia")
    fmt.Println("\t'fill' - preenchimento de desenho")
    fmt.Println("\t'curve' - desenhar curva")
    fmt.Print("Qual operação você quer realizar? ")
    fmt.Scan(&op)

    for _, v := range valid_ops {
        if (op == v) {
            return op
        }
    }

    fmt.Println("Operação inválida") 
    os.Exit(1)
    return ""
}

func GetPoint(message string) Point {
    var pi string
    var pis []string

    fmt.Print(message)
    fmt.Scan(&pi)
    pis = strings.Split(pi, ",")
    x1, err := strconv.Atoi(pis[0])

    if err != nil {
        fmt.Println("Valor de X está inválido") 
        os.Exit(1) 
    }

    y1, err := strconv.Atoi(pis[1])
    
    if err != nil {
        fmt.Println("Valor de Y está inválido") 
        os.Exit(1) 
    }

    z1, err := strconv.Atoi(pis[2])

    if err != nil {
        fmt.Println("Valor de Z está inválido") 
        os.Exit(1) 
    }

    return CreatePoint(x1, y1, z1)
}

func GetRadius(message string) int {
    var pi string

    fmt.Print(message)
    fmt.Scan(&pi)
    r, err := strconv.Atoi(pi)

    if err != nil {
        fmt.Println("Valor do raio está inválido") 
        os.Exit(1) 
    }

    return r
}