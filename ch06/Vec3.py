from ch06.Vector import *


class Vec3(Vector):

    @classmethod
    def zero(cls):
        return Vec3(0, 0, 0)

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def add(self, other):
        return Vec3( self.x + other.x, self.y + other.y, self.z * other.z )

    def scale(self, s):
        return Vec3(self.x * s, self.y * s, self.z * s)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __repr__(self):
        return "Vec3({}, {}, {})".format(self.x, self.y, self.z)