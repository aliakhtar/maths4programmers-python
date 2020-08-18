class Vec2():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        return Vec2( self.x + other.x, self.y + other.y )

    def scale(self, s):
        return Vec2(self.x * s, self.y * s)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return self.add(other)

    def __mul__(self, s):
        return self.scale(s)

    def __rmul__(self, s):
        return self.scale(s)

    def __repr__(self):
        return "Vec2({}, {})".format(self.x, self.y)