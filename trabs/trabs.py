import numpy as np
from line_algorithms import analytic, dda, bresenham_line, bresenham_lineRemember
from circle_algorithms import parametric, bresenham_circle, symmetrical_increment
from fill_algorithms import flood_fill

class Point:
    def __init__(self, x, y, z, value="\033[90mO\033[39m"):
        self.x = x
        self.y = y
        self.z = z
        self.value = value

class Plane:
    def __init__(self, size=50):
        self.size = size
        self.plane = np.empty((size, size), dtype=Point)
        for i in range(size):
            for j in range(size):
                self.plane[i][j] = Point(i, j, 0)

    def clear(self):
        for i in range(self.size):
            for j in range(self.size):
                self.plane[i][j].value = "\033[90mO\033[39m"

    def print(self, name=""):
        if name:
            print(name)
        for i in range(self.size):
            for j in range(self.size):
                print(self.plane[i][j].value, end=" ")
            print("|")
        print("\n")

    def animated_print(self, name=""):
        if name:
            print(name)
        for i in range(self.size):
            for j in range(self.size):
                print(self.plane[i][j].value, end=" ")
            print("|")
        print("\n")

    def switch_pixel(self, x, y):
        if 0 <= self.size - y - 1 < self.size and 0 <= x < self.size:
            self.plane[self.size - y - 1][x].value = "\033[91mX\033[39m"



def switch_case_menu():
    plane = Plane()
    p1 = Point(0, 0, 0)
    p2 = Point(0, 0, 0)
    pcirclecenter = Point(25, 25, 0)
    pcirclecenter2 = Point(20, 10, 0)

    while True:
        print("Menu:")
        print("1. Analytic Line Algorithm")
        print("2. DDA Line Algorithm")
        print("3. Bresenham Line Algorithm")
        print("4. Parametric Circle Algorithm")
        print("5. Symmetrical Increment Circle Algorithm")
        print("6. Bresenham Circle Algorithm")
        print("7. Flood Fill Algorithm")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            p1.x = int(input("Enter the x-coordinate of point 1: "))
            p1.y = int(input("Enter the y-coordinate of point 1: "))
            p2.x = int(input("Enter the x-coordinate of point 2: "))
            p2.y = int(input("Enter the y-coordinate of point 2: "))
            p1 = Point(p1.x, p1.y, 0)
            p2 = Point(p2.x, p2.y, 0)
            analytic(plane, p1, p2)
            plane.print("Algoritmo: Método Analítico")
            plane.clear()
        elif choice == "2":
            p1.x = int(input("Enter the x-coordinate of point 1: "))
            p1.y = int(input("Enter the y-coordinate of point 1: "))
            p2.x = int(input("Enter the x-coordinate of point 2: "))
            p2.y = int(input("Enter the y-coordinate of point 2: "))
            p1 = Point(p1.x, p1.y, 0)
            p2 = Point(p2.x, p2.y, 0)
            dda(plane, p1, p2)
            plane.print("Algoritmo: DDA")
            plane.clear()
        elif choice == "3":
            p1.x = int(input("Enter the x-coordinate of point 1: "))
            p1.y = int(input("Enter the y-coordinate of point 1: "))
            p2.x = int(input("Enter the x-coordinate of point 2: "))
            p2.y = int(input("Enter the y-coordinate of point 2: "))
            p1 = Point(p1.x, p1.y, 0)
            p2 = Point(p2.x, p2.y, 0)
            bresenham_line(plane, p1, p2)
            plane.print("Algoritmo: Bresenham")
            plane.clear()
        elif choice == "4":
            pcircle = input("Enter the radius of the circle: ")
            parametric(plane, pcirclecenter, int(pcircle))
            plane.print("Algoritmo: Equação Paramétrica")
            plane.clear()
        elif choice == "5":
            pcircle = input("Enter the radius of the circle: ")
            symmetrical_increment(plane, pcirclecenter, int(pcircle))
            plane.print("Algoritmo: Incremental com Simetria")
            plane.clear()
        elif choice == "6":
            pcircle = input("Enter the radius of the circle: ")
            bresenham_circle(plane, pcirclecenter, int(pcircle))
            plane.print("Algoritmo: Bresenham")
            plane.clear()
        elif choice == "7":
            replacement_color = input("Enter the replacement letter (e.g., x, =, ., a, b): ")
            
            # square
            p1 = Point(15, 15, 0)
            p2 = Point(30, 15, 0)
            p3 = Point(15, 30, 0)
            p4 = Point(30, 30, 0)
            bresenham_lineRemember(plane, p1,p2)
            bresenham_lineRemember(plane, p2,p4)
            bresenham_lineRemember(plane, p3,p4)
            bresenham_lineRemember(plane, p1,p3)
            plane.print()
            input()
            flood_fill(plane, pcirclecenter.x, pcirclecenter.y, replacement_color)
            input()
            
            # circle
            pcircle = input("Enter the radius of the circle: ")
            bresenham_circle(plane, pcirclecenter, int(pcircle))
            plane.print()
            input()
            flood_fill(plane, pcirclecenter.x, pcirclecenter.y, replacement_color)
            input()
            plane.clear

            # plane a)
            plane.clear()
            p1 = Point(10, 10, 0)
            p2 = Point(20, 15, 0)
            p3 = Point(5, 25, 0)
            p4 = Point(25, 35, 0)
            p5 = Point(45, 20, 0)
            p6 = Point(35, 12, 0)
            bresenham_lineRemember(plane, p1,p2)
            bresenham_lineRemember(plane, p3,p2)
            bresenham_lineRemember(plane, p3,p4)
            bresenham_lineRemember(plane, p4,p5)
            bresenham_lineRemember(plane, p6,p5)
            bresenham_lineRemember(plane, p1,p6)
            plane.print()
            input()
            flood_fill(plane, pcirclecenter.x, pcirclecenter.y, replacement_color)
            input()

            # plane C)
            plane.clear()
            p0 = Point(7, 15, 0)
            p1 = Point(3, 35, 0)
            p2 = Point(25, 40, 0)
            p3 = Point(35, 35, 0)
            p4 = Point(38, 20, 0)
            p5 = Point(20, 5, 0)
            p6 = Point(15, 25, 0)
            p7 = Point(30, 30, 0)
            p8 = Point(30, 20, 0)
            bresenham_lineRemember(plane, p1,p0)
            bresenham_lineRemember(plane, p1,p2)
            bresenham_lineRemember(plane, p2,p3)
            bresenham_lineRemember(plane, p3,p4)
            bresenham_lineRemember(plane, p5,p4)
            bresenham_lineRemember(plane, p6,p5)
            bresenham_lineRemember(plane, p6,p7)
            bresenham_lineRemember(plane, p7,p8)
            bresenham_lineRemember(plane, p0,p8)
            plane.print()
            input()
            flood_fill(plane, pcirclecenter.x, pcirclecenter.y, replacement_color)
            flood_fill(plane, pcirclecenter2.x, pcirclecenter2.y, replacement_color)
            plane.clear()
            
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

        input("Press Enter to continue...")

switch_case_menu()