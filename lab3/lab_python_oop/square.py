from .rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, side, color):
        super().__init__(side, side, color)
        self._name = "Квадрат"

    def __repr__(self):
        return super().__repr__()
