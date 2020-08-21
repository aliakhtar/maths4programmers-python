from ch06.Vector import Vector


# Represents a function of the form f(x) = ax + b where a and b are scalars / constants
class LinearFunction(Vector):
    def __init__(self, a, b ):
        self.a = a
        self.b = b

    def __call__(self, x):
        return (self.a * x) + self.b

    def add(self, other):
        return LinearFunction(self.a + other.a, self.b + other.b)

    def scale(self, s):
        return LinearFunction(self.a * s, self.b * s)

    @classmethod
    def zero(cls):
        return LinearFunction(0, 0)