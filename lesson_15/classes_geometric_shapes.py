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

    @abstractmethod
    def geometric_figure_perimeter(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Square(GeometricFigure):

    def __init__(self, side_length):
        self.__side_length = side_length

    def __setattr__(self, key, value):
        if key == "_Square__side_length":
            if type(value) in (int, float) and value > 0:
                super().__setattr__(key, value)
            else:
                raise ValueError("value is incorrect")
        else:
            super().__setattr__(key, value)

    def geometric_figure_square(self):
        return self.__side_length ** 2

    def geometric_figure_perimeter(self):
        return self.__side_length * 4

    def __str__(self):
        return "Square"


class Triangle(GeometricFigure):

    def __init__(self, side_1_length, side_2_length, side_3_length):
        self.__side_1_length = side_1_length
        self.__side_2_length = side_2_length
        self.__side_3_length = side_3_length

    def __setattr__(self, key, value):
        if key in ("_Triangle__side_1_length", "_Triangle__side_2_length", "_Triangle__side_3_length"):
            if type(value) in (int, float) and value > 0:
                super().__setattr__(key, value)
            else:
                raise ValueError("value is incorrect")
        else:
            super().__setattr__(key, value)

    def geometric_figure_square(self):
        # Heron's formula
        p = (self.__side_1_length + self.__side_2_length + self.__side_3_length) / 2
        triangle_square = math.sqrt(
            p * (p - self.__side_1_length) * (p - self.__side_2_length) * (p - self.__side_3_length))
        return triangle_square

    def geometric_figure_perimeter(self):
        return self.__side_1_length + self.__side_2_length + self.__side_3_length

    def __str__(self):
        return "Triangle"


class Rectangle(GeometricFigure):

    def __init__(self, side_1, side_2):
        self.__side_1 = side_1
        self.__side_2 = side_2

    def __setattr__(self, key, value):
        if key in ("_Rectangle__side_1", "_Rectangle__side_2"):
            if type(value) in (int, float) and value > 0:
                super().__setattr__(key, value)
            else:
                raise ValueError("value is incorrect")
        else:
            super().__setattr__(key, value)

    def geometric_figure_square(self):
        return self.__side_1 * self.__side_2

    def geometric_figure_perimeter(self):
        return 2 * (self.__side_1 + self.__side_2)

    def __str__(self):
        return "Rectangle"


class Parallelogram(GeometricFigure):

    def __init__(self, side_1, side_2, height):
        self.__side_1 = side_1
        self.__side_2 = side_2
        self.__height = height

    def __setattr__(self, key, value):
        if key in ("_Parallelogram__side_1", "_Parallelogram__side_2", "_Parallelogram__height"):
            if type(value) in (int, float) and value > 0:
                super().__setattr__(key, value)
            else:
                raise ValueError("value is incorrect")
        else:
            super().__setattr__(key, value)

    def geometric_figure_square(self):
        return self.__side_1 * self.__height

    def geometric_figure_perimeter(self):
        return 2 * (self.__side_1 + self.__side_2)

    def __str__(self):
        return "Parallelogram"


class Rhombus(GeometricFigure):

    def __init__(self, side_length, height):
        self.__side_length = side_length
        self.__height = height

    def __setattr__(self, key, value):
        if key in ("_Rhombus__side_length", "_Rhombus__height"):
            if type(value) in (int, float) and value > 0:
                super().__setattr__(key, value)
            else:
                raise ValueError("value is incorrect")
        else:
            super().__setattr__(key, value)

    def geometric_figure_square(self):
        return self.__side_length * self.__height

    def geometric_figure_perimeter(self):
        return 4 * self.__side_length

    def __str__(self):
        return "Rhombus"


class Trapezoid(GeometricFigure):
    def __init__(self, base_side_1, base_side_2, side_1, side_2, height):
        self.__base_side_1 = base_side_1
        self.__base_side_2 = base_side_2
        self.__side_1 = side_1
        self.__side_2 = side_2
        self.__height = height

    def __setattr__(self, key, value):
        if key in ("_Trapezoid__base_side_1", "_Trapezoid__base_side_2", "_Trapezoid__side_1", "_Trapezoid__side_2", "_Trapezoid__height"):
            if type(value) in (int, float) and value > 0:
                super().__setattr__(key, value)
            else:
                raise ValueError("value is incorrect")
        else:
            super().__setattr__(key, value)

    def geometric_figure_square(self):
        return (self.__base_side_1 + self.__base_side_2) * self.__height / 2

    def geometric_figure_perimeter(self):
        return self.__base_side_1 + self.__base_side_2 + self.__side_1 + self.__side_2

    def __str__(self):
        return "Trapezoid"


class Circle(GeometricFigure):
    def __init__(self, radius):
        self.__radius = radius

    def __setattr__(self, key, value):
        if key == "_Circle__radius":
            if type(value) in (int, float) and value > 0:
                super().__setattr__(key, value)
            else:
                raise ValueError("value is incorrect")
        else:
            super().__setattr__(key, value)

    def geometric_figure_square(self):
        return math.pi * self.__radius ** 2

    def geometric_figure_perimeter(self):
        return 2 * math.pi * self.__radius

    def __str__(self):
        return "Circle"

