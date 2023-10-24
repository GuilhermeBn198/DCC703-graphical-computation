import numpy as np
from line_algorithms import analytic, dda, bresenham_line
from circle_algorithms import parametric, bresenham_circle, symmetrical_increment

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

    while True:
        print("Menu:")
        print("1. Analytic Line Algorithm")
        print("2. DDA Line Algorithm")
        print("3. Bresenham Line Algorithm")
        print("4. Parametric Circle Algorithm")
        print("5. Symmetrical Increment Circle Algorithm")
        print("6. Bresenham Circle Algorithm")
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
        elif choice == "2":
            p1.x = int(input("Enter the x-coordinate of point 1: "))
            p1.y = int(input("Enter the y-coordinate of point 1: "))
            p2.x = int(input("Enter the x-coordinate of point 2: "))
            p2.y = int(input("Enter the y-coordinate of point 2: "))
            p1 = Point(p1.x, p1.y, 0)
            p2 = Point(p2.x, p2.y, 0)
            dda(plane, p1, p2)
        elif choice == "3":
            p1.x = int(input("Enter the x-coordinate of point 1: "))
            p1.y = int(input("Enter the y-coordinate of point 1: "))
            p2.x = int(input("Enter the x-coordinate of point 2: "))
            p2.y = int(input("Enter the y-coordinate of point 2: "))
            p1 = Point(p1.x, p1.y, 0)
            p2 = Point(p2.x, p2.y, 0)
            bresenham_line(plane, p1, p2)
        elif choice == "4":
            pcircle = input("Enter the radius of the circle: ")
            parametric(plane, pcirclecenter, int(pcircle))
        elif choice == "5":
            pcircle = input("Enter the radius of the circle: ")
            symmetrical_increment(plane, pcirclecenter, int(pcircle))
        elif choice == "6":
            pcircle = input("Enter the radius of the circle: ")
            bresenham_circle(plane, pcirclecenter, int(pcircle))
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

        input("Press Enter to continue...")

switch_case_menu()