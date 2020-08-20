from ch06.Vector import *

from ch06.functions import approx_equal_funcs


# Same as Function but takes a function that operates on two numbers instead
class Function2(Vector):

    def __init__(self, f):
        self.f = f

    def __call__(self, a, b):
        # assert (str(number).isnumeric())
        return self.f(a, b)

    def scale(self, s):
        scaled = lambda a, b: self.f(a, b) * s
        return Function2(scaled)

    def add(self, other):
        return Function2(lambda a, b: other(a, b) + self.f(a, b))

    @classmethod
    def zero(cls):
        return Function2(lambda a, b: 0)
