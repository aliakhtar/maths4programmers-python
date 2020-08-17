from ch05.vectors import *


def linear_combination(scalars, *vectors):
    scaled = [scale(s, v) for (s, v) in zip(scalars, vectors)]
    return add(*scaled)

def multiply_matrix_vector(matrix, vector):
    scalars = vector
    vectors = zip(*matrix)
    return linear_combination(scalars, *vectors)
