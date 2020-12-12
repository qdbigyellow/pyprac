""""Example using __slots__ to reduce memory"""

# Too many small objects can cause problems.
# ___dict__ stroe class properties.
# smaller object might make program faster, as they fit in the CPU cache line
# when CPU tries to access them，

class Point:
    """A 2D point"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        cls_name = self.__class__.__name__
        return f'{cls_name}({self.x!r}, {self.y!r})'


class SPoint:
    """A 2D point"""
    __slots__ = ['x', 'y']      # 用__slots__来限制小class的

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        cls_name = self.__class__.__name__
        return f'{cls_name}({self.x!r}, {self.y!r})'


if __name__ == '__main__':
    def alloc_points(n):
        return [Point(i, i) for i in range(n)]

    def alloc_spoints(n):
        return [SPoint(i, i) for i in range(n)]

    n = 1_000_000
    points = alloc_points(n)
    spoints = alloc_spoints(n)
