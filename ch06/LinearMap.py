from ch06.Vector import Vector
from ch06.vectors import dot
from ch06.Matrix import Matrix5x3


class LinearMap3d_to_5d(Vector):

    def __init__(self, matrix):
        assert (matrix.rows() == 5)
        assert (matrix.cols() == 3)
        self.matrix = matrix

    def add(self, other):
        new_m = self.matrix.add(other.matrix)
        return LinearMap3d_to_5d(new_m)

    def scale(self, s):
        new_m = self.matrix.scale(s)
        return LinearMap3d_to_5d(new_m)

    def zero(self):
        m = self.matrix.zero()
        return LinearMap3d_to_5d(m)

    def __call__(self, other):
        assert(other.rows() == 3)
        matrix = tuple(
            tuple(dot(row, col) for col in zip(*other.matrix))
            for row in self.matrix.matrix
        )
        return LinearMap3d_to_5d(Matrix5x3(matrix))