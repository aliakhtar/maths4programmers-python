from abc import ABCMeta, abstractmethod

class Vector(metaclass=ABCMeta):
    #def __init__(self):

    @abstractmethod
    def add(self, other):
        pass

    @abstractmethod
    def scale(self, other):
        pass

    @classmethod
    @abstractmethod
    def zero(cls):
        pass

    def subtract(self, other):
        return self.add(-1 * other)

    def __sub__(self, other):
        return self.subtract(other)

    def __add__(self, other):
        return self.add(other)

    def __mul__(self, s):
        return self.scale(s)

    def __rmul__(self, s):
        return self.scale(s)

    def __neg__(self):
        return self.scale(-1)
