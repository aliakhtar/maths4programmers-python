from ch06.Vector import Vector


class Vec2(Vector):
    @classmethod
    def zero(cls):
        return Vec2(0, 0)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        assert self.__class__ == other.__class__
        return Vec2(self.x + other.x, self.y + other.y)

    def scale(self, s):
        return Vec2(self.x * s, self.y * s)

    def __eq__(self, other):
        return self.__class__ == other.__class__ \
               and self.x == other.x and self.y == other.y

    def __repr__(self):
        return "Vec2({}, {})".format(self.x, self.y)
