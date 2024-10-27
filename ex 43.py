# Коллекция __slots__
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point2D:
    __slots__ = ("x", "y")
    MAX_COORD = 100
    def __init__(self, x, y):
        self.x = x
        self.y = y


pt = Point(1, 2)
pt.z = 9
pt2 = Point2D(3,4)
print(pt.x, pt.y, pt2.x, pt2.y)
print(pt.__dict__)
pt2.y=999
print(pt2.y)
print(pt2.__slots__)
print(pt2.MAX_COORD)