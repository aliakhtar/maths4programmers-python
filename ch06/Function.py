from ch06.Vector import *


# Takes a function of 1 number. Can be called like a function and be passed a number, returns the result of calling
# its inner function on that variable
class Function(Vector):

    def __init__(self, f):
        self.f = f

    def __call__(self, number):
        #assert (str(number).isnumeric())
        return self.f(number)

    def scale(self, s):
        scaled = lambda n: self.f(n * s)
        return Function(scaled)

    def add(self, other):
        return Function(lambda n: other(n) + self.f(n))

    @classmethod
    def zero(cls):
        return Function(lambda n: 0)
