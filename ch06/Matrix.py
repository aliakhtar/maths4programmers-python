from abc import abstractmethod

from ch06.Vector import Vector


class Matrix(Vector):

    def __init__(self, matrix):
        self.matrix = matrix

    @abstractmethod
    def rows(self):
        pass

    @abstractmethod
    def cols(self):
        pass

    def add(self, other):
        new_matrix = tuple(
            tuple(a + b for (a, b) in zip(row1, row2))
            for row1, row2 in zip(self.matrix, other.matrix)
        )
        return self.__class__(new_matrix)

    def scale(self, s):
        new_matrix = tuple(
            tuple(a * s for a in row)
            for row in self.matrix
        )

        return self.__class__(new_matrix)

    def zero(self):
        new_m = tuple(
            tuple(0 for _ in range(self.cols()))
            for _ in range(self.rows())
        )
        self.__class__(new_m)

    def __repr__(self):
        return "{}{}".format(self.__class__.__qualname__, self.matrix)
