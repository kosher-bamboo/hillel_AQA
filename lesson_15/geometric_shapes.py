from lesson_15.classes_geometric_shapes import Square, Triangle, Rectangle, Parallelogram, Rhombus, Trapezoid, Circle

square = Square(8)
triangle = Triangle(6, 14, 9)
rectangle = Rectangle(7, 9)
parallelogram = Parallelogram(10, 12, 14)
rhombus = Rhombus(13, 8)
trapezoid = Trapezoid(5, 8, 4, 10, 6)
circle = Circle(8)

list_of_figures = [square, triangle, rectangle, parallelogram, rhombus, trapezoid, circle]

for figure in list_of_figures:
    print(f"{figure}")
    print(f"    Perimeter: {figure.geometric_figure_perimeter()}")
    print(f"    Square: {figure.geometric_figure_square()}")
