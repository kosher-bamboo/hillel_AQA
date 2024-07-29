"""
Створіть абстрактний клас "Фігура" з абстрактиними методами для отримання площі та периметру.
Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично вірні для них методи для площі та периметру.
Властивості по типу “довжина сторони” и тд повинні бути приватними, та ініціалізуватись через конструктор.
Створіть Декілька різних об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та периметр кожної.
"""
from abc import ABC, abstractmethod
import math


class GeometricFigure(ABC):
    def __setattr__(self, key, value):
        # define the prefix for protected attributes
        prefix = f"_{self.__class__.__name__}__"
        # check if the attribute is a protected geometric property
        if key.startswith(prefix):
            # check if value is a proper number
            if isinstance(value, (int, float)) and value > 0:
                # set an attribute that match the check
                super().__setattr__(key, value)
            else:
                #  slicing string 'key' and return substring without prefix
                raise ValueError(f"Invalid value for {key[len(prefix):]}. The number must be correct.")
        else:
            # set an attribute that does not match the check
            super().__setattr__(key, value)

    @abstractmethod
    def geometric_figure_square(self):
        pass

    @abstractmethod
    def geometric_figure_perimeter(self):
        pass


class Square(GeometricFigure):

    def __init__(self, side_length):
        self.__side_length = side_length


    def geometric_figure_square(self):
        return self.__side_length ** 2

    def geometric_figure_perimeter(self):
        return self.__side_length * 4


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


class Rectangle(GeometricFigure):

    def __init__(self, side_1, side_2):
        self.__side_1 = side_1
        self.__side_2 = side_2


    def geometric_figure_square(self):
        return self.__side_1 * self.__side_2

    def geometric_figure_perimeter(self):
        return 2 * (self.__side_1 + self.__side_2)


class Parallelogram(GeometricFigure):

    def __init__(self, side_1, side_2, height):
        self.__side_1 = side_1
        self.__side_2 = side_2
        self.__height = height


    def geometric_figure_square(self):
        return self.__side_1 * self.__height

    def geometric_figure_perimeter(self):
        return 2 * (self.__side_1 + self.__side_2)


class Rhombus(GeometricFigure):

    def __init__(self, side_length, height):
        self.__side_length = side_length
        self.__height = height


    def geometric_figure_square(self):
        return self.__side_length * self.__height

    def geometric_figure_perimeter(self):
        return 4 * self.__side_length


class Trapezoid(GeometricFigure):
    def __init__(self, base_side_1, base_side_2, side_1, side_2, height):
        self.__base_side_1 = base_side_1
        self.__base_side_2 = base_side_2
        self.__side_1 = side_1
        self.__side_2 = side_2
        self.__height = height


    def geometric_figure_square(self):
        return (self.__base_side_1 + self.__base_side_2) * self.__height / 2

    def geometric_figure_perimeter(self):
        return self.__base_side_1 + self.__base_side_2 + self.__side_1 + self.__side_2


class Circle(GeometricFigure):
    def __init__(self, radius):
        self.__radius = radius


    def geometric_figure_square(self):
        return math.pi * self.__radius ** 2

    def geometric_figure_perimeter(self):
        return 2 * math.pi * self.__radius
