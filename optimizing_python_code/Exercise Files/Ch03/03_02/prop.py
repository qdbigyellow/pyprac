"""Properties example"""

# Python 只有在必要的时候用property
# p1 = Point(1, 2)
# %timeit p1.x
# p2 = PPoint(1, 2)
# %timeit p2.x
# p2 is 4 times slower than p1

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class PPoint:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError(type(value))
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError(type(value))
        self._y = value
