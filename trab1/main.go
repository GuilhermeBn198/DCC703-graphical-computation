package main

func main() {
    p := CreatePlane()

    op := GetOperation()

    switch op {
    case "line":
        p1 := GetPoint("Coordenadas do primeiro ponto (Ex: 5,2,1): ")
        p2 := GetPoint("Coordenadas do segundo ponto (Ex: 9,3,1): ")

        Analytic(p, p1, p2)
        DDA(p, p1, p2)
        BresenhamLine(p, p1, p2)
    case "circle":
        p1 := GetPoint("Coordenadas do centro (Ex: 5,2,1): ")
        r := GetRadius("Comprimento do raio (Ex: 1): ")

        Parametric(p, p1, r)
        SymmetricalIncrement(p, p1, r)
        BresenhamCircle(p, p1, r)
    }
}