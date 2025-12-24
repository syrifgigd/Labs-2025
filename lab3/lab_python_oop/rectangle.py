from .figure import Figure
from .color import Color

class Rectangle(Figure):
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = Color(color)
        self._name = "Прямоугольник"

    @property
    def name(self):
        return self._name

    def area(self):
        return self.width * self.height

    def __repr__(self):
        return "{} {} цвета шириной {} и высотой {} площадью {}.".format(
            self.name,
            self.color.color,
            self.width,
            self.height,
            self.area()
        )
