from abc import abstractmethod

from ch06.Vector import Vector
from ch06.vectors import add, scale


class CoordinateVector(Vector):

    def __init__(self, *coordinates):
        self.coordinates = tuple(x for x in coordinates)

    @abstractmethod
    def dimension(self):
        pass

    def add(self, other):
        return self.__class__(*add(self.coordinates, other.coordinates))

    def scale(self, s):
        return self.__class__(*scale(s, self.coordinates))

    def __eq__(self, other):
        if not self.__class__ == other.__class__:
            return False

        if not self.dimension() == other.dimension():
            return False

        for i in range(0, len(self.coordinates)):
            if not self.coordinates[i] == other.coordinates[i]:
                print("Nope, {}, {}, {}".format(i, self.coordinates[i], other.coordinates[i]))
                return False

        return True

    def __repr__(self):
        return "{} {}".format(self.__class__.__qualname__, self.coordinates)
