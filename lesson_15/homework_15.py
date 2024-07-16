"""
Створіть абстрактний клас "Фігура" з абстрактиними методами для отримання площі та периметру.
Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично вірні для них методи для площі та периметру.
Властивості по типу “довжина сторони” и тд повинні бути приватними, та ініціалізуватись через конструктор.
Створіть Декілька різних об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та периметр кожної.
"""
from abc import ABC, abstractmethod
import math


class GeometricFigure(ABC):

    @abstractmethod
    def geometric_figure_square(self):
        pass

    def geometric_figure_perimeter(self):
        pass

    def figure_name(self):
        pass


class Square(GeometricFigure):
    def __init__(self, side_length):
        self.__side_length = side_length

    def geometric_figure_square(self):
        return self.__side_length ** 2

    def geometric_figure_perimeter(self):
        return self.__side_length * 4

    def figure_name(self):
        return "Square"


class Triangle(GeometricFigure):
    def __init__(self, side_1_length, side_2_length, side_3_length):
        self.__side_1_length = side_1_length
        self.__side_2_length = side_2_length
        self.__side_3_length = side_3_length

    def geometric_figure_square(self):
        # Heron's formula
        p = (self.__side_1_length + self.__side_2_length + self.__side_3_length) / 2
        triangle_square = math.sqrt(
            p * (p - self.__side_1_length) * (p - self.__side_2_length) * (p - self.__side_3_length))
        return triangle_square

    def geometric_figure_perimeter(self):
        return self.__side_1_length + self.__side_2_length + self.__side_3_length

    def figure_name(self):
        return "Triangle"

class Circle(GeometricFigure):
    def __init__(self, radius):
        self.__radius = radius

    def geometric_figure_square(self):
        return math.pi * self.__radius ** 2

    def geometric_figure_perimeter(self):
        return "Can't calculate perimeter for circle"

    def figure_name(self):
        return "Circle"


square1 = Square(6)
triangle1 = Triangle(3, 4, 5)
circle1 = Circle(5)

list_of_figures = [square1, triangle1, circle1]
for figure in list_of_figures:
    print(f"{figure.figure_name()}")
    print(f"    Perimeter: {figure.geometric_figure_perimeter()}")
    print(f"    Square: {figure.geometric_figure_square()}")