from ch05.vectors import *


def linear_combination(scalars, *vectors):
    scaled = [scale(s, v) for (s, v) in zip(scalars, vectors)]
    return add(*scaled)


def multiply_matrix_vector(matrix, vector):
    scalars = vector
    vectors = zip(*matrix)
    return linear_combination(scalars, *vectors)


def multiply_matrix(a, b):
    # We'll view a as a list of its row vectors, and a as a list of its column vectors.
    # E.g if a = [
    # (a, b, c)
    # (d, e, f)
    # (g, h, i)  ]
    # then we'll take the rows (i.e (a, b, c), (d, e, f), (g, h, i ) from it.
    # And if b has the same values, we'll take (a, d, g), (b, e, h), and (c, f, i)

    # Then we want to go thru the rows, and for each row, go thru the cols and take their dot prod of the row.col
    # Each resulting value will be a point in the next column in the result.

    # E.g result = [
    # (r1.c1 , r1.c2,  r1.c3),
    # (r2.c1,  r2.c2,  r2.c3),
    # (r3.c1,  r3.c2,  r3.c3) ]
    # In the end we zip the columns together to put them all in the same matrix and return the result.

    # I.e each row in the result matrix is a tuple of all dot products of a particular row w/ all cols

    return tuple(
        tuple(dot(row, col) for col in zip(*b))
        for row in a
    )