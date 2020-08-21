from ch06.Vector import Vector


# Represents a function of the form f(x) = ax**2 + bx + c
class QuadraticFunction(Vector):
    def __init__(self, a, b, c ):
        self.a = a
        self.b = b
        self.c = c

    def __call__(self, x):
        return (self.a * (x ** 2)) + (self.b * x) + self.c

    def add(self, other):
        return QuadraticFunction(self.a + other.a, self.b + other.b, self.c + other.c)

    def scale(self, s):
        return QuadraticFunction(self.a * s, self.b * s, self.c * s)

    @classmethod
    def zero(cls):
        return QuadraticFunction(0, 0, 0)