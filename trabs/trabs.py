import numpy as np
from line_algorithms import analytic, dda, bresenham_line, bresenham_lineRemember, bresenham_lineRemember_clip
from circle_algorithms import parametric, bresenham_circle, symmetrical_increment, bezier_curve_parametric, casteljau
from fill_algorithms import flood_fill
from clip_algorithms import clip
from point import Point


class Plane:
    def __init__(self, size=90):
        self.size = size
        self.plane = np.empty((size, size), dtype=Point)
        for i in range(size):
            for j in range(size):
                self.plane[i][j] = Point(i, j, 0)
                
    def switch_pixel_color(self, x, y, color):
        if 0 <= self.size - y - 1 < self.size and 0 <= x < self.size:
            self.plane[self.size - y - 1][x].value = color

    def clear(self):
        for i in range(self.size):
            for j in range(self.size):
                self.plane[i][j].value = "\033[97mO\033[97m"

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
            self.plane[self.size - y - 1][x].value = "\033[92mX\033[92m"



def switch_case_menu():
    plane = Plane()
    p1 = Point(0, 0, 0)
    p2 = Point(0, 0, 0)
    pcirclecenter = Point(35, 35, 0)
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
        print("8. Bezier Curve: Casteljau Curve Algorithm")
        print("9. Bezier Curve: Parametric Curve Algorithm")
        print("10. Sutherland-Hodgman Clip Algorithm")
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
        elif choice == "8":
            num_points = int(input("Enter the number of control points for the Bezier curve: "))
            control_points = []
            for i in range(num_points):
                x = int(input(f"Enter the x-coordinate of point {i+1}: "))
                y = int(input(f"Enter the y-coordinate of point {i+1}: "))
                control_points.append(Point(x, y, 0))
                plane.switch_pixel_color(x, y, "\033[97mX\033[97m")  # Change color of control points
            casteljau(control_points, plane)
            plane.print("Algoritmo: Curva de Bézier com Algoritmo de Casteljau")
            plane.clear()

        elif choice == "9":
            num_points = int(input("Enter the number of control points for the Bezier curve: "))
            control_points = []
            for i in range(num_points):
                x = int(input(f"Enter the x-coordinate of point {i+1}: "))
                y = int(input(f"Enter the y-coordinate of point {i+1}: "))
                control_points.append(Point(x, y, 0))
                plane.switch_pixel_color(x, y, "X")
            bezier_curve_parametric(plane, control_points)
            plane.print("Algoritmo: Curva de Bézier Paramétrica")
            plane.clear()
        
        elif choice == "10":
            # Predefined points for the clip polygon
            clipPolygon = [Point(30, 30, 0), Point(30, 60, 0), Point(60, 60, 0), Point(60, 30, 0)]
            for i in range(len(clipPolygon)):
                point1 = clipPolygon[i]
                point2 = clipPolygon[(i+1) % len(clipPolygon)]
                bresenham_lineRemember(plane, point1, point2)

            # Predefined points for the subject polygons
            subjectPolygons = [
                [Point(35, 45, 0), Point(35, 80, 0), Point(55, 80, 0), Point(55, 45, 0), Point(50, 45, 0), Point(50, 65, 0), Point(40, 65, 0), Point(40, 45, 0)],
                # Add more subject polygons here as needed
            ]

            for subjectPolygon in subjectPolygons:
                clip(subjectPolygon, clipPolygon, plane)
                for i in range(len(subjectPolygon)):
                    point1 = subjectPolygon[i]
                    point2 = subjectPolygon[(i+1) % len(subjectPolygon)]
                    bresenham_lineRemember(plane, point1, point2)

            plane.print("Algoritmo: Sutherland-Hodgman Clip Algorithm")
            plane.clear()
                    
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

        input("Press Enter to continue...")

switch_case_menu()